import tkinter as tk
import tkinter.ttk as ttk
from src.testrunner import TestRunner


class TestPreview:
    def __init__(self, quiz):
        # build ui
        qcount = len(quiz.question_list)
        time = quiz.time_limit
        testname = quiz.quiz_name
        self.savedquiz = quiz
        self.TestPreview = tk.Toplevel()
        self.TestPreview.configure(height=200, width=200)
        labelframe3 = ttk.Labelframe(self.TestPreview)
        labelframe3.configure(height=200, text="Run this test?", width=500)
        label5 = ttk.Label(labelframe3)
        label5.configure(justify="left", text="Number of questions:")
        label5.grid(column=0, row=1, sticky="e")
        self.pre_numqs = ttk.Label(labelframe3)
        self.pre_numqs.configure(text=" " + str(qcount))
        self.pre_numqs.grid(column=1, row=1, sticky="w")
        label8 = ttk.Label(labelframe3)
        label8.configure(text="Time provided:")
        label8.grid(column=0, row=2, sticky="e")
        label9 = ttk.Label(labelframe3)
        label9.grid(column=1, row=2)
        self.pre_time = ttk.Label(labelframe3)
        self.pre_time.configure(text=" %d:%d" % (time / 60, time % 60))
        self.pre_time.grid(column=1, row=2, sticky="w")
        label14 = ttk.Label(labelframe3)
        label14.configure(text="Avg. per question:")
        label14.grid(column=0, row=3, sticky="e")
        self.pre_perq = ttk.Label(labelframe3)
        self.pre_perq.configure(
            text=" %d:%d" % (time / qcount / 60, time / qcount % 60)
        )
        self.pre_perq.grid(column=1, row=3, sticky="w")
        self.pre_cancel = ttk.Button(labelframe3)
        self.pre_cancel.configure(text="Cancel", width=16)
        self.pre_cancel.grid(column=0, columnspan=5, pady=4, row=6)
        self.pre_cancel.configure(command=self.pwcancel)
        self.pre_run = ttk.Button(labelframe3)
        self.pre_run.configure(text="Run", width=16)
        self.pre_run.grid(column=0, columnspan=2, row=5)
        self.pre_run.configure(command=self.pwok)
        self.pre_name = ttk.Label(labelframe3)
        self.pre_name.configure(font="TkHeadingFont", text=testname)
        self.pre_name.grid(column=0, columnspan=2, padx=12, pady=12, row=0)
        labelframe3.grid()

    def pwcancel(self):
        self.TestPreview.destroy()

    def pwok(self):
        trwindow = TestRunner(self.savedquiz)
        self.TestPreview.destroy()
