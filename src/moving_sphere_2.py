from ursina import *
from lambda2rgb import wavelength_to_rgb
import math

c = 1  # viteza luminii (normalizata)
initial_wavelength = 500  # Culoare init (verde-albastruissshh sa zicem)


class MovingSphere_2(Entity):
    def __init__(self, start_pos, direction=Vec3(0)):
        super().__init__(
            model="sphere",
            color=color.rgb(*wavelength_to_rgb(initial_wavelength)),
            position=start_pos,
            scale=0.1,
        )
        self.start_pos = Vec3(start_pos)
        self.direction = direction.normalized()
        self.speed = 0  # Sferele sunt staționare
        self.wavelength = initial_wavelength

    def update(self, observer=None, t=0):
        if observer is None:
            return

        relative_pos = observer.position - self.position
        distance = relative_pos.length()
        if distance > 0:
            direction_to_observer = relative_pos.normalized()

            # doppler (cu protectie anti-viteze > c!!!!!!!!!!!!!!!!!!!!!!!!!!)
            observer_beta = observer.velocity / c
            beta_squared = min(observer_beta.length_squared(), 0.99)

            beta_dot_r = observer_beta.dot(direction_to_observer)
            wavelength_factor = math.sqrt(1 - beta_squared) / (1 - beta_dot_r)

            # update de culoare
            self.wavelength = initial_wavelength * wavelength_factor
            self.color = color.rgb(*wavelength_to_rgb(self.wavelength))
