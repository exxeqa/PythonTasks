words = []
with open("sample.txt", "r") as file:
    text = file.read()
    for word in text.split():
        words.append(word)
print(f"There are {len(words)} words in total.")