import tkinter as tk


class DeleteButton:

    def __init__(self):
        pass

    @staticmethod
    def insert_delete_button(frame, controller) -> tk.Button:
        button = tk.Button(
            frame, text='Apagar selecionada',
            command=lambda: frame.delete(),
            font=controller.button_font,
            background=controller.font_color,
            pady=controller.small_button_pad,
            padx=controller.small_button_pad,
            width=controller.button_width
        )
        button.pack()
        return button
