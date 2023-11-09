
def greet(greeting, *, name):
    print('{} {}!'.format(greeting, name))

#greet('Hello', 'Python')
# Error!!!
# Traceback (most recent call last): File "<stdin>", line 1, in <module> TypeError: greet() takes 1 positional argument but 2 were given

greet('Hello', name='Python')
#Hello Python!

greet(greeting='Hello', name='Python')
#Hello Python!
