#Рабочая тетрадь 1 Задание 2.3
#Задание: Написать код. Задается X,напечатать к какому из интервалов принадлежит : (-infinity,-5),[-5,5] или от(5,+infinity)
import math
test = math.inf
test1 = -test
x = float(input())
if  test1 < x < 5:
    print(f'{x}, принадлежит интервалу (-infinity,-5)')
elif -5 <= x <= 5:
    print(f'{x}, принадлежит интервалу [-5,5]')
else:
    print(f'{x}, принадлежит интервалу (5,+infinity)')
    


