import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

d = b**2 - 4*a*c 

if a == 0:
    print("Not a quadratic equation.")
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are real and different.")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif d == 0:
    root = -b / (2 * a)
    print("Roots are real and equal.")
    print("Root =", root)
else:
    real = -b / (2 * a)
    imag = math.sqrt(-d) / (2 * a)
    print("Roots are complex.")
    print("Root 1 =", real, "+", imag, "i")
    print("Root 2 =", real, "-", imag, "i")
