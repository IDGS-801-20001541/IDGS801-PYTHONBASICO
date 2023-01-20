cadena= "Universidad Tecnologica de Leòn"

print(cadena)
print(cadena.lower()) #minusculas
print(cadena.upper())#mayusculas
print(cadena.title())

#buscar cadena de una cadena , contar 
print(cadena.find("de"))
print(cadena.count("a"))

textofinal= cadena.replace("a","4")
print(textofinal)
# split= Separacion de palabras de una cadena cada elemento de una lista es una palabra 
# ['Universidad', 'Tecnologica', 'de', 'Leòn'] 
cadenaNueva=cadena.split(" ")
print(cadenaNueva)

