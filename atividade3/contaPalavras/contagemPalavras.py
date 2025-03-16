#função que conta palavras

def contar_palavras(texto):

    contagem = 0

    #método que separa as palvras e as conta, adicionando elas no dicionário
    for palavra in texto.split(" "):
        contagem += 1

    return contagem

texto = input("Escreva uma frase ou um texto: ")

resultado = contar_palavras(texto)

print("O número de palavras é: ", resultado)