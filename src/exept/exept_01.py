
try:
    n = 5 / 0
except ArithmeticError:
    print('Invalid operation!')
#Invalid operation!

try:
    n = 5 / 0
except ZeroDivisionError as err:
    print('Invalid operation ({})!'.format(err))
#Invalid operation (division by zero)!
