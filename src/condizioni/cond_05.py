
squares = []
for x in range(10):
    print(x**2)
    squares.append(x**2)
print(squares)

# list comprehension che crea una lista di quadrati
print([x**2 for x in range(10)])
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# set comprehension che crea un set di cubi
print({x**2 for x in range(10)})
#{0, 1, 64, 512, 8, 343, 216, 729, 27, 125}

for c in 'abcde':
    print(c)

# dict comprehension che mappa lettere lowercase all'equivalente uppercase
print({c: c.upper() for c in 'abcde'})
#{'c': 'C', 'e': 'E', 'a': 'A', 'b': 'B', 'd': 'D'}
