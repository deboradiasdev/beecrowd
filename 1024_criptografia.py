''' Solicitaram para que você construisse um programa simples de criptografia.
    Este programa deve possibilitar enviar mensagens codificadas sem que alguém consiga lê-las.
    O processo é muito simples. São feitas três passadas em todo o texto.

    Na primeira passada, somente caracteres que sejam letras minúsculas e maiúsculas devem ser deslocadas 3 posições para a direita,
    segundo a tabela ASCII: letra 'a' deve virar letra 'd', letra 'y' deve virar caractere '|' e assim sucessivamente. Na segunda passada,
    a linha deverá ser invertida. Na terceira e última passada, todo e qualquer caractere a partir da metade em diante (truncada)
    devem ser deslocados uma posição para a esquerda na tabela ASCII. Neste caso, 'b' vira 'a' e 'a' vira '`'.

    Por exemplo, se a entrada for “Texto #3”, o primeiro processamento sobre esta entrada deverá produzir “Wh{wr #3”.
    O resultado do segundo processamento inverte os caracteres e produz “3# rw{hW”. Por último, com o deslocamento dos caracteres da metade em diante,
    o resultado final deve ser “3# rvzgV”.

    Entrada
    A entrada contém vários casos de teste. A primeira linha de cada caso de teste contém um inteiro N (1 ≤ N ≤ 1*104),
    indicando a quantidade de linhas que o problema deve tratar. As N linhas contém cada uma delas M (1 ≤ M ≤ 1*103) caracteres.

    Saída
    Para cada entrada, deve-se apresentar a mensagem criptografada.'''
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

# Lê o número de mensagens
qtd = int(input())

for _ in range(qtd):
    mensagem = input()
    criptografia = Criptografia(mensagem)
    resultado = criptografia.criptografar()
    print(resultado)