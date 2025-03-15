#função que conta palavras

def contar_palavras(texto):

    texto = texto.lower()

    contagem = {}

    for palavra in texto.split(" "):
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem