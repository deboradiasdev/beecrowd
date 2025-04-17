class Criptografia:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def passo1(self, texto):
    # Verifica caractere e desloca letras3 posições a direita na tabela ASCII
        resultado = ""
        for caractere in texto:
            if caractere.isalpha():
                resultado += chr(ord(caractere) + 3)
            else:
                resultado += caractere
        return resultado
    
    def passo2(self, texto):
        # Inverte a string
        return texto[::-1]

    def passo3(self, texto):
        # Parte a string na metade e desloca essa metade para a esquerda
        metade = len(texto) // 2
        primeira_metade = texto[:metade]

        segunda_metade = []
        for caractere in texto[metade:]:
            if caractere.isalpha():
                novo_caractere = chr(ord(caractere)-1)
                segunda_metade.append(novo_caractere)
            else:
                segunda_metade.append(caractere)

        segunda_metade = ''.join(segunda_metade)
        return primeira_metade + segunda_metade

    def criptografar(self):
    # Executa todos os passos da classe

        etapa1 = self.passo1(self.mensagem)
        etapa2 = self.passo2(etapa1)
        final = self.passo3(etapa2)

        return final

# Ler o número de mensagens
qtd = int(input())

for _ in range(qtd):
    mensagem = input()
    criptografia = Criptografia(mensagem)
    resultado = criptografia.criptografar()
    print(resultado)