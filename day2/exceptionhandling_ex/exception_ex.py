try:
    a = 10
    b = 10
    c = a + b
    d = 10/1
    f = open('xyz')
except TypeError:
    print("You cannot use + with str and int")
except ZeroDivisionError:
    print("You cannot divide by zero")
except Exception as E:
    print("Invalid usage", E)
else:
    print(c)
finally:
    print("Thanks!")