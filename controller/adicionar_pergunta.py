import json
import tkinter as tk
from tkinter import messagebox

from model.question import Question
from view.button import Button
from view.entry import Entry
from view.label import Label
from view.save_button import SaveButton
from view.title import Title


class AdicionarPergunta(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)
        self.entries = list()
        self.questions = list()

        self.read_questions()

        Title.insert_title(self, self.controller, 'Adicionar Pergunta')

        Label.insert_label(self, self.controller, 'Pergunta')
        entry = Entry()
        entry.insert_entry(self, self.controller)
        self.entries.append(entry)

        Label.insert_label(self, self.controller, 'Resposta Certa')
        entry = Entry()
        entry.insert_entry(self, self.controller)
        self.entries.append(entry)

        Label.insert_label(self, self.controller, 'Resposta Errada 1')
        entry = Entry()
        entry.insert_entry(self, self.controller)
        self.entries.append(entry)

        Label.insert_label(self, self.controller, 'Resposta Errada 2')
        entry = Entry()
        entry.insert_entry(self, self.controller)
        self.entries.append(entry)

        Label.insert_label(self, self.controller, 'Resposta Errada 3')
        entry = Entry()
        entry.insert_entry(self, self.controller)
        self.entries.append(entry)

        Label.insert_label(self, self.controller, 'Pontuação')
        entry = Entry()
        entry.insert_entry(self, self.controller)
        self.entries.append(entry)

        Label.insert_label(self, self.controller, '')

        SaveButton.insert_save_button(self, self.controller)
        Button.insert_button(self, self.controller, 'Voltar', 'AreaProfessor')

    def save(self) -> None:
        question: str = self.entries[0].entry.get()
        correct_answer: str = self.entries[1].entry.get()
        wrong_answer_1: str = self.entries[2].entry.get()
        wrong_answer_2: str = self.entries[3].entry.get()
        wrong_answer_3: str = self.entries[4].entry.get()
        points: str = self.entries[5].entry.get()

        question_obj = Question(question, correct_answer, wrong_answer_1, wrong_answer_2, wrong_answer_3, points)
        self.questions.append(question_obj.__dict__)
        self.write_questions()

    def read_questions(self):
        with open('data/questions.json', 'r') as f:
            self.questions = json.load(f)

    def write_questions(self):
        with open('data/questions.json', 'w') as f:
            json.dump(self.questions, f)

        self.controller.show_frame('AreaProfessor')

        messagebox.showinfo('Sucesso', 'Pergunta adicionada com sucesso!')

    def clear(self):
        self.read_questions()
        for entry in self.entries:
            entry.clear_text()
