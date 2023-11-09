
############################## LISTE
nums = [0, 1, 2, 3] # nuova lista di 4 elementi
print nums
#[0, 1, 2, 3]
print type(nums) # verifichiamo che il tipo sia "list"
#<class 'list'>
empty = [] # nuova lista vuota
print empty
#[]
one = ['Python'] # nuova lista con un elemento
print one
#['Python']


##############################
letters = ['a', 'b', 'c', 'd', 'e']
print letters[0] # le liste supportano indexing
#'a'
print letters[-1]
#'e'
print letters[1:4] # slicing
#['b', 'c', 'd']
print 'a' in letters # gli operatori di contenimento "in" e "not in"
#True
print letters + ['f', 'g', 'h'] # concatenazione (ritorna una nuova lista)
#['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print [1, 2, 3] * 3 # ripetizione (ritorna una nuova lista)
#[1, 2, 3, 1, 2, 3, 1, 2, 3]
