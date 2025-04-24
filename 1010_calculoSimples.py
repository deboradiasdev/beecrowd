''' Neste problema, deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça 1, o código de uma peça 2,
    o número de peças 2 e o valor unitário de cada peça 2. Após, calcule e mostre o valor a ser pago.

    Entrada
    O arquivo de entrada contém duas linhas de dados. Em cada linha haverá 3 valores, respectivamente dois inteiros e um valor com 2 casas decimais.
    
    Saída
    A saída deverá ser uma mensagem conforme o exemplo fornecido abaixo, lembrando de deixar um espaço após os dois pontos e um espaço após o "R$".
    O valor deverá ser apresentado com 2 casas após o ponto.'''
def calcularPecas (codigoPeca, numPecas, valor):
    total = numPecas * valor
    return total

peca_1 = calcularPecas(int(input()), int(input()), float(input()))
peca_2 = calcularPecas(int(input()), int(input()), float(input()))
print(f'VALOR A PAGAR: R$ {peca_1 + peca_2:.2f}')

#outra forma de fazer

peca1 = input().split()
peca2 = input().split()
total = (int(peca1[1]) * float(peca1[2])) + (int(peca2[1]) * float(peca2[2]))
print(f'VALOR A PAGAR: R$ {total:.2f}')