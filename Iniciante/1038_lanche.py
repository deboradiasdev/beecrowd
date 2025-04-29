''' Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item.
    A seguir, calcule e mostre o valor da conta a pagar.
    | Código |  Especificação   |   Preço   |
    =========================================
    |   1    |  Cachorro-Quente |   R$ 4.00 |
    |   2    |  X-Salada        |   R$ 4.50 |
    |   3    |  X-Bacon         |   R$ 5.00 |
    |   4    |  Torrada Simples |   R$ 2.00 |
    |   5    |  Refrigerante    |   R$ 1.50 |
    
    Entrada
    O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

    Saída
    O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.'''

ref_codigo = {
    1: {'produto': 'Cachorro-Quente', 'preco': 4.00},
    2: {'produto': 'X-Salada', 'preco': 4.50},
    3: {'produto': 'X-bacon', 'preco': 5.00},
    4: {'produto': 'Torrada Simples', 'preco': 2.00}, 
    5: {'produto': 'Refrigerante', 'preco': 1.50}
}

codigo, quantidade = map(int, input().split())

item = ref_codigo[codigo]
preco = item['preco']
total = preco * quantidade

print(f'Total: R$ {total:.2f}')