from ursina import *
import numpy as np
from lambda2rgb import wavelength_to_rgb


c = 1
initial_sphere_wavelength = 500
sphere_velocity = 0.1 * c


def ret_time(t, Delta, beta):
    beta2 = beta.dot(beta)
    Delta2 = Delta.dot(Delta)
    beta_dot_Delta = beta.dot(Delta)
    den = c * (1 - beta2)
    num = (
        c * t
        - beta_dot_Delta
        - np.sqrt((1 - beta2) * (Delta2 - (c * t) ** 2) + (c * t - beta_dot_Delta) ** 2)
    )
    return num / den


class ApparentSphere_1(Entity):
    def __init__(self, start_pos, direction):
        super().__init__(
            model="sphere",
            color=color.red,
            texture="white_cube",
            position=start_pos,
            initial_position=start_pos,
            scale=0.5,
        )
        self.origin = Vec3(start_pos)
        self.direction = direction
        self.speed = sphere_velocity
        self.velocity = self.direction * self.speed
        self.beta = self.velocity / c
        self.time = 0.0
        self.retarded_time = self.time
        self.wavelength = initial_sphere_wavelength
        self.color = color.rgb(*wavelength_to_rgb(initial_sphere_wavelength))

    def update(self, o=None):
        if o is None or not hasattr(o, "position"):
            return  # Do nothing if observer is not valid
        # linear motion
        relative_position = self.position - o.position
        self.retarded_time = ret_time(self.time, relative_position, self.beta)
        self.position = self.origin + self.direction * self.retarded_time * self.speed

        # Calculate position vector relative to observer
        self.relative_position = self.position - o.position
        self.relative_position = self.relative_position.normalized()

        # Calculate scalar product between relative_position and beta
        self.beta_dot_r = self.beta.dot(self.relative_position)

        wavelength_factor = (1 + self.beta_dot_r) / (
            np.sqrt(1 - self.beta.length() ** 2)
        )
        self.wavelength = initial_sphere_wavelength * wavelength_factor
        self.color = color.rgb(*wavelength_to_rgb(self.wavelength))
