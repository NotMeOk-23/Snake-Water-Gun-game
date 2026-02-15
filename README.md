# Snake-Water-Gun-game

A simple implementation of the classic Snake-Water-Gun game (similar to Rock-Paper-Scissors) in Python. Now available in both CLI and GUI versions!

## Game Rules

The game follows these winning conditions:
- **Snake** beats **Water** (snake drinks water)
- **Water** beats **Gun** (water rusts gun)
- **Gun** beats **Snake** (gun shoots snake)

## How to Play (GUI Version)

This version features an interactive graphical user interface with animations.

1. Run the GUI script:
   ```bash
   python gui_game.py
   ```
2. Click on the buttons (Snake, Water, Gun) to make your choice.
3. The game will display the result with animations:
   - **Win**: Watch the yellow balloon fly!
   - **Lose**: Receive a hopeful quote.

## How to Play (CLI Version)

1. Run the script:
   ```bash
   python snake_water_gun.py
   ```
2. Enter your choice when prompted:
   - `s` for Snake
   - `w` for Water
   - `g` for Gun
3. The computer makes a random choice
4. The game displays the result (win, lose, or draw)

## Code Overview

- `snake_water_gun.py`: Contains the core game logic and the CLI implementation.
- `gui_game.py`: Contains the GUI implementation using `tkinter`, importing logic from `snake_water_gun.py`.

### Logic
The game uses mathematical logic or conditional checks to determine the winner:
- Snake: `1`
- Water: `-1`
- Gun: `0`

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)

## Usage

CLI:
```bash
python snake_water_gun.py
```

GUI:
```bash
python gui_game.py
```
