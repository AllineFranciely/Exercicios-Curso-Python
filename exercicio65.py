sum = quant = media = maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    num = int(input('Digite um número: '))
    sum += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
media = sum / quant
print('Você digitou {} numeros, a media foi {}, o maior número foi {} e o menor numero foi {}'.format(quant, media, maior, menor))

