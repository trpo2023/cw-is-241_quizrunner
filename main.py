#!/usr/bin/python3
import pathlib
import pygubu
from tkinter import filedialog as fd

PROJECT_PATH = pathlib.Path(__file__).parent
PROJECT_UI = PROJECT_PATH / "quizrunner.ui"


class QuizrunnerApp:
    def __init__(self, master=None):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)
        # Main widget
        self.mainwindow = builder.get_object("MainMenu", master)
        builder.connect_callbacks(self)

    def run(self):
        self.mainwindow.mainloop()

    def run_test(self):
        filename = fd.askopenfilename()
        
    def create_test(self):
        pass


if __name__ == "__main__":
    app = QuizrunnerApp()
    app.run()
