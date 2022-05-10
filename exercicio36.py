valorCasa = float(input('Qual o valor da casa a ser financiada? '))
salário = float(input('Qual o valor do seu salário? '))
parcelas = int(input('Em quantas parcelas pretende pagar? '))
parcelas = valorCasa / parcelas
prestações = (salário * 30) / 100
print(prestações)

if parcelas > prestações:
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
