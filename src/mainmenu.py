import tkinter as tk
import tkinter.ttk as ttk
from src.testpreview import *
from .quiz import *
from tkinter import filedialog as fd

class QuizrunnerApp:
    def __init__(self, master=None):
        # build ui
        self.MainMenu = tk.Tk() 
        self.MainMenu.configure(height=200, width=200)
        self.MainMenu.title("The Ultimate Quizrunner ")
        label1 = ttk.Label(self.MainMenu)
        label1.configure(
            compound="left",
            cursor="boat",
            font="TkDefaultFont",
            justify="center",
            state="normal",
            takefocus=False,
            text='QuizRunner\n\nMade by V. Dmitryuk\nA. Ivanov')
        label1.pack(padx=10, pady=10, side="top")
        self.main_run = ttk.Button(self.MainMenu)
        self.main_run.configure(text='Run test')
        self.main_run.pack(expand="true", fill="x", padx=6, side="top")
        self.main_run.configure(command=self.run_test)
        self.main_new = ttk.Button(self.MainMenu)
        self.main_new.configure(text='New test')
        self.main_new.pack(
            expand="false",
            fill="x",
            padx=6,
            pady=3,
            side="top")
        self.main_new.configure(command=self.create_test)

        # Main widget
        self.mainwindow = self.MainMenu

    def run(self):
        self.mainwindow.mainloop()

    def run_test(self):
        fname = fd.askopenfilename()
        f = open(fname)
        quiz = Quiz.from_json(f)
        settingsWindow = TestPreview(quiz)

    def create_test(self):
        pass