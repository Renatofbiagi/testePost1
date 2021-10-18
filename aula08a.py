import math
num = int(input("Digite um número : "))
raiz = math.sqrt(num)
print("A raiz quadrada de {} é {} , ( sem aredondar ) ".format(num, raiz))
print("A raiz quadrada de {} é {} , ( aredondada pra cima ) ".format(num, math.ceil(raiz)))
print("A raiz quadrada de {} é {} , ( aredondada pra baixo ) ".format(num, math.floor(raiz)))
