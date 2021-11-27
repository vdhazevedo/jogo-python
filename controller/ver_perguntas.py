import json
import tkinter as tk
from tkinter import END, messagebox

from view.button import Button
from view.delete_button import DeleteButton
from view.label import Label
from view.title import Title


class VerPerguntas(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background=self.controller.background_color)
        self.questions = list()
        self.listbox = tk.Listbox(self, width=80)

        Title.insert_title(self, self.controller, 'Ver Perguntas')

        self.get_questions()

        Label.insert_label(self, self.controller, 'Role a lista para ver mais')

        DeleteButton.insert_delete_button(self, self.controller)
        Button.insert_button(self, self.controller, 'Voltar', 'AreaProfessor')

    def clear(self):
        self.get_questions()

    def read_questions(self):
        with open('data/questions.json', 'r') as f:
            self.questions = json.load(f)

    def delete(self):
        selected_item = self.listbox.get(self.listbox.curselection())

        for question in self.questions:
            if question['question'] == selected_item:
                self.questions.remove(question)

        with open('data/questions.json', 'w') as f:
            json.dump(self.questions, f)

        self.get_questions()

        messagebox.showinfo('Sucesso', 'Pergunta apagada com sucesso!')

    def get_questions(self):
        self.listbox.delete(0, END)
        self.read_questions()

        for index, question in enumerate(self.questions):
            self.listbox.insert(index, question['question'])

        self.listbox.pack()
