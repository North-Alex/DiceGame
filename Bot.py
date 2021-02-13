import random
from GameConfig import GameConfig

class Bot:
    def __init__(self, stupidity = random.randint(0, 100)):
        self.stupidity = stupidity
        self.intellectual_threshold = 70
    
    def pickDice(self, dice):
        pick = []
        #in case if bot is smart enough to pick no die on a bad throw
        #it'll pick the smallest die number of them all
        smallest = {"pos": 0, "number": GameConfig().DIE_SIZE + 1}
        tolerance = GameConfig().DIE_SIZE * self.stupidity / 100
        if tolerance == 0:
            tolerance += 0.1
        
        for i in range(len(dice)):
            #seriously stupid bot doesn't know about zeroes
            if self.stupidity < self.intellectual_threshold:
                if dice[i] in GameConfig().ZERO_DICE:
                    dice[i] = 0
            if dice[i] < smallest["number"]:
                smallest["pos"] = i
                smallest["number"] = dice[i]
            if dice[i] < tolerance:
                pick.append(i+1)
        if len(pick) == 0:
            pick.append(smallest["pos"]+1)
        return pick