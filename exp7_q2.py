list1 = list(map(int, input("Enter first list of integers: ").split()))
list2 = list(map(int, input("Enter second list of integers: ").split()))
list3 = list(map(int, input("Enter third list of integers: ").split()))

result = list(map(lambda a, b, c: a + b + c, list1, list2, list3))

print("Sum of the three lists:", result)
