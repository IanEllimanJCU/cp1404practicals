"""
CP1404/CP5632 - Practical
"""

MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ - Quit\n"
print(MENU)
choice = input("Please input your choice: ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5/9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input("Please input your choice: ").upper()
print("Thank you.")