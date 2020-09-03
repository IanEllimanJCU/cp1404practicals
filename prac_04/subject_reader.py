"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    longest_length_name=0
    longest_length_students_count=0
    data = get_data()
    print(data)
    for list in data:
        if len(list[1]) > longest_length_name:
            longest_length_name = len(list[1])
        if len(list[2]) > longest_length_students_count:
            longest_length_students_count = len(list[2])
    for list in data:
        print(f"{list[0]} is taught by {list[1]:<{longest_length_name}} and has {list[2]:>{longest_length_students_count}} students")



def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_subjects =[]
    for line in input_file:
        line = line.strip()
        line = line.split(",")
        list_of_subjects.append(line)
 #       print(line)  # See what a line looks like
 #       print(repr(line))  # See what a line really looks like
 #       line = line.strip()  # Remove the \n
 #       parts = line.split(',')  # Separate the data into its parts
 #       print(parts)  # See what the parts look like (notice the integer is a string)
 #       parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
 #       print(parts)  # See if that worked
 #       print("----------")
    input_file.close()
    return list_of_subjects

main()