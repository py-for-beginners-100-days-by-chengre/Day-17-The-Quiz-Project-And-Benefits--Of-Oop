from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
    question_b = Question(question_text=question['question'], question_answer=question['correct_answer'])
    question_bank.append(question_b)




quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()