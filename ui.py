import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizUIInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.answer = None
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250)
        self.config = self.canvas.config(bg='white', highlightthickness=0)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text="Some Question here",
                                                     font=('Arial',20,'italic'))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.right_icon = PhotoImage(file="images/true.png")
        self.wrong_icon = PhotoImage(file="images/false.png")
        self.right_button = Button(image=self.right_icon, highlightthickness=0, command=lambda: self.determine_answer("True"))
        self.wrong_button = Button(image=self.wrong_icon, highlightthickness=0, command=lambda: self.determine_answer("False"))
        self.right_button.grid(row=2,column=0)
        self.wrong_button.grid(row=2,column=1)

        self.label_score = Label()
        self.label_score.config(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.label_score.grid(row=0,column=1)
        self.game_over_label = Label()
        self.game_over_label.config(text='', fg='white', bg=THEME_COLOR)
        self.game_over_label.grid(row=0,column=0)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        if self.quiz.still_has_questions():
            quest_next = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quest_next)
            self.canvas.config(bg='white', highlightthickness=0)
        else:
            self.game_over_label.config(text=f'Quizz Over, your final score is {self.quiz.score}', fg='white', bg=THEME_COLOR)


    def determine_answer(self,answer):
        self.answer = self.quiz.check_answer(answer)
        if self.answer:
            self.canvas.config(bg='green', highlightthickness=0)
            self.label_score.config(text=f"Score: {self.quiz.score}", fg='white', bg=THEME_COLOR)
        else:
            self.canvas.config(bg='red', highlightthickness=0)
        self.window.after(1000, self.next_question)



