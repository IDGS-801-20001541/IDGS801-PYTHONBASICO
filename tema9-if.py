print("Valores de usuario")
num1= int(input("Dame el valor 1: "))
num2= int(input("Dame el valor 2: "))

if(num1>num2):
    print("{} este es mayor que {}" .format(num1,num2))
else:
     print("{1} este es mayor que {0}" .format(num1,num2))