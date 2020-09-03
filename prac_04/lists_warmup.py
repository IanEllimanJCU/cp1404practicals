def main():
    numbers = [3, 1, 4, 1, 5, 9, 2]

    print(numbers[0])
    print(numbers[-1])
    print(numbers[3])
    print(numbers[:-1])
    print(numbers[3:4])
    print(f"{5 in numbers}")
    print(f"{7 in numbers}")
# "3" in numbers?
    numbers = numbers + [6, 5, 3]
    print(f"{numbers}")

    numbers = [3, 1, 4, 1, 5, 9, 2]
# Change the first element of numbers to "ten" (the string, not the number 10)
    numbers[0] = "ten"
# Change the last element of numbers to 1
    numbers[-1] = 1
# Get all the elements from numbers except the first two (slice)
    print(f"{numbers[2:len(numbers)]}")
# Check if 9 is an element of numbers
    print(f"{9 in numbers}")

main()
# Without running the code, write down your answers to these questions (on paper, or in your Python file as a comment)
# , then use Python to see if you were correct.
# numbers[0]
# 3
# numbers[-1]
# 2
# numbers[3]
# 1
# numbers[:-1]
# not sure
# numbers[3:4]
# 1, 5
# 5 in numbers
# not sure
# 7 in numbers
# not sure
# "3" in numbers
# not sure
# numbers + [6, 5, 3]
# not sure