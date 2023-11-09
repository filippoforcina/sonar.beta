
def div(num, den):
    if den == 0:
        # se il denominatore è 0 riporta un'eccezione
        raise ZeroDivisionError('Impossibile dividere per 0')
    return num / den

print (div(8, 2))
#4.0
print (div(8, 0))
#Error ZeroDivisionError: Impossibile dividere per 0

