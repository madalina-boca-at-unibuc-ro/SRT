from ursina import *
from moving_sphere_2 import MovingSphere_2
from observer_file_2 import Observer_2


class Scenario2:
    def __init__(self, escape_callback=None):
        self.dt = 0.01
        self.t = 0
        self.running_state = False
        self.player = Observer_2(running_state_ref=lambda: self.running_state)
        self.escape_callback = escape_callback

        self.sky = Sky()

        # grila de sfere
        self.spheres = []
        self.lines = []
        grid_x_size = 100
        grid_y_size = 20
        spacing = 0.125
        offset_x = -grid_x_size // 2 * spacing
        offset_y = -grid_y_size // 2 * spacing

        # Create spheres in a 2x2 vertical grid
        sphere_positions = []
        for x in range(grid_x_size):
            for y in range(grid_y_size):
                pos = Vec3(offset_x + x * spacing, offset_y + y * spacing, 0.5)
                sphere = MovingSphere_2(start_pos=pos)
                self.spheres.append(sphere)
                sphere_positions.append((x, y, pos))

        # ui
        self.text_box = Text(
            text="WASD: Move\nShift: Up/Down\nSPACE: Pause/Resume\nESC: Back to Menu",
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

    def input(self, key):
        if key == "escape":
            if self.escape_callback:
                self.escape_callback()
        elif key == "space":
            self.running_state = not self.running_state

    def update(self):
        self.player.update()

        for sphere in self.spheres:
            sphere.update(self.player)  # update culori

        if self.running_state:
            self.t += self.dt
            self.state_text.text = f"Running\nTime: {self.t:.2f}s"
        else:
            self.state_text.text = f"Paused\nTime: {self.t:.2f}s"

    def cleanup(self):
        destroy(self.player)
        destroy(self.sky)
        destroy(self.text_box)
        destroy(self.state_text)
        for sphere in self.spheres:
            destroy(sphere)
        for line in self.lines:
            destroy(line)
        self.spheres.clear()
        self.lines.clear()
