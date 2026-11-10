text = "hello world from python"
capitalized_words = []
for word in text.split():
    word.capitalize()
    capitalized_words.append(word)
result = " ".join(capitalized_words)
print(result)