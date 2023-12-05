
INITIAL_SCORE = 0

class UserStatistics:

    def __init__(self):
        self.score = INITIAL_SCORE
        self.basic_clues = 0
        self.bonus_clues = 0

    def increase_score(self, difficulty):
        self.score += difficulty.get_score()
    