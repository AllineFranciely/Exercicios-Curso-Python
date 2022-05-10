from math import hypot
CO = float(input('Comprimento do cateto oposto:'))
CA = float(input('Comprimento do cateto adjacente:'))
H = hypot(CO, CA)
print('A hipotenusa mede {:.2f}'.format(H))
