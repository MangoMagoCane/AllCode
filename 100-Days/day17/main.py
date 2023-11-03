from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

def main():
    question_bank = []
    for quest in question_data:
        new_question = Question(quest["text"], quest["answer"])
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    while quiz.still_has_questions():
        quiz.next_question()

    print("You've completed the quiz")
    print(f"Your final score is {quiz.score}/{quiz.amount_of_questions}")




if __name__ == "__main__":
    main()