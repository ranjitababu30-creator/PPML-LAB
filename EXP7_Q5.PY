integer_list = list(map(int, input("Enter integers for the list: ").split()))
integer_tuple = tuple(map(int, input("Enter integers for the tuple: ").split()))

list_as_strings = list(map(str, integer_list))
tuple_as_strings = list(map(str, integer_tuple))

print("List converted to strings:", list_as_strings)
print("Tuple converted to strings:", tuple_as_strings)
