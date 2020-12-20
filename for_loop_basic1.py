#imprimir todos los enteros del 0 al 150
# for i in range(151):
#     print(i)

#imprimir todos los multimplos de 5 de 5 a 1000
# for x in range(5,1000,5):
#     print(x)

#imprimir enteros del 1 al 100, si es divisible por 5 imprima "codificación" en su lugar. Si es divisible por 10 que imprima "Coding Dojo"
# for c in range(101):
#     if c%10 == 0:
#         c = "Coding Dojo"
#     elif c%5 == 0:
#         c = "codificacion"
#     print(c)

#agregar los enteros impares de 0 a 500.000, imprimir la suma final

# sum_impar = 0
# for num in range(500000):
#     if num%2 != 0:
#         sum_impar = sum_impar + num
# print("Woaaa!that sucker's HUGE!",sum_impar,"!!!!")

#Imprimir los numero positivos a partir del 2018, cuenta atras por 4
# for ano in range(2018,0,-4):
#     print(ano)

#establece tres variables: lowNum, highNum, mult. Comenzando en lowNum y pasando por highNum, imprima solo los enteros que son múltiplos de mult. Por ejemplo, si lowNum = 2, highNum = 9 y mult = 3, el bucle debe imprimir 3, 6, 9 (en líneas sucesivas)

lowNum = 5
highNum = 10
mult = 2

while highNum > lowNum:
    if highNum % mult == 0:
        print(highNum)
    highNum = highNum - 1