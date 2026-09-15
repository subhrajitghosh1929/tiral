# Question
# Write a function to count the frequency of words in a sentence using a dictionary.

def count_word_frequency(sentence):
    words = sentence.split()
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

input_sentence = "Python is a powerful programming language. Python is used for various applications."
word_frequency = count_word_frequency(input_sentence)
print("Word Frequency:", word_frequency)

