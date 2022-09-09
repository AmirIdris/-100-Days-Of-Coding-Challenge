from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for qe in question_data:
    question = qe['question']
    answer = qe['correct_answer']
    q = Question(question, answer)
    question_bank.append(q)
quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_qustion()

