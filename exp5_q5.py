def perform_set_operations(set1, set2):
    return {
        "Union": set1.union(set2),
        "Intersection": set1.intersection(set2),
        "Difference (Set 1 - Set 2)": set1.difference(set2),
        "Difference (Set 2 - Set 1)": set2.difference(set1),
        "Symmetric Difference": set1.symmetric_difference(set2),
    }


def main():
    set1 = eval(input("Enter the first set: "))
    set2 = eval(input("Enter the second set: "))

    results = perform_set_operations(set1, set2)
    for operation, result in results.items():
        print(operation + ":", result)


main()
