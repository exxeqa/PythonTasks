vowels = "aeiou"
sentence = "Learning Python is fun!"
vowel = 0
for letter in sentence.lower():
    if letter in vowels:
        vowel += 1
    else:
        pass
print(f"in this sentance is {vowel}")