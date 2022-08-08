a = input("Enter a number: ")
b = input("Enter another number: ")
res = 0
D = {'name': 'Sunil'}
try:
    res = a/b
except Exception as E:
    print("There was an exception")
    print(E)

print('-'*60)

try:
    print(D['rank'])
    res = int(a)/0
    res = a/b
except KeyError:
    print("Key not found")
except TypeError:
    print("There was a type error")
except:
    print("Some other error")

print('The result is ', res)
   
print('-'*60)

try:
    print(D['name'])
except KeyError:
    print("Key not found")
except TypeError:
    print("There was a type error")
except:
    print("Some other error")
else:
    print('The result is ', res)

print('-'*60)

try:
    print(D['rank'])
except KeyError:
    print("Key not found")
except TypeError:
    print("There was a type error")
except:
    print("Some other error")
else:
    print('The result is ', res)
finally:
    print("Thank you!")

print("Proceeding futher .... ")