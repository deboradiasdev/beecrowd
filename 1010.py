def calcularPecas (codigoPeca, numPecas, valor):
    total = numPecas * valor
    return total

peca_1 = calcularPecas(int(input()), int(input()), float(input()))
peca_2 = calcularPecas(int(input()), int(input()), float(input()))
print(f'VALOR A PAGAR: = {peca_1 + peca_2:.2f}')