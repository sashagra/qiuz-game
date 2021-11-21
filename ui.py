from tkinter import Tk, Label, Canvas, Button, PhotoImage
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
RED_COLOR = "#ee665d"
GREEN_COLOR = "#29b677"


class QiuzUi:
    '''Class of quiz UI'''

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg='white')
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250,  bg='white')
        self.question_text = self.canvas.create_text(
            300 / 2,
            250 / 2,
            width=280,
            text="Some textsome test some text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file='./images/true.png')
        false_image = PhotoImage(file='./images/false.png')

        self.true_button = Button(
            image=true_image,
            text="True",
            command=self.true_pressed,
            highlightthickness=0
        )
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(
            image=false_image,
            text="false",
            command=self.false_pressed,
            highlightthickness=0
        )
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        '''Next q'''
        self.canvas.config(bg='white')
        self.disable_buttons(False)
        q_text = self.quiz.next_question()
        if q_text:
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Game over')
            self.disable_buttons(True)

    def true_pressed(self):
        '''true answer process'''
        self._process_answer(True)

    def false_pressed(self):
        '''false answer process'''
        self._process_answer(False)

    def _process_answer(self, answer: bool):
        '''check the anwser'''
        is_right_anwser, score = self.quiz.check_answer(answer)
        if is_right_anwser:
            self.score_label.config(text=f"Score: {score}")
            self.canvas.config(bg=GREEN_COLOR)
        else:
            self.canvas.config(bg=RED_COLOR)
        self.disable_buttons(True)

        self.window.after(1000, self.get_next_question)

    def disable_buttons(self, state: bool):
        '''Enable/disable buttons'''
        if state:
            self.true_button["state"] = "disabled"
            self.false_button["state"] = "disabled"
        else:
            self.true_button["state"] = "normal"
            self.false_button["state"] = "normal"
