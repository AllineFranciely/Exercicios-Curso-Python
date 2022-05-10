number = int(input('Digite um número inteiro qualquer: '))
print('''Escolha uma opção para conversão:
[ 1 ] para BINÁRIO
[ 2 ] para OCTAL
[ 3 ] para HEXADECIMAL ''')
option = int(input('Sua opção: '))
binario = bin(number)
octal = oct(number)
hexadecimal = hex(number)

if option == 1:
    print('O número {} em binário é {}'.format(number, binario))
elif option == 2:
    print('O número {} em octal é {}'.format(number, octal))
elif option == 3:
    print('O número {} em hexadecimal é {}'.format(number, hexadecimal))