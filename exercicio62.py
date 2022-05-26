print('Gerador de PA')
print('-=' * 10)
number = int(input('Digite o número: '))
razão = int(input('Qual a razão? '))
termo = number
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja mostrar? '))
print('FIM')