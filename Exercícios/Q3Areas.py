import math


def area_triangulo(base, altura):
    return (base * altura) / 2
def area_quadrado(lado):
    return lado ** 2
def area_retangulo(base, altura):
    return base * altura
def area_circulo(raio):
    return math.pi * raio ** 2
def area_trapezio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2
def area_losango(diagonal_maior, diagonal_menor):
    return (diagonal_maior * diagonal_menor) / 2

print("Área do triângulo:", area_triangulo(5, 4))
print("Área do quadrado:", area_quadrado(5))
print("Área do retângulo:", area_retangulo(6, 4))
print("Área do círculo:", area_circulo(3))
print("Área do trapézio:", area_trapezio(6, 4, 3))
print("Área do losango:", area_losango(8, 6))
