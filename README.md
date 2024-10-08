### Author: BENEDICT KARIUKI
### Date: September 17, 2024
### Version: 1.0

## Table of Contents
- [Description](#description)
- [How to Play](#how-to-play)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

## Description
This project implements the classic **Cows and Bulls** game using Python. The game generates a random 4-digit number (with no duplicate digits) and asks the user to guess it. After each guess, the program provides feedback in the form of "bulls" and "cows":
- **Bulls**: A correct digit in the correct position.
- **Cows**: A correct digit in the wrong position.

The user is given a limited number of attempts to guess the number.

## How to Play
1. A random 4-digit number is generated by the program. The digits are unique.
2. The player tries to guess the number within a set number of tries.
3. After each guess, the program will tell you:
   - How many **bulls** (correct digits in the correct positions).
   - How many **cows** (correct digits in the wrong positions).
4. The goal is to get 4 bulls to win the game.

## Requirements
- Python 3.x

## Setup and Installation
1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/benedictkariuki/cows-and-bulls.git
