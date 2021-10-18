largura = float(input("Largura da parede : "))
altura = float(input("Altura da parede : "))
area = largura * altura
litrostinta = area / 2
print("Sua parede tem dimensão de {} x {}, e área de {}m2 \n Para pintar a parede, sendo que cada litro de tinta pinta 2 metros, você precisa de {} litros de tinta !".format(largura, altura, area, litrostinta))