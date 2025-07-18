# Relativity Simulator (Ursina)

This project is a 3D visual simulator of special relativity effects, built using the [Ursina Game Engine](https://www.ursinaengine.org/). It includes interactive scenarios demonstrating phenomena such as the **Terrell rotation** and the **relativistic Doppler effect**.

## Features

- **Scenario 1**: Terrell Rotation (apparent shape deformation of fast-moving objects)
- **Scenario 2**: Doppler Shift (color changes due to observer motion)
- Real-time 3D visualization with observer control
- Physically motivated calculations for apparent positions and wavelengths

## Requirements

- Python 3.8+
- [Ursina Engine](https://www.ursinaengine.org/)
- `colour-science` (for precise wavelength-to-RGB conversion)
- `numpy`

Install dependencies with:

```bash
pip install ursina colour-science numpy

