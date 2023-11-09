
f = open('test.txt', 'w')  # creiamo il file object
with f:  # usiamo il file object come context manager nel with
    f.write('contenuto del file')  # scriviamo il file
    print (f.closed)  # verifichiamo che il file è ancora aperto
#False
print (f.closed)  # verifichiamo che dopo il with il file è chiuso
#True

with open('test.txt', 'w') as f:
    f.write('contenuto del file')
    print (f.closed)  # verifichiamo che il file è ancora aperto
#False
print (f.closed)  # verifichiamo che dopo il with il file è chiuso
#True
