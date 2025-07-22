from ursina import *
from moving_sphere_2 import MovingSphere_2
from observer_file_2 import Observer_2


class Scenario2:
    def __init__(self, escape_callback=None):

        self.dt = 0.04
        self.t = 0
        self.running_state = False  # Initialize running_state for clarity
        self.player = Observer_2()
        self.escape_callback = escape_callback
        self.update_interval = 0.04
        self.accumulated_time = 0

        self.sky = Sky()

        # grila de sfere
        self.spheres = []
        self.lines = []
        grid_x_size = 100
        grid_y_size = 100
        spacing = 0.125
        offset_x = -grid_x_size // 2 * spacing
        offset_y = -grid_y_size // 2 * spacing

        # Create spheres in a 2x2 horizontal grid
        sphere_positions = []
        for x in range(grid_x_size):
            for y in range(grid_y_size):
                pos = Vec3(offset_x + x * spacing, -0.5, offset_y + y * spacing)
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

        # Speed input UI
        self.speed_input_label = Text(
            text="Set observer speed (0 to 0.99):",
            origin=(-0.5, 0),
            x=-0.75,
            y=0.4,
            scale=0.8,
            parent=camera.ui,
            color=color.white,
        )

        self.speed_input_field = InputField(
            default_value="0.1",
            limit_content_to="0123456789.",
            character_limit=5,
            scale=(0.4, 0.1),
            x=-0.2,
            y=0.4,
            parent=camera.ui,
        )

        self.speed_set_button = Button(
            text="Set Speed",
            scale=(0.1, 0.05),
            x=0.05,
            y=0.4,
            color=color.azure,
            highlight_color=color.light_gray,
            pressed_color=color.lime,
            parent=camera.ui,
        )

        def apply_speed():
            try:
                speed = float(self.speed_input_field.text)
                speed = max(0, min(speed, 0.99))  # Clamp
                self.player.speed = speed
                print(f"Observer speed set to: {speed}")
            except ValueError:
                print("Invalid input")

            mouse.locked = True
            mouse.visible = False

        self.speed_set_button.on_click = apply_speed

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

        self.player.input_field_focus_ref = lambda: self.speed_input_field.focused

    def input(self, key):
        if key == "escape":
            if self.escape_callback:
                self.cleanup()  # Ensure cleanup on escape
                self.escape_callback()
        elif key == "space":  # Add space key for pause/resume if desired for Scenario 2
            self.running_state = not self.running_state
            if self.running_state:
                print("Scenario 2 Running.")
                mouse.locked = True
                mouse.visible = False
            else:
                print("Scenario 2 Paused.")
                mouse.locked = False
                mouse.visible = True

    def update(self):
        self.accumulated_time += time.dt
        if self.accumulated_time >= self.update_interval:
            self.accumulated_time -= self.update_interval
            self.t += self.update_interval
            self.state_text.text = f"Time: {self.t:.2f}s"
            self.player.update(self.t, mouse.locked)
            for sphere in self.spheres:
                sphere.update(self.player, self.t)  # update culori

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

        if hasattr(self, "speed_set_button") and self.speed_set_button is not None:
            destroy(self.speed_set_button)
            self.speed_set_button = None
        if hasattr(self, "speed_input_field") and self.speed_input_field is not None:
            destroy(self.speed_input_field)
            self.speed_input_field = None
        if hasattr(self, "speed_input_label") and self.speed_input_label is not None:
            destroy(self.speed_input_label)
            self.speed_input_label = None
