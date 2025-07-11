# Higher or Lower: Instagram Edition
- A command-line game where you guess who has more Instagram followers between two randomly selected celebrities, influencers, or brands.
- Inspired by the classic Higher or Lower game, this version uses a custom dataset of public figures and entities.

## Features
- Clean command-line interface with ASCII art
- Dynamic comparison between random pairs of personalities
- Real Instagram follower data for realism
- Tracks and displays current score
- Input validation and user-friendly prompts

## Tech Stack
- Python 3.X
- Standard library: `random`

## How to Play
1. Two Instagram accounts are shown.
2. You guess which one has more followers by typing A or B.
3. If you are right, your score increases and you continue playing.
4. The game ends when your guess is incorrect.

## Setup and Installation

### 1. Clone the repository:
```bash
git clone https://github.com/rampalliprakhar/Higher-or-Lower-Instagram-Edition.git
cd higher-or-lower
```

### 2. Run the game:
```bash
python main.py
```

### 3. Sample Gameplay
```bash
Compare A: Cristiano Ronaldo, a Footballer, from Portugal
vs
Against B: Selena Gomez, a Musician and actress, from United States
Who has more followers? Type 'A' or 'B': a

You're right! Current score: 1

Compare A: Cristiano Ronaldo, a Footballer, from Portugal
vs
Against B: Beyoncé, a Musician, from United States
Who has more followers? Type 'A' or 'B': b

Wrong. Final score: 1
```

### 4. Project Structure
```bash
higher-or-lower/
├── art.py         # ASCII logos for the game and VS symbol
├── main.py        # Game logic and main loop
└── game_data.py   # List of Instagram accounts and follower data
```
