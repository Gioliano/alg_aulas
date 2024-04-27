def soma_lista_recursiva(lista, indice):
    if indice == len(lista):
        # Retorna 0 caso o índice atinja o final da lista
        return 0  
    else:
        # retorna a soma do elemento atual com a chamada recursiva para o próximo índice
        return lista[indice] + soma_lista_recursiva(lista, indice + 1)  

# Criando a lista
minhalista = []
tam = 5
for i in range(tam):
    elemento = int(input("Entre com os elementos: "))
    minhalista.append(elemento)
    
print("A soma dos elementos da lista é:", soma_lista_recursiva(minhalista, 0))
