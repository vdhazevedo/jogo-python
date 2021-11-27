import tkinter as tk

from view.button import Button
from view.title import Title


class MenuPrincipal(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)

        Title.insert_title(self, self.controller, 'Quiz Educacional')

        Button.insert_button(self, self.controller, 'Jogar', 'Jogar')
        Button.insert_button(self, self.controller, 'Quadro de Líderes', 'QuadroLideres')
        Button.insert_button(self, self.controller, 'Área do Professor', 'AreaProfessor')

    def clear(self):
        pass
