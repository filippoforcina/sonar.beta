
# definiamo una lista di righe
lines = [
    'prima riga del file\n',
    'seconda riga del file\n',
    'terza riga del file\n',
]
f = open('test.txt', 'w')  # apriamo il file in scrittura
f.writelines(lines)  # usiamo il metodo writelines per scrivere le righe nel file
f.seek(0, 0)  # eseguiamo un seek per spostarci all'inizio del file (il secondo 0 indica l'inizio)
f.write('PRIMA')  # scriviamo 'PRIMA' all'inizio del file sovrascrivendo 'prima'
f.seek(0, 2)  # eseguiamo un seek per spostarci alla fine del file (il 2 indica la fine)
f.write('quarta riga del file\n')  # aggiungiamo una riga alla fine
f.close()  # chiudiamo il file

f = open('test.txt')  # riapriamo il file in lettura
print (f.readline())  # usiamo il metodo readline per ottenere una singola riga del file
#'PRIMA riga del file\n'
print (f.readline())  # usiamo il metodo readline per ottenere un'altra riga del file
#'seconda riga del file\n'
print (f.tell())  # vediamo che la posizione nel file è avanzata
#42
print (f.read())  # usiamo il metodo read per leggere il resto del contenuto del file
#'terza riga del file\nquarta riga del file\n'
print (f.tell())  # vediamo che la posizione nel file è avanzata ulteriormente
#83
print (f.read())  # quando abbiamo letto tutto, il metodo restituisce una stringa vuota
#''
f.seek(0)  # eseguiamo un seek per spostarci all'inizio del file
print (f.tell())  # vediamo che la posizione è ritornata a 0
#0
print (f.readlines())  # rileggiamo l'intero contenuto del file come lista di stringhe
#['PRIMA riga del file\n', 'seconda riga del file\n', 'terza riga del file\n', 'quarta riga del file\n']
f.close()  # chiudiamo il file
