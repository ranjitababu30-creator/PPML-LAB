def find():
    a = []

    for i in range(10):
        a += [int(input("Enter number: "))]

    a.sort()

    print("Second Smallest =", a[1])
    print("Second Largest =", a[-2])

find()