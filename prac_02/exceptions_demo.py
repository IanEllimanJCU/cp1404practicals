# When will a ValueError occur?
# When any value that isn't an integer is entered.
# When will a ZeroDivisionError occur?
# When zero is entered as the denominator.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Uhhh... detect when the user enters 0 and prompt them to enter a non-zero number?
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("You have entered 0 as the denominator, this is not valid. Please enter a number that is not 0")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
print("Finished.")
exit()