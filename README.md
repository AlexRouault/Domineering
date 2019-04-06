# Domineering

This is a domineering game with an AI, written in python 3.6.

## Contents:

### README.md

This!

### domineering.py

The main program. Runs a game of Domineering. When run, it first asks the user for board height, then for the width, then asks which players (from domineering_AI.py) will be playing. A board is created with these dimensions, then the game is run until one of the players has no legal moves. This is the loser of the game. Player 1 ("L") uses a 2 x 1 vertical block, and player 2 ("R") uses a 1 x 2 horizontal block. Once a square is filled, it cannot be played in again.

### domineering_AI.py

Contains AI's that can be used to play domineering.