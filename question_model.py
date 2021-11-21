class Question:
    '''Definition of question object'''

    def __init__(self, q_text: str, q_answer: str):
        self.text = q_text
        self.answer: bool = False if q_answer.lower() == 'false' else True
