import copy
from domineering_AI import *

class Board:

    def __init__(self, height, width):
        self.w = width
        self.h = height
        self.vals = []
        for i in range(height):
            self.vals.append(["."]*width)
        self.turn = 1 # 0=R="-"; 1=L="|"

    def copy(self):
        return copy.deepcopy(self)

    def show(self):        
        print("\n  ", end="")
        for c in range(self.w):
            print(c%10, end="")
        print('\n +', '-'*self.w, '+', sep = '')
        for r in range(len(self.vals)):
            print(r%10, '|', sep='', end='')
            for val in self.vals[r]:
                print(val, end='')
            print('|')
        print(' +', '-'*self.w, '+\n', sep = '')


    def play(self, pos):
        # Returns true if successful
        r = pos[0]
        c = pos[1]
        try:
            if self.turn: # L
                if self.vals[r][c] == '.' and self.vals[r+1][c] == '.':
                    self.vals[r][c] = '#'
                    self.vals[r+1][c] = '#'
                else:
                    print("Attempted play at [", r, ", ", c, "] is not a legal move for L!", sep = "")
                    return False
            else: # R
                if self.vals[r][c] == '.' and self.vals[r][c+1] == '.':
                    self.vals[r][c] = 'x'
                    self.vals[r][c+1] = 'x'
                else:
                    print("Attempted play at [", r, ", ", c, "] is not a legal move for R!", sep = "")
                    return False
        except:
            print("Attempted play at [", r, ", ", c, "] is not a legal move!", sep = "")
            return False
        self.turn = not self.turn
        return True

def get_players():
    players = [("human_play", human_play), ("random_play", random_play), ("minimax", minimax), ("alphabeta", alphabeta)]
    non_metered = (human_play, random_play) # players that don't have an evaluation function or depth
    eval_fns = [("greedy_score", greedy_score), ("greedy_score2", greedy_score2)]
    
    print("Players:")
    for i in range(len(players)):
        print(i, players[i][0])
    print("Evaluation functions:")
    for i in range(len(eval_fns)):
        print(i, eval_fns[i][0])
        
    # Get L player
    L = players[int(input("Enter index of L-player: "))][1]
    if L in non_metered:
        L_eval_fn = None
        L_depth = None
    else:
        L_eval_fn = eval_fns[int(input("Enter evaluation function for L: "))][1]
        L_depth = int(input("Maximum depth before evaluation metric is applied for L: "))

    # Get R player
    R = players[int(input("Enter index of R-player: "))][1]
    if R in non_metered:
        R_eval_fn = None
        R_depth = None
    else:
        R_eval_fn = eval_fns[int(input("Enter evaluation function for R: "))][1]
        R_depth = int(input("Maximum depth before evaluation metric is applied for R: "))
    
    return L, L_eval_fn, L_depth, R, R_eval_fn, R_depth

def game():
    h = int(input("Enter board height: "))
    w = int(input("Enter board width: "))
    L, Le, Ld, R, Re, Rd = get_players()
    board = Board(h,w)
    board.show()
    while True:
        # L turn
        if not possible_plays(board, 1): # L has no plays: game over
            print("R wins!")
            break
        while not board.play(L(board, Ld, Le)): # Repeat until legal move
            pass
        board.show()
        # R turn
        if not possible_plays(board, 0): # R has no plays: game over
            print("L wins!")
            break
        while not board.play(R(board, Rd, Re)): # Repeat until legal move
            pass
        board.show()

game()
