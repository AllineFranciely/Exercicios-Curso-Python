num = count = sum = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    count += 1
    sum += num
print(f'Você digitou {count} números e a soma entre eles é {sum}')