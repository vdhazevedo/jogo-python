class Question:

    def __init__(self, question, correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3, points):
        self.question: str = question
        self.correct_answer: str = correct_answer
        self.wrong_answer_1: str = wrong_answer_1
        self.wrong_answer_2: str = wrong_answer_2
        self.wrong_answer_3: str = wrong_answer_3
        self.points: str = points
