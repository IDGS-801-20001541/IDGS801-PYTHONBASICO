class OperasBasic:
    #1:Propiedades de clase 
    n1=0
    n2=0
    result=0
    #2:Constructor con parametros (self, a, b) basio (self)
    def __init__(self,a,b):
        self.n1 = a
        self.n2 = b
        
    #3:Métodos de clase
    def suma(self):
       res = self.result=self.n1+self.n2
   

    def resta(self):
        self.result=self.n1-self.n2


    def main():
        obj = OperasBasic(3,2)
        obj.suma()

    if __name__ == '__main__':
        main()