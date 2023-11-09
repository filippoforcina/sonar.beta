
def say_hello(*names):
    print('Hello {}!'.format(', '.join(names)))

say_hello('Python')
#Hello Python!

say_hello('Python', 'Cobra', 'Boa', 'Mamba')
#Hello Python, PyPy, Jython, IronPython!
