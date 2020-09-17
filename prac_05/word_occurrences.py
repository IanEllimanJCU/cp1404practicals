def main():
    count_word_occurences = {}
    user_string = []
    user_string = input("Please enter a string ")
    split_user_string = user_string.split()
    split_user_string.sort()
    print(split_user_string)
    longest_len_word = 0
    for i in split_user_string:
        if len(i) > longest_len_word:
            longest_len_word = len(i)
        if i in count_word_occurences:
            count_word_occurences[i] += 1
        else:
            count_word_occurences[i] = 1
    for i in count_word_occurences:
        if len(i) < longest_len_word:
            print(f"{i} : {count_word_occurences[i]:>{longest_len_word-len(i)+1}}")
        else:
            print(f"{i} : {count_word_occurences[i]}")
main()