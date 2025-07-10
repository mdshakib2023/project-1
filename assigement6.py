#Create a program to count the number of words in a sentence.

def count_words(sentence):
    words = sentence.split()
    return len(words)

sentence = "my name is shakib"
count = count_words(sentence)
print("Number of words:",count)
