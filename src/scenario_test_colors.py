from ursina import *
from moving_sphere_2 import MovingSphere_2
from observer_file_2 import Observer_2
from lambda2rgb import wavelength_to_rgb
import numpy as np


class ScenarioTestColors:
    def __init__(self, escape_callback=None):
        self.dt = 0.01
        self.t = 0
        self.player = Observer_2(start_pos=Vec3(0, 1, -20))
        self.escape_callback = escape_callback
        self.update_interval = 0.01
        self.accumulated_time = 0

        self.sky = Sky()

        # grila de sfere
        self.spheres = []
        grid_x_size = 100
        spacing = 0.125
        offset_x = -grid_x_size // 2 * spacing
        wavelength_grid = np.linspace(300, 800, grid_x_size)

        # Create spheres in a 2x2 vertical grid
        sphere_positions = []
        for ix, x in enumerate(range(grid_x_size)):
            pos = Vec3(offset_x + x * spacing, 0.5, 0.5)
            sphere = MovingSphere_2(start_pos=pos)
            self.spheres.append(sphere)
            sphere_positions.append((x, pos))
            sphere.color = color.rgb(*wavelength_to_rgb(wavelength_grid[ix]))

        # ui
        self.text_box = Text(
            text="list of colors",
            origin=(-0.5, 0),
            x=-0.75,
            y=-0.35,
            scale=0.8,
            z=-1,
            parent=camera.ui,
            color=color.red,
        )

    def input(self, key):
        if key == "escape":
            if self.escape_callback:
                self.escape_callback()

    def update(self):
        self.accumulated_time += time.dt
        if self.accumulated_time >= self.update_interval:
            self.accumulated_time -= self.update_interval
            self.t += self.update_interval
            self.player.update(self.t)

    def cleanup(self):
        destroy(self.player)
        destroy(self.sky)
        destroy(self.text_box)
        for sphere in self.spheres:
            destroy(sphere)
        self.spheres.clear()
