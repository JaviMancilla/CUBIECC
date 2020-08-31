"""
ARITMÉTICA DE CUERPOS BINARIOS
-------------------------------

Este modulo permite operar (suma, multiplicación, resto e inverso de un polinomio) con polinomios binarios F 2^m.

Un polinomio binario será representado como una cadena de CEROS y UNOS o como, dicha candena,
convertida a su numero entero, tal como se presenta en el ejemplo.
    Ejemplo:    x = 10 = 2
                x + 1 = 11 = 3
                x^3 + x^2 + 1 = 1101 = 13
                x^5 + x + 1 = 100011 = 35

"""

import math
import copy 
import random
import sys


class aritmeticaCuerposBinarios:     

    def __init__(self, contexto):
        self.c = contexto

#-------------------------------------------------------------------------------------------------------------------------

    """
        FUNCIÓN sumaPolinomio(pol1, pol2):
        ----------------------------------
        Función que suma dos números, que mediante el operador de asignacion ' ^ ' realiza la operacion XOR bit a bit.

        ENTRADA: Dos números enteros 'a' y 'b'.
        SALIDA: Un número entero resultado de la operación XOR bit a bit

    """

    def suma(self, a, b):

        resultado = a ^ b

        return resultado

#-------------------------------------------------------------------------------------------------------------------------

    """
        FUNCIÓN multiplicacion(a, b):
        -----------------------------------

        Función que multiplica dos números dados en la entrada, que se  .

        ENTRADA: Dos numeros enteros 'a' y 'b'
        SALIDA: Un numero entero resultado de la multiplicación de los números dados en la entrada. 

        ^ XOR bit a bit
        << Desplazamiento a la izquierda bit a bit

    """

    def multiplicacion(self, a, b):
        
        #print(pol1)
        r = a
        #print(r)
        n = 0
        bin_b = bin(b)[2:]

        for i in reversed(bin_b):
            if i=='1':
                n ^= r
            r=r << 1
            
        return n

#-------------------------------------------------------------------------------------------------------------------------

    """
        FUNCIÓN resto(n, c)
        -----------------------------------

        Función que realiza la funcion de calcular el resto de dos numeros dados. 

        ENTRADA: Dos enteros (n, c).
        SALIDA: La salida es el resultado de realizar la operacion resto entre los numeros dados en la entrada.

    """
    # Cambiar nombre

    def reduccion (self, n, c):

        bin_c = bin(c)[2:]
        limite = 1 << (len(bin_c)-1)

        while n >= limite:
            x = len(bin(n))-2
            n = n ^ (c << (x-len(bin_c)))
        return n

#-------------------------------------------------------------------------------------------------------------------------

    """
        FUNCIÓN inversor(n, c)
        -----------------------------------

        Función que mediante el algoritmo extendido de Euclides, nos devuelve el inverso de un número. 

        ENTRADA: Dos enteros (n, c).
        SALIDA: Un numero entero que representa al inverso de los dos números dados en la entrada.

    """

    def inversor(self, n, c):
        
            a, b = n, c
            u, v = 1, 0

            if a > b:
                a,b = b,a

            while a != 1:
                j = len(bin(a))-len(bin(b)) 
                if j < 0:
                    a, b, u, v, j = b, a, v, u, -j
                
                a = a ^ (b << j)
                u = u ^ (v << j)
            
            return u
            

#-------------------------------------------------------------------------------------------------------------------------

    def division(self, a, b, c):
        temp = self.inversor(b, c)
        resultado = self.multiplicacion(a, temp)
        res = self.reduccion(resultado,c)
        return res

    