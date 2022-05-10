dist = float(input('Qual a distância a ser percorrida? '))
if dist <= 200:
    valor = 0.50 * dist
else:
    valor = 0.45 * dist

#valor = dist * 0.50 if dist <= 200 else dist * 0.45

print('O valor da viagem é de R$ {}'.format(valor))
