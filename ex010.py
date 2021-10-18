real = float(input("Quantos de dinheiro você tem ? R$ "))
dolar = real / 5.51
euro = real / 6.38
print("Com R${:.2f}, você pode comprar : \n Dolares : U$ {:.2f} \n Euros : {:.2f}".format(real, dolar, euro))

