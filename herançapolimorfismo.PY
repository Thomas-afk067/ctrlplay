#encapsulamento

# class A:
#     a = 1 
#     __b = 2

# class B(A):
#     __c = 3 

#     def __init__(self):
#         print(self.a)
#         print(self.__c)

# exibirA = A()
# print (exibirA.a) #Exibindo atributo publico class A
# print (exibirA.__b) #ERRO: atributo privado da class A

class animal:
    def __init__(self,nome,idade):
        self.nome=nome 
        self.idade=idade

    def emitirsom(self):
        return "som de animal"
    
    def informacao(self):
        return f"nome:{self.nome}, idade: {self.idade} anos"
    
class cachorro (animal):
    def emitirsom(self):
        return "au au!"
    

class gato(animal):
    def emitirsom(self):
        return "miauuuu"
    
class peixe (animal):
    def emitirsom(self):
        return "glubiglubi"
    
class passaro (animal):
    def emitirSom (self):
        return "aaaAAAaaAAaaAA"


animal1= cachorro("jeorgin",25)
animal2=gato("jubiskrevaldo",35)
animal3=peixe("blubbubu", 2025)
animal4=passaro("jenevaldo", 156)
print(animal1.informacao())
print(animal1.emitirsom())


print(animal2.informacao())
print(animal2.emitirsom())


    


