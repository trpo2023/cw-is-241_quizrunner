
import tkinter as tk
import tkinter.ttk as ttk

class TestResults:
    def __init__(self, quiz, givenanswers, timeleft):
        # build ui
        timeelapsed = quiz.time_limit - timeleft
        i = 0
        right = 0
        for q in quiz.correct_answer_list:
            #print("%s ? %s", givenanswers[i], quiz.correct_answer_list[i])
            if givenanswers[i] != -1\
                or quiz.answer_list[givenanswers[i]] == quiz.correct_answer_list[i]:
                right += 1
            i+=1
        self.TestResults = tk.Toplevel()
        self.TestResults.configure(height=200, width=200)
        self.TestResults.title("Results")
        labelframe13 = ttk.Labelframe(self.TestResults)
        labelframe13.configure(
            height=200,
            takefocus=True,
            text='Test Results',
            width=500)
        label38 = ttk.Label(labelframe13)
        label38.configure(justify="left", text='Score:')
        label38.grid(column=0, row=1, sticky="e")
        self.score = ttk.Label(labelframe13)
        self.score.configure(text=' %s/%s' % (right, i))
        self.score.grid(column=1, row=1, sticky="w")
        label40 = ttk.Label(labelframe13)
        label40.configure(text='Time elapsed:')
        label40.grid(column=0, row=2, sticky="e")
        label41 = ttk.Label(labelframe13)
        label41.grid(column=1, row=2)
        self.time = ttk.Label(labelframe13)
        self.time.configure(text=' %02d:%02d' % (timeelapsed/60, timeelapsed%60))
        self.time.grid(column=1, row=2, sticky="w")
        label43 = ttk.Label(labelframe13)
        label43.grid(column=0, row=3, sticky="e")
        label44 = ttk.Label(labelframe13)
        label44.grid(column=1, row=3, sticky="w")
        self.done = ttk.Button(labelframe13)
        self.done.configure(text='Done', width=16)
        
        self.done.grid(column=0, columnspan=2, pady=8, row=5)
        self.done.configure(command=self.okdone)
        self.testname = ttk.Label(labelframe13)
        self.testname.configure(font="TkHeadingFont", text=quiz.quiz_name)
        self.testname.grid(column=0, columnspan=2, padx=12, pady=12, row=0)
        labelframe13.pack(side="top")

    def okdone(self):
        self.TestResults.destroy()