import tkinter as tk
from tkinter import font as tkfont

from controller.area_professor import AreaProfessor
from controller.adicionar_pergunta import AdicionarPergunta
from controller.game_master import GameMaster
from controller.jogar import Jogar
from controller.menu_principal import MenuPrincipal
from controller.quadro_lideres import QuadroLideres
from controller.questao import Questao
from controller.ver_perguntas import VerPerguntas


class QuizEducacional(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.game_master = GameMaster()

        self.title_font = tkfont.Font(family='Segoe UI', size=42)
        self.label_font = tkfont.Font(family='Segoe UI', size=16)
        self.button_font = tkfont.Font(family='Segoe UI', size=16)
        self.small_button_font = tkfont.Font(family='Segoe UI', size=12)
        self.field_font = tkfont.Font(family='Segoe UI', size=12)
        self.background_color: str = '#42b0f5'
        self.font_color: str = '#ffffff'
        self.title_pady: int = 10
        self.title_side: str = 'top'
        self.title_side_fill: str = 'x'
        self.button_pad: int = 12
        self.small_button_pad: int = 6
        self.button_width: int = 40
        self.entry_width: int = 46

        self.state('zoomed')

        container = tk.Frame(self, pady=32, padx=32)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.configure(background=self.background_color)

        self.frames = {}

        for F in (
            MenuPrincipal,
            Jogar,
            QuadroLideres,
            AreaProfessor,
            AdicionarPergunta,
            VerPerguntas,
            Questao
        ):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MenuPrincipal")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.clear()
        frame.tkraise()

    def clear(self):
        pass
