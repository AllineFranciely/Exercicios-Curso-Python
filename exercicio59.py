number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))
option = 0
while option != 5:
    print(''' O que deseja fazer?
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa ''')
    option = int(input('Digite a opção: '))
    if option == 1:
        sum = number1 + number2
        print('A soma dos valores é {}'.format(sum))
    elif option == 2:
        mult = number1 * number2
        print('A multiplicação dos valores é {}'.format(mult))
    elif option == 3:
       if number1 > number2:
           maior = number1
       else:
           maior = number2
       print('O maior valor é {}'.format(maior))
    elif option == 4:
        print('Informe os números novamente')
        number1 = int(input('Digite um número: '))
        number2 = int(input('Digite outro número: '))
    elif option == 5:
        print('Finalizando')
    else:
        print('Opção inválida')
print('Fim do programa')
