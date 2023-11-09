
def divisor(num, den):
    try:
        ret = num / den
    except ZeroDivisionError as err:
        # stampa informazioni sull'errore
        print('* Logged exception:', err)
        print('* Re-raising exception.')
        raise  # lascia che l'eccezione originale si propaghi
    else:
        return ret

print (divisor(8, 2))
#4.0
print (divisor(8, 0))
#Error ZeroDivisionError: Impossibile dividere per 0
