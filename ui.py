import time
from tkinter import *


from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scoreboard = Label(text="Score:0", fg="white", bg=THEME_COLOR)
        self.scoreboard.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas_text = self.canvas.create_text(150,
                                                   125,
                                                   width=280,
                                                   text="Something text for canvas",
                                                   font=("arial", 16, "italic"),
                                                   fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.button_false = Button(image=false_image, highlightthickness=0, command=self.callback_false)
        self.button_false.grid(row=2, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.button_true = Button(image=true_image, highlightthickness=0, command=self.callback_true)
        self.button_true.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.scoreboard.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You`ve reached the end of the quiz.")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def callback_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def callback_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

