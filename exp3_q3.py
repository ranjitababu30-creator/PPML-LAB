def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


def main():
    n = int(input("Enter the year: "))

    if is_leap_year(n):
        print("It's a Leap Year")
    else:
        print("Not a Leap Year")
main()