altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
área = largura * altura
tinta = área / 2
print('Para a pintar a parede de {}m² você utilizará {}l de tinta'.format(área, tinta))
