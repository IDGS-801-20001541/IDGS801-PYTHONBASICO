class OperasBas:
    #propiedades de clases
    n1=0
    n2=0
    res=0
    #constructor de clase
    def _init_(self, a,b) -> None:
        self.n1 = a
        self.n2 = b

    #los metodos de clase
    def suma(self):
        self.res=self.n1+self.n2
    def resta(self):
        self.res=self.n1-self.n2

def main():
    obj=OperasBas(3,2)
    obj.suma()
    print("La suma es: {}".format(obj.res))

if __name__ == "_main_":
    main()