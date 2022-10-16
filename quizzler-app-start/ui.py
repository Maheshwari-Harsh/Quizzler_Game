from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Label for window
        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125, text="Some Question Text",
                                                     font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        # Buttons
        self.right_button = Button()
        right_img = PhotoImage(file="images/true.png")
        self.right_button.config(image=right_img, highlightthickness=0, command=self.true_checked)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button()
        wrong_img = PhotoImage(file="images/false.png")
        self.wrong_button.config(image=wrong_img, highlightthickness=0, command=self.false_checked)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_checked(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_checked(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
