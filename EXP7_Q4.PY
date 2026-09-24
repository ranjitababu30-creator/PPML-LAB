sequence = input("Enter a sequence: ")

uppercase = "".join(dict.fromkeys(map(str.upper, sequence)))
lowercase = "".join(dict.fromkeys(map(str.lower, sequence)))

print("Uppercase without duplicates:", uppercase)
print("Lowercase without duplicates:", lowercase)
