def somarNumeros(numeros):
    
    if not numeros:
        return 0
    else:
        return numeros[0] + somarNumeros(numeros[1: ])
    
listaNumeros = []

while True:

    listaInput = int(input("Adicione um número na lista ou digite 0 para não adicionar: "))

    if listaInput == 0:
        break
    
    listaNumeros.append(listaInput)

resultado = somarNumeros(listaNumeros)

print("A soma de todos os núemros da lista ", listaNumeros, " é: ", resultado)