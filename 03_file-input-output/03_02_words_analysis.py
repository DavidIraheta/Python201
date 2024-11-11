# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.
with open ("/Users/davidiraheta/Documents/CodingNomads/Projects/python-201-main/03_file-input-output/words.txt", "r") as file:
    words = file.read().split()
    shortest = []
    longest = []
    total_words = []

    if words:
        min_length = len(words[0])
        max_length = len(words[0])
        for word in words:
            if len(word) < min_length:
                min_length = len(word)
                shortest = [word]
            elif len(word) == min_length:
                shortest.append(word)
            if len(word) > max_length:
                max_length = len(word)
                longest = [word]
            elif len(word) == max_length:
                longest.append(word)
    total_words = len(words)
    print(f"The shortest word(s) is/are: {shortest}")
    print(f"The longest word(s) is/are: {longest}")
    print(f"The total number of words in the file is: {total_words}")
    
