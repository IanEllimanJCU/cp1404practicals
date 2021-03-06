"""
CP1404/CP5632 - Practical
Task 2
"""
import random


def main():
    score = float(input("Enter score: "))
    graded_score = grade_the_score(score)
    print(graded_score)
    random_score = random.randint(0, 100)
    random_graded_score = grade_the_score(random_score)
    print(f"Random {random_graded_score}")


def grade_the_score(score):
    if score < 0 or score > 100:
        graded_score = 'Score is invalid'
    elif score >= 90:
        graded_score = 'Score is excellent'
    elif score >= 50:
        graded_score = 'Score is pass'
    else:
        graded_score = 'Score is bad'
    return graded_score


main()
