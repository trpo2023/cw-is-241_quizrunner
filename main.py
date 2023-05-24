#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from src.quiz import Quiz
from src.mainmenu import QuizrunnerApp

if __name__ == "__main__":
    app = QuizrunnerApp()
    app.run()
