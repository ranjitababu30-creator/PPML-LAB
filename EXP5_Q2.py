def remove_duplicate_values(dictionary):
    unique_dictionary = {}
    seen_values = []

    for key, value in dictionary.items():
        if value not in seen_values:
            unique_dictionary[key] = value
            seen_values.append(value)

    return unique_dictionary


def main():
    dictionary = eval(input("Enter a dictionary: "))
    result = remove_duplicate_values(dictionary)
    print("Dictionary after removing duplicate values:", result)


main()
