from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = self.quiz.score

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"SCORE:{self.score}", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Questions",
                                                     width=280,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.button = Button(image=self.true_img, highlightthickness=0, command=self.is_true)
        self.button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.button = Button(image=self.false_img, highlightthickness=0, command=self.is_false)
        self.button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def is_true(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def is_false(self):
        self.quiz.check_answer("False")
        self.get_next_question()

