altura = float(input("Altura (m) : "))
peso = float(input("Peso (kg): "))
idade = float(input("Idade : "))
imc = peso / ( altura ** 2 )
print("Seu imc é : {:.1f} ".format(imc))
if imc < 17:
    print("Você está muito abaixo do peso ! ")
elif 17 <= imc < 18.5:
    print("Você está abaixo do peso ! ")
elif 18.5 <= imc < 24.9:
    print("Você está no peso normal, Parabens ! ")
elif 25 <= imc < 29.9:
    print("Você está acima do peso ")
elif 30 <= imc < 34.9:
    print("Você está em Obesidade 1 ")
elif 35 <= imc < 39.9:
    print("Você está em Obesidade 2 ( severa ) ")
elif imc >= 40:
    print("Você está em Obesidade 3 ( mórbida ) ")

