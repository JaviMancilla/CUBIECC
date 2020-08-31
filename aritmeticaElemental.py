
class aritmeticaElemental:

    def __init__(self, a, b):
        self.a = a
        self.b = b


    def inversomodular(self, a, b):
            (u0,u1) = (1,0)
            while b>0:
                (u0,u1) = (u1,u0-(a//b)*u1)
                (a,b) = (b,a%b)
            if a == 1:
                return u0
            else:
                print("No existe el inverso")
            return 0