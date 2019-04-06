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
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        print("\n  ", end="")
        for c in range(self.w):
            print(c%10, end="")
        print('\n +', '-'*self.w, '+', sep = '')
        for r in range(len(self.vals)):
            print(r, '|', sep='', end='')
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
    players = [("human_play", human_play), ("random_play", random_play), ("greedy_play", greedy_play),
               ("greedy_opp_d2_play", greedy_opp_d2_play), ("greedy_opp_d3_play", greedy_opp_d3_play),
               ("greedy_opp_d4_play", greedy_opp_d4_play), ("greedy_play2", greedy_play2)]
    print("Players:")
    for i in range(len(players)):
        print(i, players[i][0])
    L = players[int(input("Enter index of L-player: "))][1]
    R = players[int(input("Enter index of R-player: "))][1]
    return L, R

def game():
    h = int(input("Enter board height: "))
    w = int(input("Enter board width: "))
    L, R = get_players()
    board = Board(h,w)
    board.show()
    while True:
        # L turn
        if not possible_plays(board, 1): # L has no plays: game over
            print("R wins!")
            break
        while not board.play(L(board)): # Repeat until legal move
            pass
        board.show()
        # R turn
        if not possible_plays(board, 0): # R has no plays: game over
            print("L wins!")
            break
        while not board.play(R(board)): # Repeat until legal move
            pass
        board.show()

game()
