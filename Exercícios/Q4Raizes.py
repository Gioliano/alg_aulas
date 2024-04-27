import math

#x² – 4x + 4 = 0 --- a = 1, b = -4, c = 4
def calcular_raizes(a, b, c):
    # Calculando o delta
    delta = b**2 - 4*a*c
    
    # Verificando os deltas
    if delta >= 0:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        return raiz1, raiz2
    else:
        # Retorna None se as raízes forem complexas - esse caso não considerado! Tente fazer rsrs 
        return None  

# Recebendo os coeficientes do usuário
a = float(input("Digite o coeficiente  a: "))
b = float(input("Digite o coeficiente  b: "))
c = float(input("Digite o coeficiente  c: "))

# Calculando as raízes
raizes = calcular_raizes(a, b, c)
print(raizes)

