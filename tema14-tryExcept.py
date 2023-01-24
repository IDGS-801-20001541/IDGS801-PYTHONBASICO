num1 = 20
num2 = 0

#tem=num1/num2
try: 
    tem=num1/num2
except ZeroDivisionError:
    print("Error en el programa :'(")
finally:
    print("Siempre aparezco (nimodin)")
