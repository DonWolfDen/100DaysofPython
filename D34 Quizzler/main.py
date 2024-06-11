from question_model import Question, Category
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
import random

# cat = Category().get_category(categories)

question_bank = []
for quest in question_data:
    question_bank.append(Question(quest["question"], quest["correct_answer"], quest["category"]))

print(question_bank)
random.shuffle(question_bank)
quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print(f"You've completed the quiz.\n"
#       f"Your final score is {quiz.score}/{quiz.question_num}")
