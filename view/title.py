import tkinter as tk


class Title:

    def __init__(self):
        pass

    @staticmethod
    def insert_title(frame, controller, title: str):
        label = tk.Label(
            frame, text=title,
            font=controller.title_font,
            background=controller.background_color,
            fg=controller.font_color
        )
        label.pack(
            side=controller.title_side,
            fill=controller.title_side_fill,
            pady=controller.title_pady
        )
        return label
