def lists():
    list1 = []
    list2 = []

    print("Enter 5 integers:")
    for i in range(5):
        list1.append(int(input()))

    print("Enter 5 strings:")
    for i in range(5):
        list2.append(input())

    print("Combined elements:")
    for i in range(5):
        print(list1[i], list2[i])

lists()