# Domineering

This is a domineering game with an AI, written in python 3.6.

## Contents

### README.md

This!

### domineering.py

The main program. Runs a game of Domineering. When run, it first asks the user for board height, then for the width, then asks which players (from domineering_AI.py) will be playing. A board is created with these dimensions, then the game is run until one of the players has no legal moves. This is the loser of the game. Player 1 ("L") uses a 2 x 1 vertical block, and player 2 ("R") uses a 1 x 2 horizontal block. Once a square is filled, it cannot be played in again.

### domineering_AI.py

Contains players and evaluation functions that can be used to play domineering. 

#### Players

The following are the list of players which are prompted for selection at the beginning of the domineering.py file:

##### 0: Human
When it is this player's turn, the program prompts the user for input, by first entering the row, and then the column. If using this option, keep in mind that the first player ("L") uses vertical blocks, the second player ("R") uses horizontal blocks, and that the indexing is done by the top (or left) half of the block. 

##### 1: Random
This player randomly selects a legal move and plays there.

##### 2: Minimax
When given a depth and evaluation function (see below), computes the minimax move up to that depth. If no 1st player strategy exists that will win the game by this depth, the evaluation function is used as a imperfect metric to compare the value of gamestates.

##### 3: Alphabeta
Improves on minimax by not visiting any more of the children of a node if its player can force a better result than can be acheived by visiting one of its sister nodes instead. This algorithm selects moves with the same probability distribution as *minimax*, but decreases the search space (see results).
See [Wikipedia article on Alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha–beta_pruning)

##### 4: Alpha-Beta with symmetry pruning
Improves further on the alpha-beta algorithm by pruning moves that are symmetric to another move. If the board is symmetric horizontally we can prune any moves that are on the right side of the board because it's mirror on the left side will produce a congruent game. Likewise, if the board is symmetric vertically we can prune moves that are on the bottom of the board. Finally, if the board is 180 degrees rotationally symmetric, we can prune the moves to the right side of the board. This improvement also selects moves with the same probability distribution as *minimax*.

##### 5: Sorted Alpha-Beta with symmetry pruning
Improves further on *Alpha-Beta with symmetry pruning* by visiting moves that are more likely better (measured by evaluation function) first. The effect of this is a higher likelihood that alphabeta pruning will occur. As with the previous algorithms, this algorithm selects moves with the same probability distribution as *minimax.*

##### A Note on the players
Because, as listed above, *Minimax,* *Alphabeta,* *Alpha-Beta with symmetry pruning,* and *Sorted Alpha-Beta with symmetry pruning* all select moves with the same probability distribution, to maximize performance, we should select the algorithm with the fastest performance (See results). *Alpha-Beta with symmetry pruning* and *Sorted Alpha-Beta with symmetry pruning* seem to complete at similar speeds for board sizes 5x5 and 6x6, and are faster than the other algorithms that produce the same result, so when looking for performance, one should choose one of these two. The other algorithms were included for the sole purpose of showing the progress of this project, but should generally not be used.

#### Evaluation Functions

##### Legal Moves

This simple evaluation function returns the difference between the number of the player's and the opponent's legal moves. 
For example, on the 2x4 board below, I ("R") have 6 legal moves that I can make, and my opponent has 4, so *Legal Moves* will return +2 as my score for this gamestate.

| |0|1|2|3|
|---|---|---|---|---|
|0| | | | |
|1| | | | |

##### Playability

*Playability* is another simple evaluation function. Simply, it returns the number of my pieces that I could fit on the board assuming I had unlimited back-to-back turns.
For example, on the board below, I ("R") can place 3 tiles, while my opponent can only play 2 tiles; thus, the *Playability* function will return a score of +1 for me.

| |0|1|2|3|
|---|---|---|---|---|
|0| | |x|x|
|1| | | | |