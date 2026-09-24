def remove_duplicate_values(dictionary):
    result = {}
    seen_values = []

    for key, value in dictionary.items():
        if value not in seen_values:
            result[key] = value
            seen_values.append(value)

    return result


def main():
    dictionary = eval(input("Enter a dictionary: "))
    unique_dictionary = remove_duplicate_values(dictionary)
    print("Dictionary after removing duplicate values:", unique_dictionary)


main()
