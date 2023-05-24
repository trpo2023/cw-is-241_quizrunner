import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END
from src.testresults import TestResults
from tkinter import messagebox as mb


class TestRunner:
    def __init__(self, quiz):
        # build ui
        print(quiz.quiz_name)
        self.quiz = quiz
        self.TestRunner = tk.Toplevel()
        self.TestRunner.configure(height=200, width=200)
        self.TestRunner.title("Quiz Running")
        label23 = ttk.Label(self.TestRunner)
        label23.configure(font="TkDefaultFont")
        label23.grid(column=0, row=0, sticky="w")
        self.qtext = tk.Text(self.TestRunner)
        self.qtext.configure(
            exportselection="true",
            height=16,
            state="disabled",
            takefocus=True,
            undo="false",
            width=100,
        )
        self.qtext.grid(column=0, columnspan=2, padx=16, pady=16, row=0)
        frame7 = ttk.Frame(self.TestRunner)
        frame7.configure(height=200, width=200)
        labelframe5 = ttk.Labelframe(frame7)
        labelframe5.configure(height=200, text="Navigation", width=200)
        self.prev = ttk.Button(labelframe5)
        self.prev.configure(text="<= Previous")
        self.prev.grid(column=0, columnspan=1, padx=8, pady=8, row=0, rowspan=3)
        self.prev.configure(command=self.go_prev)
        self.next = ttk.Button(labelframe5)
        self.next.configure(text="Next =>")
        self.next.grid(column=3, columnspan=1, padx=8, pady=8, row=0, rowspan=3)
        self.next.configure(command=self.go_next)
        self.ans_a = ttk.Radiobutton(labelframe5)
        self.ans = tk.IntVar(value=0)
        self.ans_a.configure(text="Answer A)", value=0, variable=self.ans)
        self.ans_a.grid(column=1, row=0)
        self.ans_a.configure(command=self.set_answer)
        self.ans_b = ttk.Radiobutton(labelframe5)
        self.ans_b.configure(text="Answer B)", value=1, variable=self.ans)
        self.ans_b.grid(column=2, row=0)
        self.ans_b.configure(command=self.set_answer)
        self.ans_c = ttk.Radiobutton(labelframe5)
        self.ans_c.configure(text="Answer C)", value=2, variable=self.ans)
        self.ans_c.grid(column=1, row=1)
        self.ans_c.configure(command=self.set_answer)
        self.ans_d = ttk.Radiobutton(labelframe5)
        self.ans_d.configure(text="Answer D)", value=3, variable=self.ans)
        self.ans_d.grid(column=2, row=1)
        self.ans_d.configure(command=self.set_answer)
        self.ans_clr = ttk.Radiobutton(labelframe5)
        self.ans_clr.configure(
            style="TButton", text="Clear selection", value=-1, variable=self.ans
        )
        self.ans_clr.grid(column=1, columnspan=2, row=2)
        self.ans_clr.configure(command=self.set_answer)
        labelframe5.grid(column=1, row=0)
        labelframe6 = ttk.Labelframe(frame7)
        labelframe6.configure(height=200, text="Time Left", width=200)
        self.timeleft_txt = tk.Label(labelframe6)
        self.timeleft_txt.configure(text="00:00")
        self.timeleft_txt.pack(side="top")
        self.timeleft_bar = ttk.Progressbar(labelframe6)
        self.timeleft_bar.configure(orient="horizontal")
        self.timeleft_bar.pack(side="top")
        labelframe6.grid(column=0, ipadx=16, ipady=6, padx=16, pady=0, row=0)
        labelframe11 = ttk.Labelframe(frame7)
        labelframe11.configure(height=200, text="QuizRunner", width=200)
        self.end = ttk.Button(labelframe11)
        self.end.configure(text="End Test")
        self.end.pack(expand="true", side="top")
        self.end.configure(command=self.endtest)
        labelframe11.grid(column=2, ipady=12, padx=12, row=0)
        frame7.grid(column=0, columnspan=2, row=1)
        # Main widget
        self.mainwindow = self.TestRunner
        self.current_q_index = 0
        self.givenanswers = []
        self.timeleft = self.quiz.time_limit
        self.timeleft_bar.configure(value=100)
        self.givenanswers = [-1 for i in range(len(quiz.question_list))]
        self.print_q_text()
        self.clock()

    def clock(self):
        self.timeleft_bar.configure(value=self.timeleft / self.quiz.time_limit * 100)
        self.timeleft_txt.configure(
            text="%02d:%02d" % (self.timeleft / 60, self.timeleft % 60)
        )
        self.timeleft -= 1
        if self.timeleft == -1:
            self.endtest()
        else:
            self.timeleft_txt.after(1000, self.clock)

    def print_q_text(self):
        self.qtext.configure(state="normal")
        self.qtext.delete(1.0, tk.END)
        self.qtext.insert(
            END,
            "Question %s/%s.\n\n"
            % (str(self.current_q_index + 1), len(self.quiz.question_list)),
        )
        self.qtext.insert(END, self.quiz.question_list[self.current_q_index] + "\n\n")
        self.qtext.insert(
            END,
            "A) %s\nB) %s\nC) %s\nD) %s\n"
            % (
                self.quiz.answer_list[self.current_q_index][0],
                self.quiz.answer_list[self.current_q_index][1],
                self.quiz.answer_list[self.current_q_index][2],
                self.quiz.answer_list[self.current_q_index][3],
            ),
        )
        self.qtext.configure(state="disabled")
        self.ans.set(self.givenanswers[self.current_q_index])

    def run(self):
        self.mainwindow.mainloop()

    def go_prev(self):
        if self.current_q_index != 0:
            self.current_q_index -= 1
            self.print_q_text()

    def go_next(self):
        if self.current_q_index + 1 != len(self.quiz.question_list):
            self.current_q_index += 1
            self.print_q_text()

    def set_answer(self):
        self.givenanswers[self.current_q_index] = self.ans.get()

    def endtest(self):
        if self.timeleft <= 0 or mb.askyesno(
            title="Confirmation", message="Are you sure you want to end the test?"
        ):
            for a in self.givenanswers:
                a = self.quiz.answer_list[self.current_q_index][a]
            TestResults(self.quiz, self.givenanswers, self.timeleft)
            self.TestRunner.destroy()
