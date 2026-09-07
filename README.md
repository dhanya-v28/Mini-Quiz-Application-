# Mini Quiz App

A simple **command-line Mini Quiz App** built using Python. It allows users to answer multiple-choice questions and get their final score and performance.

## Features

* 15 multiple-choice questions
* Questions from Python, DBMS, and Computer Fundamentals
* Display questions one at a time
* Accept answers using A, B, C, or D
* Show the correct answer for a wrong response
* Keep track of the score
* Calculate final percentage
* Display a performance message
* Randomize the order of questions
* Handle invalid answer input

## Approach

* Questions are stored separately in `questions.py` using a **list of dictionaries**.
* Each question contains the **question, options, correct answer, and category**.
* `quiz.py` imports the questions and contains the main quiz logic.
* A copy of the questions list is created using `copy()` so the original list is not changed.
* `random.shuffle()` is used to display the questions in a **random order**.
* A `for` loop with `enumerate()` displays the questions one by one with their question number.
* A separate function takes the user's answer and checks whether it is a valid option (`A`, `B`, `C`, or `D`).
* The user's answer is compared with the correct answer stored in the question dictionary.
* The score is increased by 1 for every correct answer.
* If the answer is wrong, the correct option is displayed.
* After all questions are completed, the final score and percentage are calculated.
* An `if-elif-else` structure displays a performance message based on the percentage.

## Concepts Used

* Variables
* Input/Output
* Conditions
* `for` and `while` loops
* Lists
* Dictionaries
* Functions
* Modules
* Input validation
* `random.shuffle()`
* `enumerate()`

## How to Run

Make sure Python is installed.

Open the terminal in the project folder and run:

```bash
python quiz.py
```

## Note

This is a command-line based project developed as part of the college Technical Society task of Programming Domain.
