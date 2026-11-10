with open("notes.txt", "w") as file:
    file.write("Hello, this is my first note.\nPython file handling is simple.\nEnd of file.")
with open("notes.txt", "r") as file:
    for line in file:
        print(line)