
def try_except_else_test(x):
    try:
        n = int(x)  # prova a convertire x in intero
    except ValueError as err:
        # eseguito in caso di ValueError
        print('Invalid value ({})!'.format(err))
    else:
        # eseguito se non ci sono errori
        print('Valid number!')
        return n
    finally:
        print('End function')

try_except_else_test('five')  # numero non valido: esegue l'except
#Invalid number!
try_except_else_test('5')  # numero valido: esegue l'else
#Valid number!
