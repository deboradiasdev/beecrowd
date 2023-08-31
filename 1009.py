nomeVendedor = input()
salarioFixo = float(input())
totalVendasMes = float(input())

totalSalario = (totalVendasMes * 0.15) + salarioFixo
print(f'TOTAL = R$ {totalSalario:.2f}')