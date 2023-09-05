# Tuplas
my_tuple = tuple()
my_other_tuple = (23, 60, 30, 17)

my_tuple = (23, 1.93, "Nico", "Rios", 'Pepe')
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Nico"))
print(my_tuple.index("Rios"))

#my_tuple[1] = 1.98 error
#print(my_tuple) las tuplas son inmutables, no se pueden modificar.

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple)) # cambiar de tupla a lista

my_tuple[4] = "Pepito"
my_tuple.insert(1, 'Azul')
my_tuple = tuple(my_tuple)
print(type(my_tuple)) #cambio de lista a tupla

#del my_tuple[2] 'tuple' object doesn't support item deletion
#del my_tuple
#print(my_tuple) 'my_tuple' is not defined
