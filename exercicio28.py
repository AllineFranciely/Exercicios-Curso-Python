#Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0, 5) # faz o computador pensar
print('Advinhe em qual número pensei entre 0 e 5')
pessoa = int(input('Digite um número'))
print('PROCESSANDO...')
sleep(2)
if pessoa == computador:
    print('Parabéns, você ganhou!!')
else:
    print('Que pena, você perdeu, eu pensei no número {}'.format(computador))
