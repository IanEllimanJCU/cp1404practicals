def main():
    numbers = []
    for i in range(5):
        numbers.append(int(input("Please input a number: ")))
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[4]}")
    numbers.sort()
    print(f"The smallest number is {numbers[0]}")
    print(f"The smallest number is {numbers[4]}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = input("Please input your username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")
main()