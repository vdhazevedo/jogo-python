import tkinter as tk


class Entry:

    def __init__(self):
        self.entry = None

    def insert_entry(self, frame, controller):
        self.entry = tk.Entry(
            frame,
            width=controller.entry_width,
            font=controller.field_font
        )
        self.entry.pack()

    def clear_text(self):
        self.entry.delete(0, 'end')
