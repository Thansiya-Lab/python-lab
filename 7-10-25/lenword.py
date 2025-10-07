def length_of_longest_word(words_list):
    longest_length = 0
    for word in words_list:
        if len(word) > longest_length:
            longest_length = len(word)
    return longest_length
words_list = input("Enter words: ").split()
print("length of longest word: " ,length_of_longest_word(words_list))
