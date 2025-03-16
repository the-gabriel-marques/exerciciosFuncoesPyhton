def receberInfo(*args):
    return args

lista = []

while True:

    inserir = input("Insira qualquer informação que quiser, ou pression 's' para sair: ")

    if inserir == 's':
        break

    lista.append(inserir)

resultado = receberInfo(lista)

print("As informações que você digitou são: ", resultado)