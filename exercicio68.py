from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computados jogou {computador} Total de {total} ', end = '')
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 != 0:
            print('Você venceu!!')
            v += 1
        else:
            print('Você perdeu')
            break
print(f'GAME OVER. Você vender {v} vezes.')