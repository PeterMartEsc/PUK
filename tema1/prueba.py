import random

class Partida():
    board = []
    turn = None
    
    def __init__(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        self.turn = bool(random.randint(0,1))

    def alternate_turn(self):
        self.turn = not self.turn 
    
    def play_turn():
        