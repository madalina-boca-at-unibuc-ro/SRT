from ursina import *
import numpy as np
from lambda2rgb import wavelength_to_rgb


c = 1
initial_sphere_wavelength = 500
sphere_velocity = 0.1 * c


class MovingSphere_1(Entity):
    def __init__(self, start_pos, direction):
        super().__init__(
            model="sphere",
            color=color.gray,
            texture="white_cube",
            position=start_pos,
            scale=0.5,
        )
        self.origin = Vec3(start_pos)
        self.direction = direction
        self.speed = sphere_velocity
        self.velocity = self.direction * self.speed
        self.beta = self.velocity / c
        self.time = 0.0
        self.wavelength = initial_sphere_wavelength
        self.color = color.gray

    def update(self, o=None):
        if o is None or not hasattr(o, "position"):
            return  # Do nothing if observer is not valid
        # linear motion
        self.position = self.origin + self.direction * self.time * self.speed
