
############################
# definisco una funzione che ritorna il quadrato di un numero
def square(n):
    return n**2

squaresMap = map(square, range(10)) # map ritorna un oggetto iterabile
print (squaresMap)
#<map object at 0xb6730d8c>

print (list(squaresMap))  # convertendolo in lista si possono vedere gli elementi
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# la seguente listcomp è equivalente a usare list(map(func, seq))
squaresCom = [square(x) for x in range(10)]
print (squaresCom)
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


############################
# definisco una funzione che ritorna True se il numero è pari
def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

evenMap = filter(is_even, range(10)) # filter ritorna un oggetto iterabile
print (evenMap)
#<filter object at 0xb717b92c>

print (list(evenMap))  # convertendolo in lista si possono vedere gli elementi
#[0, 2, 4, 6, 8]

# la seguente listcomp è equivalente a usare list(filter(func, seq))
evenCom = [x for x in range(10) if is_even(x)]
print (evenCom)
#[0, 2, 4, 6, 8]
