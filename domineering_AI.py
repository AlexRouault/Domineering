import random
import math

# # # AI's # # #
# All return play [r,c]

def human_play(board):
    r = input("It is your turn to make a play!\nRow: ")
    c = input("Column: ")
    return [int(r), int(c)]

def random_play(board):
    # random player
    return random.choice(possible_plays(board, board.turn))


def greedy_play(board):
    # plays to maximize greedy_score
    max_score = -math.inf
    max_play = None
    for option in possible_plays(board, board.turn):
        new_board = board.copy()
        new_board.play(option)
        new_score = greedy_score(new_board, board.turn)
        if new_score > max_score:
            max_score = new_score
            max_play = option
    return max_play

def greedy_opp_d2_play(board):
    # plays to maximize greedy_score after opponent reacts to play using minimax
    # (depth 2 minimax using greedy_score)
    return minimax(board, board.turn, 2, greedy_score)

def greedy_opp_d3_play(board):
    # plays to maximize greedy_score after opponent reacts to play using minimax
    # (depth 2 minimax using greedy_score)
    return minimax(board, board.turn, 3, greedy_score)

def greedy_opp_d4_play(board):
    # plays to maximize greedy_score after opponent reacts to play using minimax
    # (depth 2 minimax using greedy_score)
    return minimax(board, board.turn, 4, greedy_score)

def greedy_play2(board):
    # plays to maximize greedy_score2
    max_score = -math.inf
    max_play = None
    for option in possible_plays(board, board.turn):
        new_board = board.copy()
        new_board.play(option)
        new_score = greedy_score2(new_board, board.turn)
        if new_score > max_score:
            max_score = new_score
            max_play = option
    return max_play
    

# # # HELPER FUNCTIONS # # #

def possible_plays(board, player):
    # given board and player 0 (R) or 1 (L)
    # returns a list of coordinates [r,c] of row-column pairs indicating the location of a possible play for player
    plays = []
    if player == 0: # R
        for r in range(board.h): # All rows
            for c in range(board.w - 1): # All columns except last
                if board.vals[r][c] == '.' and board.vals[r][c+1] == '.':
                    plays.append([r,c])
    else: # L
        for r in range(board.h - 1): # All rows except last
            for c in range(board.w): # All columns
                if board.vals[r][c] == '.' and board.vals[r+1][c] == '.':
                    plays.append([r,c])
    return plays
    
def greedy_score(board, player):
    # spaces only I can play - spaces only opponent can play
    return len(possible_plays(board, player)) - len(possible_plays(board, not player))

def greedy_score2(board, player):
    # number of my pieces that can be fit on the board - opponent
    a = 0 # number of horizontal pieces that can be fit on the board
    for r in range(board.h):
        c = 0
        while c < board.w - 1:
            if board.vals[r][c] == '.':
                if board.vals[r][c+1] == '.':
                    a += 1
                c += 2
            else:
                c += 1
    b = 0 # number of vertical pieces that can fit on the board
    for c in range(board.w):
        r = 0
        while r < board.h - 1:
            if board.vals[r][c] == '.':
                if board.vals[r+1][c] == '.':
                    b += 1
                r += 2
            else:
                r += 1
    if player == 0:
        return a - b
    else:
        return b - a
    

def minimax(board, player, max_depth, eval_fn):
    # First layer of minimax (maximizes)
    # Returns best PLAY
    max_score = -math.inf
    max_play = None
    for pp in possible_plays(board, board.turn):
        new_board = board.copy()
        new_board.play(pp)
        new_score = mini(new_board, player, max_depth-1, eval_fn)
        if new_score >= max_score:
            max_score = new_score
            max_play = pp
    return max_play

def mini(board, player, max_depth, eval_fn):
    # Even layers of minimax (opponent's turn)
    # Returns worst SCORE opponent can force
    if max_depth == 0: # At max_depth -> return my evaluated score on current board
        return eval_fn(board, player)
    else:
        min_score = math.inf
        for pp in possible_plays(board, board.turn):
            new_board = board.copy()
            new_board.play(pp)
            new_score = maxi(new_board, player, max_depth-1, eval_fn)
            if new_score < min_score:
                min_score = new_score
        return min_score
    
def maxi(board, player, max_depth, eval_fn):
    # Odd layers of minimax (my turn)
    # Returns best SCORE I can force
    if max_depth == 0: # At max_depth -> return my evaluated score on current board
        return eval_fn(board, player)
    else:
        max_score = -math.inf
        for pp in possible_plays(board, board.turn):
            new_board = board.copy()
            new_board.play(pp)
            new_score = mini(new_board, player, max_depth-1, eval_fn)
            if new_score > max_score:
                max_score = new_score
        return max_score
