#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

name = str(input('Qual seu nome completo?')).strip()
print('Analisando seu nome')
print('Seu nome é {}'.format(name))
upperName = name.upper()
print('Seu nome em maiúsculas é {}'.format(upperName))
lowerName = name.lower()
print('Seu nome em minúsculas é {}'.format(lowerName))
lenName = len(name) - name.count(' ')
print('Seu nome tem {} letras'.format(lenName))
#lenFirstName = name.find(' ')
#print(l'Seu primeiro nome tem {} letras'.format(lenFirstName))
separetedName = name.split()
print(separetedName)
print('Seu primeiro nome tem {} letras'.format(len(separetedName[0])))
