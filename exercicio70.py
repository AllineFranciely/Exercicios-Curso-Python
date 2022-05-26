total = 0
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço do produto: '))
    total += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de {total:10.2f}')