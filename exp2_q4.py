num = int(input("Enter a number: "))

s = 0

for i in range(1, num):
    if num % i == 0:
        s = s + i

if s == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
