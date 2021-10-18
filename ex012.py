preço = float(input("Qual o preço do produto ? R$ "))
desconto = (preço * 5) / 100
preçocomdesconto = preço - desconto
print("O produto com 5% de desconto é R${:.2f} ".format(preçocomdesconto))
