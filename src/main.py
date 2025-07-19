import os
import sys 

from ursina import Entity, Text, Button, camera, color, mouse, application
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina import Ursina

app = Ursina()

from scenario_1_file import Scenario1
from scenario_2_file import Scenario2


# === Main Menu ===
class MainMenu(Entity):
    def __init__(self):
        super().__init__()
        self.menu_background = Entity(
            parent=camera.ui,
            model="quad",
            texture="main_texture.jpg",
            z=1,
        )
        self.title = Text(
            "RELATIVITY \n SIMULATOR",
            scale=4,
            y=0.3,
            origin=(0, 0),
            z=-1,
            parent=camera.ui,
            color=color.white,
        )

        self.text_box = Text(
            text="Click a scenario to begin. \nPress 'ESC' to return to this menu.",
            origin=(-0.5, 0),
            x=-0.5,
            y=-0.2,
            scale=0.8,
            z=-1,
            parent=camera.ui,
        )
        self.btn1 = Button(
            text="Scenario 1\nThe Terrell Rotation",
            scale=(0.3, 0.1),
            y=0.1,
            z=-1,
            parent=camera.ui,
            color=color.azure,
            highlight_color=color.light_gray,
            pressed_color=color.lime,
        )
        self.btn2 = Button(
            text="Scenario 2\nThe Doppler Effect",
            scale=(0.3, 0.1),
            y=-0.05,
            z=-1,
            parent=camera.ui,
            color=color.azure,
            highlight_color=color.light_gray,
            pressed_color=color.lime,
        )
        self.quit_btn = Button(
            text="Quit",
            scale=(0.3, 0.1),
            y=-0.2,
            z=-1,
            parent=camera.ui,
            color=color.azure,
            highlight_color=color.light_gray,
            pressed_color=color.lime,
        )

        self.btn1.on_click = lambda: load_scenario(Scenario1)
        self.btn2.on_click = lambda: load_scenario(Scenario2)
        self.quit_btn.on_click = application.quit

        self.menu_elements = [
            self.menu_background,
            self.title,
            self.btn1,
            self.btn2,
            self.quit_btn,
            self.text_box,
        ]

    def show(self):
        for element in self.menu_elements:
            element.enabled = True
            mouse.locked = False  # Ensure mouse is unlocked for menu interaction
            mouse.visible = True

    def hide(self):
        for element in self.menu_elements:
            element.enabled = False


# === Scenario management ===
current_scenario = None
main_menu = MainMenu()


def load_scenario(scenario_class):
    global current_scenario
    main_menu.hide()
    current_scenario = scenario_class(escape_callback=handle_escape)
    # Lock mouse for scenario interaction
    mouse.locked = True
    mouse.visible = False


def handle_escape():
    global current_scenario
    if current_scenario:
        unload_scenario(current_scenario)


def unload_scenario(scenario):
    global current_scenario
    if hasattr(scenario, "cleanup"):
        scenario.cleanup()
    current_scenario = None
    main_menu.show()
    # Unlock mouse for menu interaction
    mouse.locked = False
    mouse.visible = True


def input(key):
    if current_scenario and hasattr(current_scenario, "input"):
        current_scenario.input(key)


def update():
    if current_scenario:
        current_scenario.update()


# Create a global input handler
class InputHandler(Entity):
    def input(self, key):
        if current_scenario and hasattr(current_scenario, "input"):
            current_scenario.input(key)
    
    def update(self):
        if current_scenario:
            current_scenario.update()

# Create the input handler
input_handler = InputHandler()

app.run()
