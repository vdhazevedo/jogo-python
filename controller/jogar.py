import tkinter as tk

from view.button import Button
from view.entry import Entry
from view.label import Label
from view.title import Title


class Jogar(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)
        self.nickname = None
        self.entry = Entry()

        Title.insert_title(self, self.controller, 'Jogar')

        Label.insert_label(self, self.controller, 'Digite o seu nickname')

        self.entry.insert_entry(self, self.controller)

        Label.insert_label(self, self.controller, '')

        Button.insert_button(self, self.controller, 'Iniciar Jogo', '', True)
        Button.insert_button(self, self.controller, 'Voltar', 'MenuPrincipal')

    def clear(self):
        self.entry.clear_text()

    def overridden_command(self):
        self.nickname = self.entry.entry.get()
        self.controller.game_master.reset_game()
        self.controller.game_master.player = self.nickname
        self.controller.show_frame('Questao')
