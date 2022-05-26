total18 = totalH = totalM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [F/M] ')).strip().upper()[0]
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalH += 1
    if sexo == 'F' and idade < 20:
        totalM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Total de homens: {totalH}')
print(f'Total de mulheres com menos de 20 anos: {totalM20}')