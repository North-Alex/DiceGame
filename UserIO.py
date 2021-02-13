class UserIO:
    def __init__(self):
        self.delimiter = " "
        
    def holdPrompt(self, dice_num):
        prompt_message = "Enter dice you want to keep " \
            "(for example, \"2{}5\")\n".format(self.delimiter)
        user_input = input(prompt_message)
        is_valid, error = self.validateInput(user_input, dice_num)
        if is_valid:
            return list(set(user_input.split(self.delimiter)))
        else:
            print(error)
            return self.holdPrompt(dice_num)
    
    def validateInput(self, user_input, dice_num):
        input_array = user_input.split(self.delimiter)
        if len(input_array) == 0:
            return False, "You must enter at least 1 die to hold"
        for die in input_array:
            try: die = int(die)
            except ValueError: return False, "Non-numeric input. " \
                "Please use numbers only"
            if die < 1 or die > dice_num:
                return False, "Please use numbers from 1 to " + str(dice_num)
        return True, ""
        
    def promptPlayerName(self, number, player_list, message = ""):
        user_input = input("Enter name for player {}: {}\n".format(number, message))
        for p in player_list:
            if p.name == user_input:
                return self.promptPlayerName(number, player_list, "('{}'" \
                    " name already exists)".format(p.name))
        if len(user_input) > 40 or len(user_input) < 2:
            return self.promptPlayerName(number, player_list, "(Please enter " \
                " a name that is between 2 and 40 characters long)")
        return user_input
        
    def promptStart(self):
        user_input = input("Enter 'start' to start the game, 'rules' " \
            "to see game rules or 'quit' to exit game.\n")
        return user_input
        
    def formatDice(self, dice):
        top_row = ""
        center_row = ""
        bottom_row = ""
        hint_row = ""
        hint_label = 1
        for d in dice:
            top_row += "___ "
            center_row += "|{}| ".format(d)
            bottom_row += "‾‾‾ "
            hint_row += "-{}- ".format(hint_label)
            hint_label += 1
        return "{}\n{}\n{}\n{}".format(
            top_row, center_row, bottom_row, hint_row
        )
        
    def gameResult(self, player_list):
        #not just sorting here by design as there can be multiple winners
        winners = []
        winning_score = -1
        for p in player_list:
            if winning_score < 0:
                winners.append(p)
                winning_score = p.score
            elif p.score == winning_score:
                winners.append(p)
            elif p.score < winning_score:
                winners = [p]
                winning_score = p.score
        
        if len(winners) > 1:
            print ("{} are the winners! Congratulations!".format(
                ", ".join((p.name) for p in winners)
            ))
        else:
            print("{} is the winner! Congratulations!".format(
                winners[0].name
            ))
            
    def formatStandings(self, player_list):
        rating = sorted(player_list, key=lambda pl: pl.score)
        print("Standings:\n")
        for player in rating:
            print("{}: {} points".format(player.name, player.score))