# Snake-Water-Gun-game

A simple command-line implementation of the classic Snake-Water-Gun game (similar to Rock-Paper-Scissors).

## Game Rules

The game follows these winning conditions:
- **Snake** beats **Water** (snake drinks water)
- **Water** beats **Gun** (water rusts gun)
- **Gun** beats **Snake** (gun shoots snake)

## How to Play

1. Run the script
2. Enter your choice when prompted:
   - `s` for Snake
   - `w` for Water
   - `g` for Gun
3. The computer makes a random choice
4. The game displays the result (win, lose, or draw)

## Code Overview

### Long Version
Uses explicit if-else conditions to check all possible winning/losing scenarios.

### Optimized Version
Uses mathematical logic:
- `(computer - you) == 0`: Draw
- `(computer - you) in (1, -2)`: Player wins
- Otherwise: Player loses

This works because each choice defeats exactly two other choices.

## Game Values

- Snake: `1`
- Water: `-1`
- Gun: `0`

## Requirements

- Python 3.x
- No external dependencies

## Usage

```bash
python solution.py

Example:

Enter your choice: s
you chose Snake
computer chose Water
You won!