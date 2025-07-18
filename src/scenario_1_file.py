from ursina import *
import numpy as np

from observer_file_1 import Observer_1
from deformed_cube import DeformedCube

c = 1.0
cube_side_length = 5
initial_velocity = Vec3(0.0 * c, 0.0 * c, 0.5 * c)


def update_real_positions(t, initial_positions, velocity):
    new_positions = []
    for initial_position in initial_positions:
        new_positions.append(initial_position + velocity * t)
    return new_positions


starting_positions = [
    Vec3(0, 0, 0),
    Vec3(cube_side_length, 0, 0),
    Vec3(0, 0, cube_side_length),
    Vec3(cube_side_length, 0, cube_side_length),
    Vec3(0, cube_side_length, 0),
    Vec3(cube_side_length, cube_side_length, 0),
    Vec3(0, cube_side_length, cube_side_length),
    Vec3(cube_side_length, cube_side_length, cube_side_length),
]

initial_origin = Vec3(5, 10, 0)

for position in starting_positions:
    position += initial_origin


def ret_time(t, Delta, beta):
    v2 = beta.dot(beta) * c * c
    Delta2 = Delta.dot(Delta)
    v_dot_Delta = beta.dot(Delta) * c
    den = c * c - v2
    num = (
        c * c * t
        - v_dot_Delta
        - np.sqrt(
            (c * c - v2) * (Delta2 - (c * t) ** 2) + (c * c * t - v_dot_Delta) ** 2
        )
    )
    res = num / den
    if res < 0:
        res = 0
    return res


def update_apparent_positions(t, initial_positions, observer_position, velocity):
    new_positions = []
    for i, initial_position in enumerate(initial_positions):
        Delta = observer_position - initial_position
        beta = velocity / c
        t_ret = ret_time(t, Delta, beta)
        new_positions.append(initial_position + velocity * t_ret)
    return new_positions


class Scenario1:
    def __init__(self, escape_callback=None):
        self.dt = 0.01
        self.t = 0
        self.running_state = False

        # Create observer with reference to running state
        self.player = Observer_1(running_state_ref=lambda: self.running_state)

        self.ground = Entity(
            model="plane",
            scale=(100, 1, 100),
            color=color.light_gray,
            collider="box",
            texture="white_cube",
            texture_scale=(100, 100),
        )
        self.escape_callback = escape_callback

        # Add sky
        self.sky = Sky()

        self.real_cube = DeformedCube(
            positions=starting_positions,
            sphere_color=color.white,
            line_color=color.white,
        )
        self.real_cube_positions = starting_positions
        self.real_cube_velocity = initial_velocity

        self.apparent_cube = DeformedCube(
            positions=starting_positions, sphere_color=color.red, line_color=color.red
        )
        self.apparent_cube_positions = starting_positions
        self.apparent_cube_velocity = initial_velocity

        self.text_box = Text(
            text="WASD: Horizontal Movement (paused only)\nRight SHIFT: Move Down (paused only)\nLeft SHIFT: Move Up (paused only)\n r: Reset Camera\n SPACE: Start/Pause\n\nWatch the cubes rotate due to the Terrell Rotation effect!",
            origin=(-0.5, 0),
            x=-0.75,
            y=-0.35,
            scale=0.8,
            z=-1,
            parent=camera.ui,
            color=color.red,
        )

        self.state_text = Text(
            text="Paused",
            origin=(-0.5, 0),
            x=-0.75,
            y=0.25,
            scale=0.8,
            z=-1,
            parent=camera.ui,
            color=color.red,
        )

        self.title = Text(
            "The Terrell Rotation",
            scale=2,
            y=0.3,
            origin=(0, 0),
            z=-1,
            parent=camera.ui,
            color=color.white,
        )

    def input(self, key):
        if key == "escape":
            if self.escape_callback:
                self.escape_callback()
        elif key == "space":
            self.toggle_pause()
        elif key == "r":
            self.player.orient_camera(target_position=self.apparent_cube_positions[0])

    def toggle_pause(self):
        """Toggle between running and paused states"""
        self.running_state = not self.running_state

    def update(self):
        # Always update the observer to handle movement and mouse look
        self.player.update()

        if self.running_state:
            self.t += self.dt
            self.state_text.text = "Running" + f"\nTime: {self.t:.2f}s"
            self.real_cube_positions = update_real_positions(
                self.t, starting_positions, self.real_cube_velocity
            )
            self.apparent_cube_positions = update_apparent_positions(
                self.t,
                starting_positions,
                self.player.position,
                self.apparent_cube_velocity,
            )
            self.real_cube.update(new_positions=self.real_cube_positions)
            self.apparent_cube.update(new_positions=self.apparent_cube_positions)
        else:
            self.state_text.text = "Paused" + f"\nTime: {self.t:.2f}s"

    def cleanup(self):
        """Clean up all entities created by this scenario"""
        if hasattr(self, "player"):
            destroy(self.player)
        if hasattr(self, "ground"):
            destroy(self.ground)
        if hasattr(self, "sky"):
            destroy(self.sky)
        if hasattr(self, "text_box"):
            destroy(self.text_box)
        if hasattr(self, "state_text"):
            destroy(self.state_text)
        if hasattr(self, "title"):
            destroy(self.title)
        if hasattr(self, "real_cube"):
            self.real_cube.cleanup()  # Clean up child entities first
            destroy(self.real_cube)
        if hasattr(self, "apparent_cube"):
            self.apparent_cube.cleanup()  # Clean up child entities first
            destroy(self.apparent_cube)
