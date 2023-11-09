n = 8
for x in range(3):
     guess = int(input('Inserisci un numero da 1 a 10: '))
     if guess == n:
         print('Hai indovinato!')
         break  # numero indovinato, interrompi il ciclo
else:
     print('Tentativi finiti. Non hai indovinato')
