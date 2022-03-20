from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text=f"SCORE: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="Questions",
                                                     width=280,
                                                     font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.t_button = Button(image=self.true_img, highlightthickness=0, command=self.is_true)
        self.t_button.grid(row=2, column=0)

        self.false_img = PhotoImage(file="images/false.png")
        self.f_button = Button(image=self.false_img, highlightthickness=0, command=self.is_false)
        self.f_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"SCORE: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You completed the Quiz!")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def is_true(self):
        right = self.quiz.check_answer("True")
        self.feedback(right)

    def is_false(self):
        right = self.quiz.check_answer("False")
        self.feedback(right)

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


