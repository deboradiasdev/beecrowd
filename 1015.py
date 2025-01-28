pontos = []

pontos.append([float(input()), float(input())])
pontos.append([float(input()), float(input())])

x1, y1 = pontos[0]
x2, y2 = pontos[1]

distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print(f'{distancia:.4f}')


