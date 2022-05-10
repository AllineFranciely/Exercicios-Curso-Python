salario = float(input('Digite o salário: '))

if salario > 1250:
    aumento = (10 * salario) / 100
else:
    aumento = (15 * salario) / 100

novoSalario = salario + aumento

print('Você recebeu um aumento de R${} e seu novo salário é de R$ {}'.format(aumento, novoSalario))
