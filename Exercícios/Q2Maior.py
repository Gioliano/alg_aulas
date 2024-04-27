def encontrar_maior(lista):
    if len(lista) == 0:
        # retorna None se a lista estiver vazia
        return None  
    else:
        # indica que o primeiro elemento é o maior
        maior = lista[0]  
        for elemento in lista:
            if elemento > maior:
                maior = elemento
        return maior

#criando a lista
minhalista = []
tam = 5
for i in range(tam):
    elemento = int(input("Insira um elemento da lista: "))
    minhalista.append(elemento)

print("O maior elemento é:", encontrar_maior(minhalista))
