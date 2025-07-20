# Usage Guide for Relativity Simulator

## How to Use the Scenarios

The scenarios are **functional** but start in a **paused state**. Here's how to use them:

### Scenario 1: Terrell Rotation

1. **Start the application**: `python run.py`
2. **Click "Scenario 1"** from the main menu
3. **Press SPACE** to start the simulation (it starts paused)
4. **Watch the cubes**: You'll see two cubes - white (real) and red (apparent)
5. **Move around**: Use WASD to move when paused, mouse to look around
6. **Focus camera**: Press R to rotate camera towards the red cube. 
7. **Press SPACE again** to pause/resume
8. **Press ESC** to return to main menu

### Scenario 2: Doppler Effect

1. **Click "Scenario 2"** from the main menu
2. **Press SPACE** to start the simulation
3. **Move around**: Use WASD to move, observe color changes
4. **Watch the spheres**: They change color based on relative motion
5. **Press SPACE** to pause/resume
6. **Press ESC** to return to main menu

### Controls Summary

- **SPACE**: Start/Pause simulation (scenarios start paused)
- **WASD**: Move observer (when paused in Scenario 1, always in Scenario 2)
- **Mouse**: Look around
- **ESC**: Return to main menu
- **R**: Reset camera (Scenario 1 only)

### What to Look For

**Scenario 1**: The white cube starts moving at $t=0$ as a rigid body. The observer will se the red (apparent) cube; each of its corners starts moving at different moments, due to the different distance to the observer, so the red cube appears rotated. This is the Terrell rotation.

**Scenario 2**: The spheres will change color as you move around, demonstrating the relativistic Doppler effect.

### Troubleshooting

If the scenarios appear "not functional":
1. **Press SPACE** - they start paused by design
2. **Move around** - use WASD and mouse to see the effects
3. **Check the text** - the UI shows the current state (Paused/Running)

The scenarios are working correctly - they just require user interaction to start the simulation! 