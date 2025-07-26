# ** Sorting Words **: Take a sentence as input and return a sorted list of unique words from that sentence.
sentence = "I am Ayush"
words = sentence.split()
unique_words = list(set(words))
unique_words.sort()
print(unique_words)