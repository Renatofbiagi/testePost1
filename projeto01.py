altura = float(input("Altura (m) : "))
peso = float(input("Peso (kg): "))
idade = float(input("Idade : "))
genero = int(input("Gênero : "))
imc = peso / ( altura ** 2 )
print("Seu imc é : {:.1f} ".format(imc))
if imc < 17:
    print("Você está muito abaixo do peso ")
elif 17 <= imc < 18.5:
    print("Você está na faixa de peso normal, Parabéns ! ")
elif 18.5 <= imc < 24.9:
    print("Você está abaixo do peso ")
elif 25 <= imc < 29.9:
    print("Você está acima do peso ")
elif 30 <= imc < 34.9:
    print("Você está em Obesidade 1 ")
atividade = float(input("Exercício físico , moderada ou  :"))
gastocaloriahomem = (10*peso)+(6.25*altura)-(5*idade)+5
gastocaloriamulher = (10*peso)+(6.25*altura)-(5*idade)-161
print("O gasto de calória é : {} ".format(gastodecaloria))
caloria = int(input("Quanto gasta de calória em média ( para homens ) por dia em repouso : "))
proteina = altura*2
lipidios = gastodecaloria/4
gastolipidios = lipidios/9
carboidrato = gastodecaloria-(proteina*4-gastolipidios*9)
carboidrato2 = carboidrato/4
print("Voce precisa de {} gramas de proteina para ganhar massa muscular ".format(proteina))
print("Você precisa de {} gramas de lipidios ".format(gastolipidios))
print("Você precisa de {} gramas de carboidratos ".format(carboidrato2))







