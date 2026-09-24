def combine_sets(first_set, second_set):
    return first_set.union(second_set)


set1 = set(input("Enter string elements for first set (space-separated): ").split())
set2 = set(input("Enter string elements for second set (space-separated): ").split())

new_set = combine_sets(set1, set2)
print("New set:", new_set)
