# Slot Machine Game

This simple Python program implements a basic slot machine game. Players can deposit an initial amount, place bets, and spin the virtual slot machine reels. The outcome of each spin determines whether the player wins or loses, affecting their balance accordingly.

## Table of Contents
- [Features](#features)
- [Usage](#usage)
- [Game Mechanics](#game-mechanics)
- [How to Play](#how-to-play)
- [Requirements](#requirements)
- [License](#license)

## Features

- **Deposit and Bet:** Players can deposit an initial amount and place bets for each round.
- **Random Slot Machine:** The slot machine generates random characters for each of the three lines.
- **Winning Logic:** The game checks for matching characters in rows and columns to determine if the player wins.
- **Balance Management:** The player's balance is updated based on the outcome of each round.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/slot-machine-game.git
   cd slot-machine-game
   ```
2. Run the game:
  
    ```bash
    python slot_machine.py
    ```
    Follow the on-screen instructions to deposit money, place bets, and spin the slot machine.

## Game Mechanics
The slot machine consists of three lines, each displaying three randomly chosen characters from the set "ABC." The game checks for matching characters in rows and columns to determine if the player wins. If a winning combination is found, the player's balance is increased by double the bet amount; otherwise, the balance is decreased by the bet amount.

## How to Play
- **Deposit Money:**
  Enter the amount you want to deposit when prompted. The amount must be greater than $0.

- **Place Bets:** 
  Enter your desired bet amount when prompted. The amount must be between $5 and $100.
  
- **Spin the Slot Machine:**
  Watch the slot machine reels spin and wait for the outcome.

- **Win or Lose:**
  If the characters align in a winning combination, you win and your balance is increased.
  If no winning combination is found, you lose, and your balance is decreased.

- **Repeat or Exit:**
  You can choose to place another bet and continue playing or exit the game.
  
## Requirements
Python 3.x

## License
This project is licensed under the MIT License.
