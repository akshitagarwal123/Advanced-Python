# a = 1/0


try:
    a = 1/0
except ZeroDivisionError:
    print('There was an error')
except Exception as E:
    print('Some other error -> ', E)
else:
    print('Everything went well')
finally:
    print('Thank you!')



print('---------------------')