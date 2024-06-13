from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=40, padx=40, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}",
            bg=THEME_COLOR, fg="white",
            font=("Ariel", 30, "normal"),
            width=14
        )
        self.score_label.grid(column=1, row=0)

        self.category = Canvas(height=150, width=300, bg=THEME_COLOR, highlightthickness=0)
        self.category_text = self.category.create_text(
            150,
            75,
            text=f"\n ",
            font=("Ariel", 30, "normal"),
            width=300,
            fill="white"
        )
        self.category.grid(column=0, row=0)

        self.canvas = Canvas(bg="white", width=600, height=500)
        self.question_text = self.canvas.create_text(
            300,
            250,
            text="Sample text",
            font=("Ariel", 30, "italic"),
            width=560
        )
        self.canvas.grid(columnspan=2, column=0, row=1, pady=50)

        check = PhotoImage(file="images/true.png")
        self.true = Button(image=check, highlightthickness=0, command=self.check_true)
        self.true.grid(column=1, row=2)

        cross = PhotoImage(file="images/false.png")
        self.false = Button(image=cross, highlightthickness=0, command=self.check_false)
        self.false.grid(column=0, row=2)

        self.get_next_q()

        self.window.mainloop()

    def get_next_q(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.category.itemconfig(self.category_text, text=f"{self.quiz.current_q.category}")
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"You answered {self.quiz.score} out of "
                                        f"{len(self.quiz.questions_list)} questions correctly")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def check_true(self):
        self.feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right:bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(2000, self.get_next_q)



