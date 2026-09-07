# MINI QUIZ APP
# Questions are kept separately in questions.py

import random
from questions import questions


# Shows the question and its options
def show_question(question, question_number):

    print("\n----------------------------------------")
    print("Question", question_number, "of", len(questions))
    print("Category:", question["category"])
    print("----------------------------------------")

    print(question["question"])

    for option in question["options"]:
        print(option)


# Takes the answer from the user
def get_answer():

    answer = input("\nYour answer: ").upper()

    # Ask again if the input is not A, B, C or D
    while answer not in ["A", "B", "C", "D"]:
        print("Please enter A, B, C or D.")
        answer = input("Your answer: ").upper()

    return answer


# Shows the final score
def show_result(score):

    total_questions = len(questions)
    percentage = (score / total_questions) * 100

    print("\n========================================")
    print("             QUIZ COMPLETED")
    print("========================================")

    print("Final Score:", score, "/", total_questions)
    print("Percentage:", round(percentage, 2), "%")

    # Show a message according to the score
    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good!")
    elif percentage >= 40:
        print("Performance: Needs Improvement.")
    else:
        print("Performance: Keep Practicing!")


# Starts and runs the quiz
def start_quiz():

    score = 0

    # Make a copy before shuffling the questions
    quiz_questions = questions.copy()

    # Show questions in a random order
    random.shuffle(quiz_questions)

    print("========================================")
    print("             MINI QUIZ APP")
    print("========================================")
    print("Total Questions:", len(quiz_questions))
    print("Categories: Python, DBMS, Computer Fundamentals")
    print("Questions are displayed in random order.")

    # Go through all the questions one by one
    for question_number, question in enumerate(quiz_questions, start=1):

        show_question(question, question_number)

        # Get the user's answer
        user_answer = get_answer()

        # Check the answer
        if user_answer == question["answer"]:

            score = score + 1

            print("Correct!")
            print("Score:", score, "/", question_number)

        else:

            print("Wrong!")
            print("Correct Answer:", question["answer"])
            print("Score:", score, "/", question_number)

    # Show the final result
    show_result(score)


# Run the quiz
start_quiz()