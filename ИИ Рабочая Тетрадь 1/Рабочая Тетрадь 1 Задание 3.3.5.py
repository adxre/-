#Рабочая Тетрадь 1 Задание 3.3.5
#Задание: Срез. Напишите код, который все элементы массива x с четными
#индексами переставит в обратном порядке. Т.е. если x = [0, 1, 2, 3, 4,
#5, 6, 7, 8, 9], то код должен сформировать [8, 1, 6, 3, 4, 5, 2, 7, 0, 9].

a = [0,1,2,3,4,5,6,7,8,9]

x = a[::-2][::-1]

for i,y in enumerate(x):
    a[i*2] = y

print(a)