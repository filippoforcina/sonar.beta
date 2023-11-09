
f = open('test.txt', 'w')  # apriamo il file in scrittura
f.write('prima riga del file\n')  # scriviamo una riga nel file
f.write('seconda riga del file\n')  # scriviamo un'altra riga nel file
f.close()  # chiudiamo il file

f = open('test.txt')  # riapriamo il file in lettura
content = f.read()  # leggiamo tutto il contenuto del file
print(content)
#prima riga del file
#seconda riga del file
f.close()  # chiudiamo il file