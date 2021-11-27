import json
import tkinter as tk

from view.button import Button
from view.label import Label
from view.title import Title


class QuadroLideres(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)
        self.leaderboard = list()

        self.title = None
        self.players = list()
        self.space = None
        self.back = None

        self.read_leaderboard()

        self.fill_leaderboard()

    def clear(self):
        self.leaderboard = list()
        self.read_leaderboard()
        self.title.destroy()
        self.space.destroy()
        self.back.destroy()
        for player in self.players:
            player.destroy()
        self.fill_leaderboard()

    def read_leaderboard(self):
        with open('data/leaderboard.json', 'r') as f:
            self.leaderboard = json.load(f)

    def fill_leaderboard(self):
        self.title = Title.insert_title(self, self.controller, 'Quadro de Líderes')

        if len(self.leaderboard) > 0:
            self.leaderboard = sorted(self.leaderboard, key=lambda d: d['points'], reverse=True)
            for index, player in enumerate(self.leaderboard):
                if index < 10:
                    self.players.append(
                        Label.insert_label(self, self.controller, f'({player["points"]}) - {player["name"]}')
                    )
                else:
                    break
        else:
            self.players.append(Label.insert_label(self, self.controller, 'Nenhum jogador'))

        self.space = Label.insert_label(self, self.controller, '')

        self.back = Button.insert_button(self, self.controller, 'Voltar', 'MenuPrincipal')
