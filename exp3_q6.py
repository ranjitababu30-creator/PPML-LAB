def remove_duplicates(s):
    result = ""

    for ch in s:
        if ch not in result:
            result = result + ch

    print("String after removing duplicates:", result)

text = input("Enter a string: ")
remove_duplicates(text)