#una tupla es estatica 

tupla = (1,2,3,)
print(tupla)
print(type(tupla))

tupla2 = (7,"Roberto", True, 23.8, 15+7j)
print(tupla2)

print(tupla2[1]) #Acceder a un elemento de la tupla 
print(tupla2[4])
print(tupla2[-1])# - empieza desde el final de la tupla 

print(tupla2[0:3]) #tomar una seccion de los elementos de la tupla
print(tupla2[3:])#empiese desde la posicion de 3 hasta acabar 

a,b,c = tupla
print(a)
print(c)

tuplaN = tupla+tupla2
print(tuplaN)

print(tupla.count(True))

tupla[2]=23