import tkinter as tk

from view.button import Button
from view.title import Title


class AreaProfessor(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)

        Title.insert_title(self, self.controller, 'Área do Professor')

        Button.insert_button(self, self.controller, 'Adicionar Pergunta', 'AdicionarPergunta')
        Button.insert_button(self, self.controller, 'Ver Perguntas', 'VerPerguntas')
        Button.insert_button(self, self.controller, 'Voltar', 'MenuPrincipal')

    def clear(self):
        pass
