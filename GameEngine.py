import random, time
from UserIO import UserIO
from GameConfig import GameConfig
from Player import Player
from Bot import Bot

class GameEngine:
    def __init__(self):
        print("Welcome to Dice")
        self.start()
        
    def start(self, command = ""):
        if command == "start":
            self.playGame();
        elif command == "rules":
            print("""
                === Welcome to Dice ===
                In this game of four players you take turns and 
                roll {d_num} dice. Then you hold at least 1 die and re-roll
                until all dice are held. Then all players take their turns
                rolling. Every die held counts as its face value. {zero_arr}
                die throws are counted as 0 points. The player with the 
                lowest score wins the game.
                To play with a bot, start player's name with 'BOT', like 
                'BOTZILLA' or "BOT 2547".
            """.format(
                d_num = GameConfig().DICE_NUMBER, 
                zero_arr = GameConfig().ZERO_DICE)
            )
            self.start(UserIO().promptStart())
        elif command == "quit":
            quit()
        else:
            self.start(UserIO().promptStart())
        
    def playGame(self):
        player_list = []
        for i in range(GameConfig().PLAYER_NUMBER):
            player_list.append(
                Player(UserIO().promptPlayerName(i + 1, player_list))
            )
        for round in range(GameConfig().ROUNDS):
            self.playRound(round, player_list)
            #first player starts last next round
            player_list = player_list[1:] + [player_list[0]]
            
    def playRound(self, round_idx, player_list):
        print("\nStarting round {}. " \
            "Starting with {}.\n".format(round_idx + 1, player_list[0].name))
        for p in player_list:
            print("=== {}'s turn ===".format(p.name))
            player_selection = self.playTurn(p.name, []) 
            #print("you scored {}".format(scoreDice(player_selection)))
            p.addScore(self.scoreDice(player_selection))
        print("\nRound {} finished\n".format(round_idx+1))
        print ("Standings:")
        for p in player_list:
            print("{}: {} points".format(p.name, p.score))
            
            
    def playTurn(self, player, dice_selected = []):
        if len(dice_selected) == 5:
            return dice_selected
        roll = []
        for i in range(GameConfig().DICE_NUMBER-len(dice_selected)):
            roll.append(random.randint(1, GameConfig().DIE_SIZE))
        print(UserIO().formatDice(roll))
        if player[0:3] == "BOT":
            dice_hold_idx = Bot().pickDice(roll)
            time.sleep(1.5)
            print("\n === {}: I select {}\n".format(player, dice_hold_idx))
        else:
            max_dice = GameConfig().DICE_NUMBER-len(dice_selected)
            dice_hold_idx = UserIO().holdPrompt(max_dice)
        dice_hold = [roll[int(d) - 1] for d in dice_hold_idx]
        dice_selected += dice_hold
        return self.playTurn(player, dice_selected)
        
    def scoreDice(self, dice):
        sum = 0
        for d in dice:
            if d not in GameConfig().ZERO_DICE:
                sum += d
        return sum