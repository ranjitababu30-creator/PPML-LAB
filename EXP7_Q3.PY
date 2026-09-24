bases = list(map(int, input("Enter base numbers: ").split()))
exponents = list(map(int, input("Enter corresponding exponents: ").split()))

powers = list(map(lambda base, exponent: base ** exponent, bases, exponents))

print("List of powers:", powers)
