
######################## TUPLE
t = ('abc', 123, 45.67)  # la virgola crea la tupla
print t  # la rappresentazione di una tupla include sempre le ()
#('abc', 123, 45.67)
print t[0]  # le tuple supportano indexing
#abc
print type(t)
#<class 'tuple'>
tp = ('abc', 123, 45.67)  # le () evitano ambiguita'
print t == tp  # il risultato e' equivalente
#True
print len((1, 'a', 2.3))  # in questo caso le () sono necessarie
#3

########################
print len(('abc', 123, 45.67, 'xyz', 890))  # numero di elementi
#5
print min((4, 1, 7, 5))  # elemento piu' piccolo
#1
print max((4, 1, 7, 5))  # elemento piu' grande
#7
t = ('a', 'b', 'c', 'b', 'a')
print t.index('c')  # indice dell'elemento 'c'
#2
print t.count('c')  # numero di occorrenze di 'c'
#1
print t.count('b')  # numero di occorrenze di 'b'
#2
