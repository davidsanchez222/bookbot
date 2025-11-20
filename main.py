with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    word_list = file_contents.split()
    [print(word, i) for word, i in enumerate(word_list)]
