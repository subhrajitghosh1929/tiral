def remove_letter(sentence, letter):
    words = sentence.split()  
    new_sentence = []  
    for word in words:
        new_word = ''
        for char in word:
            if char.lower() != letter.lower():  
                new_word += char
        new_sentence.append(new_word)  
    return ' '.join(new_sentence)  

def capwords_custom(sentence):
    words = sentence.split()  
    capitalized_words = []
    for word in words:
       capitalized_word = word.capitalize()
       capitalized_words.append(capitalized_word)
    return ' '.join(capitalized_words)  

sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")
print("After removing letter:", remove_letter(sentence, letter))  

from string import capwords
sentences_input = input("Enter a sentence: ")
sentences = sentences_input.split('.') 

for sentence in sentences:
    sentence = sentence.strip()  
    print("Custom capwords result:", capwords_custom(sentence))
    print("Capwords result from string module:", capwords(sentence))
