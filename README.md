# Lab 8: Pygame Project

A simple pygame game featuring bouncing cats and interactive game mechanics.

## Project Overview

This project demonstrates core pygame concepts including:
- Loading and scaling images
- Creating multiple sprite instances from a single image
- Managing game state and velocity
- Event handling (keyboard and mouse input)
- Collision detection
- Rendering graphics to the screen

## Features

- **Multiple Sprites**: Load one image and display 10 independent animated cats
- **Bouncing Animation**: Cats bounce between screen boundaries
- **Game Loop**: Proper game loop structure with FPS control
- **Event Handling**: Respond to user input (quit events)

## Installation

### Prerequisites
- Python 3.10+
- pip (Python package manager)

### Setup

1. Navigate to the project directory:
```bash
cd lab8-pygame
```

2. Activate the virtual environment:
```bash
# On Windows
.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Project

```bash
python main.py
```

The game window will open and display 10 animated cats bouncing horizontally across the screen.

## Project Structure

```
lab8-pygame/
├── main.py                 # Main game file
├── graphics/              # Image assets
│   └── cat.png           # Cat sprite image
├── requirements.txt        # Project dependencies
├── README.md              # This file
└── .venv/                 # Virtual environment (auto-generated)
```

## Key Concepts Demonstrated

### Velocity Lists
Each cat has an associated velocity stored in a parallel list:
```python
cat_velocities = [4] * 10  # 10 cats, each with velocity 4
```

Using `enumerate()` matches each cat's position with its velocity:
```python
for i, cat_rect in enumerate(cat_list):
    cat_rect.x += cat_velocities[i]
```

### Collision and Boundary Detection
Cats reverse direction when hitting screen edges:
```python
if cat_rect.left <= 0:
    cat_velocities[i] = 4      # Bounce right
if cat_rect.right >= 1200:
    cat_velocities[i] = -4     # Bounce left
```

## Controls

- **Close Window**: Click the X button to exit the game

## Future Enhancements

- Add interactive elements (click to affect cats)
- Scoring system
- Different animation speeds for different cats
- Collision between cats
- Sound effects

## Dependencies

- **pygame**: Game development library for Python

See `requirements.txt` for specific versions.

## Notes

- Game runs at 60 FPS (frames per second)
- Uses `convert_alpha()` for optimized alpha blending
- Screen resolution: 1200x600 pixels
