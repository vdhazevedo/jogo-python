class GameMaster:

    def __init__(self):
        self.player = None
        self.points = 0
        self.answered_questions = list()
        self.game_over = False

    def add_points(self, points):
        self.points = self.points + points

    def reset_game(self):
        self.answered_questions = list()
        self.game_over = False
        self.points = 0
