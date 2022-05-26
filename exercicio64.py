number = count = sum = 0
while number != 999:
    number = int(input('Digite um número: '))
    print('{}'.format(number))
    count += 1
    sum += number
print('Você digitou {} valores e a soma entre eles é {}'.format(count, sum))

