import tkinter as tk


class SaveButton:

    def __init__(self):
        pass

    @staticmethod
    def insert_save_button(frame, controller) -> tk.Button:
        button = tk.Button(
            frame, text='Salvar',
            command=lambda: frame.save(),
            font=controller.button_font,
            background=controller.font_color,
            pady=controller.small_button_pad,
            padx=controller.small_button_pad,
            width=controller.button_width
        )
        button.pack()
        return button
