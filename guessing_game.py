class GuessingGame():
    def __init__(self, answer_numer):
        self.answer_number = answer_numer
        self.winner = False
    
    def guess(self, user_guess):
        if int(user_guess) > self.answer_number:
            return "high"
        elif int(user_guess) < self.answer_number:
            return "low"
        else:
            self.winner = True
            return "correct"
    
    def solved(self):
        if self.winner:
            return True
        return False

# game = GuessingGame(20)

# print(game.guess(20))
# print(game.solved())