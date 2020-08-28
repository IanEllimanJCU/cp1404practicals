"""
CP1404/CP5632 - Practical
Task 1
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >=0:
    if sales >= 1000:
        bonus_multiplier = 0.15
    else:
        bonus_multiplier = 0.10
    bonus = bonus_multiplier * sales
    print(f'Bonus is ${bonus:.2f}')
    sales = float(input("Enter sales: $"))
exit()