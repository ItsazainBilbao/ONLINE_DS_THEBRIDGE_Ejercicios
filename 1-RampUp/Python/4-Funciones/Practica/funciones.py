import math

def area_cuadrado(a, b = None):
    if(b== None):
        return a**2
    else:
        return a*b

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_circulo(radio):
    return math.pi*(radio**2)