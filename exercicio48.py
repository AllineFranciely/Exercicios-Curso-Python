sum = 0
count = 0
for number in range(1, 501, 2):
    if number % 3 == 0:
      sum = sum + number
      count = count + 1
print('Existem {} números múltiplos de 3 nesse intervalo /n'
      'e a soma deles é {}' .format(count, sum))
