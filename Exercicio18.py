import math
ângulo = float(input('Digite um ângulo:'))
anguloRad = math.radians(ângulo)
seno = math.sin(anguloRad)
print('O valor do SENO do ângulo {} é {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('O valor do COSSENO do ângulo {} é {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O valor da TANGENTE do ângulo {} é {:.2f}'.format(ângulo, tangente))

