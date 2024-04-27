def logica(a,b):
    x = a and b
    y = a or b
    z = not a
    z1 = y != a
    return x, y, z, z1

a = True
b = False
resultado = logica(a,b)

print(resultado)