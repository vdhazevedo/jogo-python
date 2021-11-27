import tkinter as tk


class Option2Button:

    def __init__(self):
        pass

    @staticmethod
    def insert_option_2_button(frame, controller, text) -> tk.Button:
        button = tk.Button(
            frame, text=text,
            command=lambda: frame.select_option_2(),
            font=controller.button_font,
            background=controller.font_color,
            pady=controller.small_button_pad,
            padx=controller.small_button_pad,
            width=controller.button_width
        )
        button.pack()
        return button
