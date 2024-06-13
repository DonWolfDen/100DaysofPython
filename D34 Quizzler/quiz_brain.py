import html

class QuizBrain:

    def __init__(self, bank):
        self.question_num = 0
        self.questions_list = bank
        self.score = 0


    def still_has_questions(self):
        return self.question_num < len(self.questions_list)

    def next_question(self):
        self.current_q = self.questions_list[self.question_num]
        self.question_num += 1
        q_text = html.unescape(self.current_q.text)
        return f"Q.{self.question_num}: {q_text} (True/False): "
        # user_answer = input(f"Q.{self.question_num}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_q.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct")
            return True
        else:
            print("Incorrect")
            print(f"The correct answer is {correct_answer}\n")
            return False
