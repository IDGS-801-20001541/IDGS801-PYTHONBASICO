
#Definir una lista 
nombre = ["juan ","Mario", "Ana"]
numero = [1,6,3,4,2,8]
datos = [1,2.5,"Mario", "Juan"]

nombre[0]="Roberto"
print(nombre[:])
print(nombre[2])
print(nombre[:3])
print(nombre[1:])

nombre.append("Dario")
print(nombre)
nombre.insert(2,"Laura")#remplazar
print(nombre)

nombre.extend(["Chencha",2,23.5])
print(nombre)

nombre.remove("Chencha")
print(nombre)

nombre.pop()#eliminar el ultimo de la lista 
print(nombre)

n=["Juan"]
n2 = n*5 
print(n2)
print(nombre)


del nombre[0]
print (nombre)

numero.reverse();
print(numero)

numero.sort()
print(numero)
