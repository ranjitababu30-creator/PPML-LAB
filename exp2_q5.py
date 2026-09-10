s = input("Enter a string: ")

print("Reverse string:", s[::-1])

v = 0
c = 0

for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        v = v + 1
    elif i.isalpha():
        c = c + 1

print("Vowels =", v)
print("Consonants =", c)
