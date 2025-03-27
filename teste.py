import unittest 

# def Soma(A,B):
#     return A+B 

# class testSoma(unittest.TestCase):

#     def testSomaPositivo(self):
#         self.assertEqual(Soma(2,3),5)

#     def testSomaNegativos(self):
#         self.assertEqual(Soma(-2,-3),-5)

#     def testSomasZeros(self):
#         self.assertEqual(Soma(0,0),0)

# if __name__ == '__main__':
#     unittest.main()

# def dividir(a,b):
#     if b == 0:
#        raise ValueError("Divisao por zero nao permitida")
#     else:
#        return a/b 
    
# class testdividir(unittest.TestCase):
   
#    def testDivisaopPorZero(self):
#         with self.assertRaises(ValueError):dividir(10,0)

# if __name__ =='__main__':
#     unittest.main()


class calculadora:
    def __init__(self):
        self.resultado = 0 

        def soma(self,a,b):
            return a+b
        def subtracao(self , a , b ):
            return a-b
        def multiplicacao(self , a , b ):
            return a*b
        def divisao (self,a,b): 
            if b == 0:
                raise ValueError("Divisao por 0 pode nao man")
            else:
                return a/b
            
class testcalculadora(unittest.testcase):

    def setUp(self):
        self.C= calculadora()

    def testSoma(self):
        self.assertEqual(self.C.soma(5,3),8)

    def testsubtracao(self):
        self.assertEqual(self.C.subtracao(-5,-3),-8)

    def testmultiplicacao(self):
        self.assertEqual(self.C.multiplicacao(5,3),8)

    def testdivisao(self):
        self.assertEqual(self.C.divisao(5,3),8) 

    def testdivisaoporzero(self):
        with self.assertRaises(ValueError):self.C.divisao(10,0)

if __name__ == '__main__':
    unittest.main()

        

