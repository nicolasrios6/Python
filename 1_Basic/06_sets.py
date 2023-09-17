# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {'Nico', 'Rios', 23}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Baco')
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('Baco')
print(my_other_set) # Un set no permite datos repetidos

print("Nico" in my_other_set) # Devuelve true si el elemento se encuentra en el set
print("Niko" in my_other_set) # Devuelve false si el elemento se encuentra en el set

my_other_set.remove("Nico") # Elimina un elemento del set
print(my_other_set)

my_other_set.clear() # Borra los elementos del set
print(len(my_other_set))


del my_other_set

my_set = {'Nico', 'Rios', 23}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {'Kotlin', 'Swift', 'Python'}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))