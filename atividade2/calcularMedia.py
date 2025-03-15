#Função que calucla a média
def calcular_media(notas):
   
   #Awui é armazenado um valor para a soma, assim no loop for cada valor de nota será adicionado aqui
    soma = 0

    for nota in notas:
        soma += nota 

        media = soma / 5 

    return media
