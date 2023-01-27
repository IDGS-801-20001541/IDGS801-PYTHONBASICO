#Calculadora basica 

class Calculadora:
    #propiedades de clases
    n1=0
    n2=0
    res=0
    
    #constructor de clase
    def _init_(self, a,b) -> None :
        self.n1 = a
        self.n2 = b

    #los metodos de clase
    def suma(self, a,b):
        self.res=a+b
        
    def resta(self, a,b):
        self.res=a-b
    def multiplicacion(self, a,b):
        self.res=a*b
    def division(self, a,b):  
        try: 
            self.res=a/b
        except ZeroDivisionError:
            print("No se puede diviidir entre 0 :'(")




def main():
    op =0 
    while True: 
        print(" Menu \n 1- Suma \n 2- Resta \n 3- Multiplicación  \n 4- Division \n 5- Salir")    

        op = int(input("Elige la opción "))
    
        if op == 1:
            nu1= float(input("Escriba el primer número "))
            nu2= float(input("Escriba el primer número "))

            obj=Calculadora()
            obj.suma(nu1,nu2)
            print("La suma es: {}".format(obj.res))
        elif op == 2:
            nu1= float(input("Escriba el primer número "))
            nu2= float(input("Escriba el primer número "))

            obj=Calculadora()
            obj.resta(nu1,nu2)
            print("La Resta es: {}".format(obj.res))

        elif op == 3:
            nu1= float(input("Escriba el primer número "))
            nu2= float(input("Escriba el primer número "))

            obj=Calculadora()
            obj.multiplicacion(nu1,nu2)
            print("La multiplicación es: {}".format(obj.res))


        elif op == 4:
            nu1= float(input("Escriba el primer número "))
            nu2= float(input("Escriba el primer número "))

            obj=Calculadora()
            obj.division(nu1,nu2)
            print("La resta es: {}".format(obj.res)) 
        else:
            exit

if __name__ == '__main__':
    main()