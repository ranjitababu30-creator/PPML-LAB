def copy_set(source_set):
    new_set = set()

    for element in source_set:
        new_set.add(element)

    return new_set


def main():
    source_set = eval(input("Enter a set: "))
    copied_set = copy_set(source_set)
    print("Copied set:", copied_set)


main()
