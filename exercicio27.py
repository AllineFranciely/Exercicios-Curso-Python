#Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

name = str(input('Digite seu nome completo: ')).strip()
separatedName = name.split()
print('Seu primeiro nome é {}'.format(separatedName[0]))
print('Seu último nome é {}'.format(separatedName[len(separatedName)-1]))
