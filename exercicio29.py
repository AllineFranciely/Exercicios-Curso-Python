velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
if velocidade <= 80:
    print('Está liberado')
else:
    print('Você foi multado em R$ {:.2f}'.format(multa))
