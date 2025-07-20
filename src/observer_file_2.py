from ursina import *
import math

c = 1  # viteza luminii normaliz (1 = v max!!!!!!!!!)


def clamp(value, min_val, max_val):
    return max(min_val, min(max_val, value))


class Observer_2(Entity):
    def __init__(self, running_state_ref=None):
        super().__init__()
        self.position = Vec3(0, 1, -10)
        self.speed = 4  # Viteza de mișcare
        self.running_state_ref = running_state_ref

        # config cam
        camera.parent = self
        camera.position = Vec3(0, 0, 0)
        camera.rotation = (0, 0, 0)
        self.orient_camera()

    def orient_camera(self):
        target_position = Vec3(0, 0, 0)
        self.look_at(target_position)

    def update(self):
        move = Vec3(
            held_keys["d"] - held_keys["a"],
            held_keys["left shift"] - held_keys["right shift"],
            held_keys["w"] - held_keys["s"],
        )

        # normaliz doar daca se apasa cel putin o tasta
        if move.length() > 0:
            move = move.normalized() * min(
                self.speed, 0.99 * c
            )  # acum 'c' este definita
        else:
            move = Vec3(0)

        self.position += move * time.dt

        # control camera cu mouse (sau touchpad actually)
        self.rotation_y += mouse.velocity[0] * 40
        camera.rotation_x -= mouse.velocity[1] * 40
        camera.rotation_x = clamp(camera.rotation_x, -90, 90)
