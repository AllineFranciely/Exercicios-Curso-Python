print('Gerador de PA')
print('-=' * 10)
number = int(input('Digite o número: '))
razão = int(input('Qual a razão? '))
termo = number
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
print('FIM')