from html import unescape
from question_model import Question


class QuizBrain:
    '''Class of quiz'''

    def __init__(self, q_list: list[Question]):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[0]

    def next_question(self) -> str:
        '''Asks next quesion'''
        try:
            self.current_question = self.question_list[self.question_number]
        except IndexError:
            return ""
        self.question_number += 1
        try:
            q_text = unescape(self.current_question.text)
        except IndexError:
            return ""
        return f"Q.{self.question_number}: {q_text}"

    def check_answer(self, user_answer: bool) -> tuple[bool, int]:
        '''Checks is right answer'''
        correct_answer = self.current_question.answer
        if user_answer == correct_answer:
            self.score += 1
            return True, self.score
        else:
            return False, self.score

        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
