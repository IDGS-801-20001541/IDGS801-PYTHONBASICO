#Calculadora basica 

class Calculadora:
    #propiedades de clases
    n1=0
    n2=0
    res=0
    #constructor de clase
    def _init_(self, a,b) :
        self.n1 = a
        self.n2 = b

    #los metodos de clase
    def suma(self):
        self.res=self.n1+self.n2
    def resta(self):
        self.res=self.n1-self.n2
    def multiplicacion(self):
        self.res=self.n1*self.n2
    def division(self):  
        try: 
            self.res=self.n1/self.n2
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

        obj=Calculadora(nu1,nu2)
        obj.suma()
        print("La suma es: {}".format(obj.res))
       
    elif op == 3:
        nu1= float(input("Escriba el primer número "))
        nu2= float(input("Escriba el primer número "))

        obj=Calculadora(nu1,nu2)
        obj.multiplicacion()
        print("La multiplicación es: {}".format(obj.res))


    elif op == 4:
        nu1= float(input("Escriba el primer número "))
        nu2= float(input("Escriba el primer número "))

        obj=Calculadora(nu1,nu2)
        obj.division()
        print("La resta es: {}".format(obj.res)) 
    else:
        exit

if __name__ == '__main__':
    main()