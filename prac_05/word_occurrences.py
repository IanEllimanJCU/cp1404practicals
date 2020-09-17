def main():
    count_word_occurences = {}
    user_string = []
    user_string = input("Please enter a string ")
    split_user_string = user_string.split()
    split_user_string.sort()
    longest_len_word = max(len(split_user_string) for split_user_string in split_user_string)
    for i in split_user_string:
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