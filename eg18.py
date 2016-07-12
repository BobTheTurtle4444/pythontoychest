# 18.py - this program illustrates Python except handling using try, except, and finally.
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("Inside Finally block.")
