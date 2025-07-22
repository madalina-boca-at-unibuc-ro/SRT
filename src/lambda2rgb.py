import numpy as np
import math


def wavelength_to_rgb(wavelength):
    """Convert a wavelength in nm to an RGB color value.
    Wavelength should be between 380 and 780 nm."""
    if wavelength < 380 or wavelength > 780:
        return (0, 0, 0)

    if wavelength < 395:
        R = 0.41 - 0.41 * (395 - wavelength) / 15
        G = 0.0
        B = 0.8 + 0.6 * (395 - wavelength) / 15
    if wavelength < 410:
        R = 0.41 * (410 - wavelength) / 30
        G = 0.0
        B = 0.8 + 0.6 * (410 - wavelength) / 30
    elif wavelength < 440:
        R = 0.19 - 0.19 * (440 - wavelength) / 30
        G = 0.0
        B = 1.0
    elif wavelength < 490:
        R = 0.0
        G = 1.0 - (490 - wavelength) / 50
        B = 1
    elif wavelength < 510:
        R = 0.0
        G = 1.0
        B = (510 - wavelength) / 20
    elif wavelength < 580:
        R = 1.0 - (580 - wavelength) / 70
        G = 1.0
        B = 0.0
    elif wavelength < 640:
        R = 1.0
        G = (640 - wavelength) / 60
        B = 0.0
    elif wavelength < 700:
        R = 1.0
        G = 0.0
        B = 0.0
    elif wavelength < 780:
        R = 1.0 + (700 - wavelength) / 80
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B)


def wavelength_to_rgb_cie(wavelength):
    """Convert a wavelength in nm to an RGB color value.
    Wavelength should be between 380 and 780 nm."""
    if wavelength < 380 or wavelength > 780:
        return (0, 0, 0)

    if wavelength < 410:
        R = 0.6 - 0.41 * (410 - wavelength) / 30
        G = 0.0
        B = 0.39 + 0.6 * (410 - wavelength) / 30
    elif wavelength < 440:
        R = 0.19 - 0.19 * (440 - wavelength) / 30
        G = 0.0
        B = 1.0
    elif wavelength < 490:
        R = 0.0
        G = 1.0 - (490 - wavelength) / 50
        B = 1
    elif wavelength < 510:
        R = 0.0
        G = 1.0
        B = (510 - wavelength) / 20
    elif wavelength < 580:
        R = 1.0 - (580 - wavelength) / 70
        G = 1.0
        B = 0.0
    elif wavelength < 640:
        R = 1.0
        G = (640 - wavelength) / 60
        B = 0.0
    elif wavelength < 700:
        R = 1.0
        G = 0.0
        B = 0.0
    elif wavelength < 780:
        R = 0.35 - 0.65 * (780 - wavelength) / 80
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    return (R, G, B)
