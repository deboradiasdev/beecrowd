''' Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário.
    A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto.
    As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01.
    A seguir mostre a relação de notas necessárias.

    Entrada
    O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

    Saída
    Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.

    Obs: Utilize ponto (.) para separar a parte decimal.'''
valor = float(input())

cedulas = (100, 50, 20, 10, 5, 2)
moedas = (1, 0.50, 0.25, 0.10, 0.05, 0.01)

def calcularNotas(valor):
    restante = valor
    print('NOTAS:')
    for cedula in cedulas:
        quantidade_cedula = int(restante // cedula)
        print(f'{quantidade_cedula} nota(s) de R$ {cedula:.2f}')
        restante = restante % cedula
    return restante

def calcularMoedas(valor):
    restante = int(round(valor * 100))

    print('MOEDAS:')
    moedas_centavos = (100, 50, 25, 10, 5, 1)
    valores_moedas = (1.00, 0.50, 0.25, 0.10, 0.05, 0.01)

    for i in range(len(moedas_centavos)):
        quantidade_moedas = restante // moedas_centavos[i]
        print(f'{quantidade_moedas} moeda(s) de R$ {valores_moedas[i]:.2f}')
        restante = restante % moedas_centavos[i]

restante = calcularNotas(valor)
calcularMoedas(restante)
