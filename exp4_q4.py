def odd():
    n = int(input("Enter a number: "))

    for i in range(15):
        if n % 2 == 0:
            n += 1
        print(n + 5)
        n += 2

odd()