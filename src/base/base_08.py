
######################## SET
nums = {10, 20, 30, 40}  # nuovo set di 4 elementi
print nums  # gli elementi del set non sono ordinati
#{40, 10, 20, 30}
print type(nums)  # verifichiamo che il tipo sia "set"
#<class 'set'>
fnums = frozenset(nums)  # nuovo frozenset a partire dal set nums
print fnums
#frozenset({40, 10, 20, 30})
print type(fnums)  # verifichiamo che il tipo sia "frozenset"
#<class 'frozenset'>
print {'Python'}  # set di 1 elemento (una stringa)
#{'Python'}
empty = set()  # nuovo set vuoto
print empty
#set()
print type({})  # {} crea un dict vuoto
#<class 'dict'>
print type(set())  # set() crea un set vuoto
#<class 'set'>
print type(frozenset())  # frozenset() crea un frozenset vuoto
#<class 'frozenset'>
