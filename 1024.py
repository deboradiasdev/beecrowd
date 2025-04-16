mensagem = input()
msg_criptografada = ""

#Verifica caractere e acrescenta 3 posições a direita na tabela ASCII
for caractere in mensagem:
    if caractere.isalpha():
        msg_criptografada += chr(ord(caractere) + 3)
    else:
        msg_criptografada += caractere

#Inverte a string
msg_criptografada = msg_criptografada[::-1]

#Parte a string na metade e desloca essa metade para a esquerda
metade = len(msg_criptografada) // 2
primeira_metade = msg_criptografada[:metade]

segunda_metade = []
for caractere in msg_criptografada[metade:]:
    if caractere.isalpha():
        novo_caractere = chr(ord(caractere)-1)
        segunda_metade.append(novo_caractere)
    else:
        segunda_metade.append(caractere)

segunda_metade = ''.join(segunda_metade)

msg_criptografada = primeira_metade + segunda_metade

print(msg_criptografada)