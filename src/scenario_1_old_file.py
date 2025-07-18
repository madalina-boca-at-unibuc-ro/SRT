from ursina import *
import numpy as np

from observer_file_1 import Observer_1
from moving_sphere_1 import MovingSphere_1
from aparent_sphere_1 import ApparentSphere_1


cube_side_length = 15

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


class Scenario1_old:
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

        self.moving_spheres = []
        for i in range(8):
            self.moving_spheres.append(
                MovingSphere_1(start_pos=starting_positions[i], direction=Vec3(0, 0, 1))
            )

        self.apparent_spheres = []
        for i in range(8):
            self.apparent_spheres.append(
                ApparentSphere_1(
                    start_pos=starting_positions[i], direction=Vec3(0, 0, 1)
                )
            )

        # Add a clock
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
            "The Doppler Effect",
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
            self.player.orient_camera(target_position=Vec3(0, 0, 0))

    def toggle_pause(self):
        """Toggle between running and paused states"""
        self.running_state = not self.running_state

    def update(self):
        # Always update the observer to handle movement and mouse look
        self.player.update()

        if self.running_state:
            self.t += self.dt
            self.state_text.text = "Running" + f"\nTime: {self.t:.2f}s"
            # Update moving sphere
            for sphere in self.moving_spheres:
                sphere.time = self.t
                sphere.update(self.player)
            for sphere in self.apparent_spheres:
                sphere.time = self.t
                sphere.update(self.player)
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
        for sphere in self.moving_spheres:
            destroy(sphere)
        for sphere in self.apparent_spheres:
            destroy(sphere)
        self.moving_spheres.clear()
        self.apparent_spheres.clear()
