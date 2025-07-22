from ursina import *
import math

c = 1  # viteza luminii normaliz (1 = v max!!!!!!!!!)


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


class Observer_2(Entity):
    def __init__(self, start_pos=Vec3(0, 1, -10), initial_speed=0.0):
        super().__init__()
        self.position = start_pos
        self.speed = initial_speed
        self.speed = min(self.speed, 0.99 * c)  # Viteza de mișcare
        self.velocity = Vec3(0)

        # config cam
        camera.parent = self
        camera.position = Vec3(0, 0, 0)
        camera.rotation = (0, 0, 0)

    def orient_camera(self):
        target_position = Vec3(0, 0, 0)
        self.look_at(target_position)

    def update(self, t=0, mouse_locked=False):
        self.velocity = Vec3(
            held_keys["d"] - held_keys["a"],
            held_keys["left shift"] - held_keys["right shift"],
            held_keys["w"] - held_keys["s"],
        )

        # normalize only if at least one key is pressed
        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalized() * self.speed
        else:
            self.velocity = Vec3(0)

        self.position += self.velocity * time.dt
        if mouse_locked:
            self.rotation_y += mouse.velocity[0] * 30
            camera.rotation_x -= mouse.velocity[1] * 30
            camera.rotation_x = clamp(camera.rotation_x, -90, 90)
