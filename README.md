# Relativity Simulator (Ursina)

This project is a 3D visual simulator of special relativity effects, built using the [Ursina Game Engine](https://www.ursinaengine.org/). It includes interactive scenarios demonstrating phenomena such as the **Terrell rotation** and the **relativistic Doppler effect**.

## Features

- **Scenario 1**: Terrell Rotation (apparent shape deformation of fast-moving objects)
- **Scenario 2**: Doppler Shift (color changes due to observer motion)
- Real-time 3D visualization with observer control
- Physically motivated calculations for apparent positions and wavelengths

## Installation

### Option 1: Using pip (Recommended)

```bash
# Install dependencies
pip install -r requirements.txt
```

### Option 2: Manual installation

```bash
# Install required packages
pip install ursina numpy
```

## Running the Application

### Option 1: Using the launcher script (Recommended)

```bash
python run.py
```

### Option 2: Running from src directory

```bash
cd src
python main.py
```

## Controls

- **WASD**: Move observer (when simulation is paused)
- **Mouse**: Look around
- **SPACE**: Start/Pause simulation
- **ESC**: Return to main menu
- **R**: Reset camera orientation

## Scenarios

### Scenario 1: Terrell Rotation
Watch a cube appear to rotate as it moves at relativistic speeds. This demonstrates how the finite speed of light affects the apparent shape of moving objects.

### Scenario 2: Doppler Effect
Observe how the color of spheres changes based on their relative motion, demonstrating the relativistic Doppler effect.

## Requirements

- Python 3.8+
- [Ursina Engine](https://www.ursinaengine.org/)
- `numpy`

## Troubleshooting

If you encounter import errors, make sure you're running the application from the project root directory using `python run.py`.

