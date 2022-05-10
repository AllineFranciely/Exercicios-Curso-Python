kms = float(input('Qual a quilometragem percorrida? '))
dias = int(input('Por quantos dias o carro foi alugado? '))
valor = (60 * dias) + (0.15 * kms)
print('O valor a pagar é {} '.format(valor))
