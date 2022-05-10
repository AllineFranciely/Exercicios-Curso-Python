import math
num = float(input('Digite um número:'))
numInt = math.floor(num)
print(numInt)

num2 = float(input('Digite outro número:'))
print('Número digitado: {}; Parte inteira: {}'.format(num2, math.trunc(num2)))

