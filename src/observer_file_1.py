from ursina import *
import numpy as np


class Observer_1(Entity):
    def __init__(self, running_state_ref=None):
        super().__init__()
        # Set observer position
        self.position = Vec3(-25, 10.5, 5)
        self.speed = 5
        # Reference to running state from scenario
        self.running_state_ref = running_state_ref

        # Set up camera as child of observer
        camera.parent = self
        camera.position = Vec3(0, 0, 0)  # Camera at observer's position
        camera.rotation = (0, 0, 0)

        # Point camera towards origin
        direction_to_origin = Vec3(0, 0, 0) - self.position
        self.rotation_y = (
            np.atan2(direction_to_origin.x, direction_to_origin.z) * 180 / pi
        )

    def orient_camera(self, target_position=Vec3(0, 0, 0)):
        # rotate camera to look at origin
        direction_to_origin = target_position - self.position
        self.rotation_y = (
            np.atan2(direction_to_origin.x, direction_to_origin.z) * 180 / pi
        )

    def update(self):
        # Only allow movement when simulation is paused
        is_running = self.running_state_ref() if self.running_state_ref else False
        if not is_running:
            # Movement
            move = (
                Vec3(1, 0, 0) * (held_keys["w"] - held_keys["s"])
                + Vec3(0, 0, 1) * (held_keys["a"] - held_keys["d"])
                + Vec3(0, 1, 0) * (held_keys["left shift"] - held_keys["right shift"])
            ).normalized()
            self.position += move * time.dt * self.speed

        # Mouse look (always enabled)
        self.rotation_y += mouse.velocity[0] * 60
        camera.rotation_x -= mouse.velocity[1] * 80
        if held_keys["right mouse"]:
            camera.rotation_z += mouse.velocity[0] * 40
