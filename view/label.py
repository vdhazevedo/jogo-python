import tkinter as tk


class Label:

    def __init__(self):
        pass

    @staticmethod
    def insert_label(frame, controller, text: str):
        label = tk.Label(
            frame,
            text=text,
            font=controller.label_font,
            background=controller.background_color,
            fg=controller.font_color
        )
        label.pack()
        return label
