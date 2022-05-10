sum = 0
count = 0
for c in range(1, 7):
    number = int(input('Enter a number: '))
    if number % 2 == 0:
        sum += number
        count += 1
print(count, sum)
