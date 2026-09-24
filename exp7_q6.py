from array import array

numbers = array("i", map(int, input("Enter array elements: ").split()))
total = len(numbers)

positive_ratio = sum(number > 0 for number in numbers) / total
negative_ratio = sum(number < 0 for number in numbers) / total
zero_ratio = sum(number == 0 for number in numbers) / total

print("Positive ratio:", positive_ratio)
print("Negative ratio:", negative_ratio)
print("Zero ratio:", zero_ratio)
