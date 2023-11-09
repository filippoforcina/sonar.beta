
def print_twice(text):
    if not text:
        # termina immediatamente se text è una stringa vuota
        return 'no text'
    print(text)
    print(text)
    # ritorna None automaticamente al termine della funzione

# stampa 2 volte e ritorna None al termine della funzione
res = print_twice('Python')
print(res)
#None

# entra nell'if e ritorna None prima di stampare
res = print_twice('')
print(res)
#no text
