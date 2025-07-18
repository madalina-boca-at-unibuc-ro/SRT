from ursina import *
from lambda2rgb import wavelength_to_rgb
import math

c = 1  # viteza luminii (normalizata)
initial_wavelength = 500  # Culoare init (verde-albastruissshh sa zicem)


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


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

    def update(self, observer=None):
        if observer is None:
            return

        # vector obs - sfera
        relative_pos = self.position - observer.position
        distance = relative_pos.length()

        if distance > 0:
            direction_to_observer = relative_pos.normalized()

            # Use observer's actual velocity based on movement
            observer_velocity = Vec3(0, 0, 0)
            if hasattr(observer, "speed"):
                # Calculate velocity based on movement direction
                move_direction = Vec3(
                    held_keys["d"] - held_keys["a"], 0, held_keys["w"] - held_keys["s"]
                )
                if move_direction.length() > 0:
                    observer_velocity = move_direction.normalized() * observer.speed

            # doppler (cu protectie anti-viteze > c!!!!!!!!!!!!!!!!!!!!!!!!!!)
            observer_beta = observer_velocity / c
            beta_squared = observer_beta.length_squared()

            # evitam eroarea matem
            if beta_squared >= 1:
                beta_squared = 0.99  # fortat o valoare sub c neap

            beta_dot_r = observer_beta.dot(direction_to_observer)
            wavelength_factor = (1 - beta_dot_r) / math.sqrt(1 - beta_squared)

            # update de culoare
            self.wavelength = initial_wavelength * wavelength_factor
            self.wavelength = clamp(
                self.wavelength, 380, 780
            )  # domeniu extra vizibil :)  (380-780nm)
            self.color = color.rgb(*wavelength_to_rgb(self.wavelength))
