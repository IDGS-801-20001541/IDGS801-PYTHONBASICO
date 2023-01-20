#Programa que pida el usuario y pida la tabla de multiplicar de este numero 
num1= int(input("Dame el nùmero a multiplicar "))
for n in range (1,11):
    print(" {} * {} = {}".format(num1,n,(num1*n)))


