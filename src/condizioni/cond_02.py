
# stampa il quadrato di ogni numero di seq
seq = [1, 2, 3, 4, 5]
for n in seq:
     print('Il quadrato di', n, 'e', n**2)

# determina se i numeri di seq sono pari o dispari
seq = [1, 2, 3, 4, 5]
for n in seq:
     print('Il numero', n, 'e', end=' ')
     if n%2 == 0:
         print('pari')
     else:
         print('dispari')

rng = range(5)  # ritorna un oggetto range con start uguale a 0 e stop uguale a 5
print(list(rng))  # convertendolo in lista possiamo vedere i valori
#[0, 1, 2, 3, 4]
print(list(range(5, 10)))  # con 2 argomenti si può specificare lo start e lo stop
#[5, 6, 7, 8, 9]
print(list(range(0, 10, 2)))  # con 3 argomenti si può specificare anche lo step
#[0, 2, 4, 6, 8]
for n in range(1, 6):
     print('Il quadrato di', n, 'e', n**2)
