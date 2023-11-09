
######################## DIZIONARI
d = {'a': 1, 'b': 2, 'c': 3}  # nuovo dizionario di 3 elementi
print d
#{'c': 3, 'a': 1, 'b': 2}
print d['a']
print type(d)  # verifichiamo che il tipo sia "dict"
#<class 'dict'>
d = {20: ['Jack', 'Jane'], 28: ['John', 'Mary']}  # int come chiavi, list come valori
print d
#{28: ['John', 'Mary'], 20: ['Jack', 'Jane']}
print d[20]

########################
d = {'a': 1, 'b': 2, 'c': 3}  # nuovo dict di 3 elementi
print len(d)  # verifica che siano 3
#3
print d.items()  # restituisce gli elementi
#dict_items([('c', 3), ('a', 1), ('b', 2)])
print d.keys()  # restituisce le chiavi
#dict_keys(['c', 'a', 'b'])
print d.values()  # restituisce i valori
#dict_values([3, 1, 2])
print d.get('c', 0)  # restituisce il valore corrispondente a 'c'
#3
print d.get('x', 0)  # restituisce il default 0 perche' 'x' non e' presente
#0
print d  # il dizionario contiene ancora tutti gli elementi
#{'c': 3, 'a': 1, 'b': 2}
print d.pop('a', 0)  # restituisce e rimuove il valore corrispondente ad 'a'
#1
print d.pop('x', 0)  # restituisce il default 0 perche' 'x' non e' presente
#0
print d  # l'elemento con chiave 'a' e' stato rimosso
#{'c': 3, 'b': 2}
print d.popitem()  # restituisce e rimuove un elemento arbitrario
#('c', 3)
print d  # l'elemento con chiave 'c' e' stato rimosso
#{'b': 2}
d.update({'a': 1, 'c': 3})  # aggiunge di nuovo gli elementi 'a' e 'c'
print d
#{'c': 3, 'a': 1, 'b': 2}
d.clear()  # rimuove tutti gli elementi
print d  # lasciando un dizionario vuoto
#{}
