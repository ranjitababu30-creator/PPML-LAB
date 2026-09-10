def even_words(s):
    words = s.split()

    for word in words:
        if len(word) % 2 == 0:
            print(word)

text = input("Enter a string: ")
even_words(text)