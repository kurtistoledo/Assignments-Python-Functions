# Lesson 5: Python Functions
# 4. The Quiz Game

def ask_question(question, correct_answer):
    user_answer = input(f"{question} ").lower()
    return user_answer == correct_answer.lower()

def main():
    questions = [
        ("What is the chemical symbol for water?", "H2O"),
        ("Which river is the longest in the world?", "Nile"),
        ("Who wrote the play \"Romeo and Juliet\"?", "William Shakespeare"),
        ("What year did World War II end?", "1945")
    ]

    score = 0
    total_questions = len(questions)

    print("Welcome to the Quiz Game!")
    print("NOTE: If your spelling is incorrect, it is considered a wrong answer.")

    for i, (question, correct_answer) in enumerate(questions, start=1):
        if ask_question(f"\n{i}. {question}", correct_answer):
            print("Correct! You got 1 point.")
            score += 1
        else:
            print("Incorrect!")
            print(f"Current answer is --> {correct_answer}")

    print(f"\nNumber of questions: {total_questions}")
    print(f"Your score: {score}/{total_questions}")

    try:
        percentage = (score * 100) / total_questions
    except ZeroDivisionError:
        percentage = 0

    print(f"{percentage:.2f}% questions are correct.")

if __name__ == "__main__":
    main()
