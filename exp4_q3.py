def create_list():
    numbers = [0] * 20

    for i in range(20):
        numbers[i] = int(input("Enter number: "))

    for i in range(20):
        if numbers[i] % 2 != 0:
            numbers[i] += 5

    print(numbers)

create_list()