def esfera(raio):
    volume = (4/3.0) * 3.14159 * raio**3
    return volume

resultado = esfera(float(input()))
print(f'VOLUME = {resultado:.3f}')