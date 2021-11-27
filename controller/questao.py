import json
import tkinter as tk
import random
from tkinter import messagebox

from model.player import Player
from view.button import Button
from view.label import Label
from view.option_1_button import Option1Button
from view.option_2_button import Option2Button
from view.option_3_button import Option3Button
from view.option_4_button import Option4Button
from view.title import Title


class Questao(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)
        self.questions = list()
        self.leaderboard = list()
        self.selected_question = None

        self.title = None
        self.question = None
        self.question_space_1 = None
        self.question_space_2 = None
        self.option_1 = None
        self.option_2 = None
        self.option_3 = None
        self.option_4 = None
        self.back = None

        self.fill_question()

    def clear(self):
        if self.selected_question is not None:
            self.title.destroy()
            self.question.destroy()
            self.question_space_1.destroy()
            self.question_space_2.destroy()
            self.option_1.destroy()
            self.option_2.destroy()
            self.option_3.destroy()
            self.option_4.destroy()
            self.back.destroy()
            self.fill_question()

    def read_questions(self):
        with open('data/questions.json', 'r') as f:
            self.questions = json.load(f)

    @staticmethod
    def get_options(question) -> list:
        options = list()
        options.append(question['correct_answer'])
        options.append(question['wrong_answer_1'])
        options.append(question['wrong_answer_2'])
        options.append(question['wrong_answer_3'])
        random.shuffle(options)

        return options

    def fill_question(self):
        self.read_questions()

        for answered_question in self.controller.game_master.answered_questions:
            self.questions[:] = [d for d in self.questions if d.get('question') != answered_question]

        if len(self.questions) == 1:
            self.questions.append(self.questions[0])

        if len(self.questions) > 0:
            random.shuffle(self.questions)
            self.selected_question = self.questions.pop()
            self.title = Title.insert_title(self, self.controller, f'Pontos: {self.controller.game_master.points}')
            self.question = Label.insert_label(self, self.controller, self.selected_question['question'])
            self.question_space_1 = Label.insert_label(self, self.controller, '')

            options = self.get_options(self.selected_question)

            self.option_1 = Option1Button.insert_option_1_button(self, self.controller, options[0])
            self.option_2 = Option2Button.insert_option_2_button(self, self.controller, options[1])
            self.option_3 = Option3Button.insert_option_3_button(self, self.controller, options[2])
            self.option_4 = Option4Button.insert_option_4_button(self, self.controller, options[3])

            self.question_space_2 = Label.insert_label(self, self.controller, '')

            self.back = Button.insert_button(self, self.controller, 'Voltar', 'MenuPrincipal')
        else:
            self.controller.game_master.game_over = True

    def select_option_1(self):
        self.show_result(self.option_1['text'])

    def select_option_2(self):

        self.show_result(self.option_2['text'])

    def select_option_3(self):
        self.show_result(self.option_3['text'])

    def select_option_4(self):
        self.show_result(self.option_4['text'])

    def show_result(self, option):
        if self.selected_question['correct_answer'] == option:
            tk.messagebox.showinfo('Resultado', 'Resposta correta!')
            self.controller.game_master.add_points(int(self.selected_question['points']))
        else:
            tk.messagebox.showerror('Resultado', 'Resposta incorreta!')
        self.controller.game_master.answered_questions.append(self.selected_question['question'])
        if not self.controller.game_master.game_over:
            self.controller.show_frame('Questao')
        if len(self.questions) > 0 and not self.controller.game_master.game_over:
            self.controller.show_frame('Questao')
        else:
            with open('data/leaderboard.json', 'r') as f:
                self.leaderboard = json.load(f)

            new_player = Player(self.controller.game_master.player, self.controller.game_master.points)
            self.leaderboard.append(new_player.__dict__)

            with open('data/leaderboard.json', 'w') as f:
                json.dump(self.leaderboard, f)

            self.controller.show_frame('QuadroLideres')
