"""
CP1404/CP5632 - Practical
Task 3
"""
for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 110, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
star_count=int(input('How many stars would you like to print? '))
print('Number of stars:',(star_count))
for i in range(0, (star_count), 1):
    print('*', end="")
print()
print('Number of stars:',(star_count))
for i in range(1, (star_count+1), 1):
    print('*' * (i))
print()
exit()