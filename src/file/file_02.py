
# definiamo una lista di righe
lines = [
     'prima riga del file\n',
     'seconda riga del file\n',
     'terza riga del file\n',
]
f = open('test.txt', 'w')  # apriamo il file in scrittura
f.writelines(lines)  # usiamo il metodo writelines per scrivere le righe nel file
f.close()  # chiudiamo il file

print ("check 01")
f = open('test.txt')  # riapriamo il file in lettura
print (f.readlines())  # usiamo il metodo readlines per ottenere una lista di righe del file
#['prima riga del file\n', 'seconda riga del file\n', 'terza riga del file\n']
f.close()  # chiudiamo il file

print ("check 02")
f = open('test.txt')  # riapriamo il file in lettura
print (f.readline())  # usiamo il metodo readline per ottenere una singola riga del file
#'prima riga del file\n'
print (f.readline())  # usiamo il metodo readline per ottenere una singola riga del file
#'seconda riga del file\n'
print (f.readline())  # usiamo il metodo readline per ottenere una singola riga del file
#'terza riga del file\n'
print (f.readline())  # quando abbiamo letto tutto, il metodo restituisce una stringa vuota
#''
f.close()  # chiudiamo il file

print ("check 03")
# È possibile utilizzare un for per iterare sulle righe di un file:
f = open('test.txt')  # riapriamo il file in lettura
for line in f:  # iteriamo sulle righe del file
    print (line)
#'prima riga del file\n'
#'seconda riga del file\n'
#'terza riga del file\n'
f.close()  # chiudiamo il file
