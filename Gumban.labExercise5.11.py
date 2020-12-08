import re
def syllables(word):
    word = word.lower()
    if word.endswith('e'):
        word = word[:-1]
    count = len(re.findall('[aeiou]+', word))
    return count
word = str(input("Input word: "))
print ("Number of vowels in the word","'", word,"'", ":",syllables(word))
