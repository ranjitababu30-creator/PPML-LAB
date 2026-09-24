numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
tripled_numbers = list(map(lambda number: number * 3, numbers))

print("Tripple list:", tripled_numbers)
