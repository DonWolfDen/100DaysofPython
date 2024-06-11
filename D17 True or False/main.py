from question_model import Question, Category
from data import categories, question_data
from quiz_brain import QuizBrain
import random

print("True or False Quiz\n")

cat = Category().get_category(categories)
question_bank = []
for i in question_data[cat]:
    question_bank.append(Question(i["question"], i["correct_answer"]))
random.shuffle(question_bank)
quiz = QuizBrain(question_bank)

print("\nType T for true or F for false then hit enter\n")
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz.\n"
      f"Your final score is {quiz.score}/{quiz.question_num}")
