class QuizBrain:

    def __init__(self, bank):
        self.question_num = 0
        self.questions_list = bank
        self.score = 0

    def still_has_questions(self):
        return self.question_num < len(self.questions_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        print(f"The correct answer is {correct_answer}")
        print(f"Score: {self.score}/{self.question_num}\n")

    def next_question(self):
        current_q = self.questions_list[self.question_num]
        self.question_num += 1
        # print(f"Category: {current_q.category}")
        user_answer = input(f"Q.{self.question_num}: {current_q.text} (T/F): ")
        self.check_answer(user_answer, current_q.answer)
