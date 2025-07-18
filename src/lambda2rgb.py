import colour
import numpy as np
import math


import math


def wavelength_to_rgb(wavelength):
    """
    Convert wavelength in nanometers to RGB values.
    Based on the visible light spectrum (380-780 nm).
    """
    # Clamp wavelength to visible range
    wavelength = max(380, min(780, wavelength))

    if wavelength < 440:
        # Violet to Blue
        r = -(wavelength - 440) / (440 - 380)
        g = 0.0
        b = 1.0
    elif wavelength < 490:
        # Blue to Cyan
        r = 0.0
        g = (wavelength - 440) / (490 - 440)
        b = 1.0
    elif wavelength < 510:
        # Cyan to Green
        r = 0.0
        g = 1.0
        b = -(wavelength - 510) / (510 - 490)
    elif wavelength < 580:
        # Green to Yellow
        r = (wavelength - 510) / (580 - 510)
        g = 1.0
        b = 0.0
    elif wavelength < 645:
        # Yellow to Orange
        r = 1.0
        g = -(wavelength - 645) / (645 - 580)
        b = 0.0
    else:
        # Orange to Red
        r = 1.0
        g = 0.0
        b = 0.0

    # Apply gamma correction and intensity falloff
    factor = 0.3
    if wavelength < 420:
        factor = 0.3 + 0.7 * (wavelength - 380) / (420 - 380)
    elif wavelength > 700:
        factor = 0.3 + 0.7 * (780 - wavelength) / (780 - 700)

    # Gamma correction
    gamma = 0.8
    r = math.pow(r * factor, gamma)
    g = math.pow(g * factor, gamma)
    b = math.pow(b * factor, gamma)

    return (r, g, b)


def wavelength_to_rgb_old(wavelength_nm):
    """
    Convert a wavelength in nm (380–780) to RGB using colour-science.
    Output: (r, g, b) integers in range 0–255 (sRGB, gamma-corrected)
    """

    if wavelength_nm < 380:
        wavelength_nm = 380
    elif wavelength_nm > 780:
        wavelength_nm = 780

    # Convert scalar wavelength to XYZ
    xyz = colour.wavelength_to_XYZ(wavelength_nm * 1.0)

    # Normalize XYZ
    xyz /= np.max(xyz) if np.max(xyz) > 0 else 1

    # Convert to sRGB
    rgb = colour.XYZ_to_sRGB(xyz)

    # Clamp, gamma correct, and scale to 0–255
    rgb = np.clip(rgb, 0, 1)
    rgb_int = tuple(int(round(c * 255)) for c in rgb)

    return rgb_int
