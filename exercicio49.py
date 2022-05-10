number = int(input('De qual número você quer saber a tabuada? '))
multiplicador = 0

for multiplicador in range(0, 11):
    print('{} X {:2} = {}'. format(number, multiplicador, number * multiplicador))
    multiplicador = multiplicador + 1