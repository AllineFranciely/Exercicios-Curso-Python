numberOne = int(input('Digite um número: '))
numberTwo = int(input('Digite outro número: '))
numberThree = int(input('Digite outro número: '))

maior = 0
menor = 0

if numberOne == numberTwo or numberOne == numberThree or numberTwo == numberThree:
    print('Você digitou números iguais')
else:
    if numberOne > numberTwo and numberOne > numberThree and numberTwo < numberThree:
        maior += numberOne
        menor += numberTwo
    elif numberTwo > numberOne and numberTwo > numberThree and numberThree < numberOne:
        maior += numberTwo
        menor += numberThree
    elif numberThree > numberTwo and numberThree > numberOne and numberOne < numberTwo:
        maior += numberThree
        menor += numberOne
    print('O maior valor digitado é {} e o menor é {}'.format(maior, menor))
