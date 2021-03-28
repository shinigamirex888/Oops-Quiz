from question_structure import Question
from data import question_data
from implement import QuizBrain

question_bank=[]
for x in question_data:
    question_text=x["text"]
    question_answer=x["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")



