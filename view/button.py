import tkinter as tk


class Button:

    def __init__(self):
        pass

    @staticmethod
    def insert_button(frame, controller, text: str, frame_name: str, overridden_command=False) -> tk.Button:
        if overridden_command:
            button = tk.Button(
                frame, text=text,
                command=lambda: frame.overridden_command(),
                font=controller.button_font,
                background=controller.font_color,
                pady=controller.small_button_pad,
                padx=controller.small_button_pad,
                width=controller.button_width
            )
            button.pack()
            return button
        else:
            button = tk.Button(
                frame, text=text,
                command=lambda: controller.show_frame(frame_name),
                font=controller.button_font,
                background=controller.font_color,
                pady=controller.small_button_pad,
                padx=controller.small_button_pad,
                width=controller.button_width
            )
            button.pack()
            return button
