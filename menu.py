x=0
while (x !=1):
    print("\nMenu:")
    print("1. Occurrence of a word")
    print("2. Character frequency")
    print("3. Factorial of a number")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        a=input("Enter line of text:")
        words=a.split()
        count_words=[]
        counts=[]
        for s in words:
            if s not in count_words:
                count=0
                for i in words:
                    if i==s:
                        count+=1
                count_words.append(s)
                counts.append(count)
        for i in range(len(count_words)):
            print(count_words[i],":",counts[i])

    elif choice == '2':
        word = input("Enter a word: ")
        char_count = {}
        for char in word:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        print("Character occurrences:")
        for char, count in char_count.items():
            print(f"'{char}': {count}")

    elif choice == '3':
        n = int(input("Enter a positive integer: "))
        print("Factors of ",n, "are:")
        for i in range(1, n + 1):
            if n % i == 0:
                print(i)

    elif choice == '4':
        print("Exiting the program. Goodbye!")
        x=1
    else:
        print("Invalid choice")
