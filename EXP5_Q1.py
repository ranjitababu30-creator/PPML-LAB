def merge_dictionaries(dictionary1, dictionary2):
    return dictionary1 | dictionary2


def main():
    dictionary1 = eval(input("Enter the first dictionary: "))
    dictionary2 = eval(input("Enter the second dictionary: "))

    merged_dictionary = merge_dictionaries(dictionary1, dictionary2)
    print("Values in the merged dictionary:", list(merged_dictionary.values()))


main()
