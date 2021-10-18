km = float(input("Quantos km você rodou com o carro alugado ? "))
dias = float(input("Por quantos dias você alugou o carro ? "))
km2 = ( km * 0.15 )
dias2 = dias * 60
total = km2 + dias2
print(" Você deve pagar R${:.2f} pelo dias que alugou, e R${:.2f} pelos kilometros rodados com o carro ! \n O total a pagar é {:.2f} ".format(dias2, km2, total))

