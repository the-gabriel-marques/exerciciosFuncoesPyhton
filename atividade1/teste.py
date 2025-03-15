import contaPalavras

texto = "Python é uma linguagem de programação de alto nível, interpretada e de propósito geral. " \
"Criada por Guido van Rossum e lançada pela primeira vez em 1991, a filosofia do Python é enfatizar " \
"a legibilidade do código com sua sintaxe simples e fácil de aprender. A linguagem foi projetada com a " \
"filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. " \
"Prioriza a legibilidade do código sobre a velocidade ou expressividade. " \
"Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e " \
"frameworks desenvolvidos por terceiros. Python é uma linguagem de propósito geral de alto nível, multiparadigma, " \
"suporta o paradigma orientado a objetos, imperativo, funcional e procedural. " \
"Possui tipagem dinâmica e uma de suas principais características é permitir a fácil leitura do código e exigir poucas l" \
"inhas de código se comparado ao mesmo programa em outras linguagens."

resultado = contaPalavras.contar_palavras(texto)

print("Contagem de palavras: ", resultado)