#função que conta palavras

def contar_palavras(texto):

    #função que transforma tudo em minúsculo
    texto = texto.lower()

    #dicionário
    contagem = {}

    #método que separa as palvras e as conta, adicionando elas no dicionário
    for palavra in texto.split(" "):
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem