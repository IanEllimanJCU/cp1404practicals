"""
CP1404/CP5632 - Practical
Task 2
"""
score = float(input("Enter score: "))
if score < 0 or score > 100:
    print('Score is invalid')
elif score >= 90:
    print('Score is excellent')
elif score >= 50:
    print('Score is pass')
else:
    print('Score is bad')
exit()