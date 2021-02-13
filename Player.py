class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
    
    def addScore(self, score):
        self.score += score