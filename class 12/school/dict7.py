# Question
# Write a function to check if two strings are anagrams using dictionaries. 
def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    char_count1 = {}
    char_count2 = {}
    for char in str1:
        char_count1[char] = char_count1.get(char, 0) + 1
    for char in str2:
        char_count2[char] = char_count2.get(char, 0) + 1
    return char_count1 == char_count2

word1 = "listen"
word2 = "silent"
if are_anagrams(word1, word2):
    print(f"{word1} and {word2} are anagrams.")
else:
    print(f"{word1} and {word2} are not anagrams.")
