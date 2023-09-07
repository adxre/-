#Рабочая Тетрадь 1 Задание 4.3.5
#Задание:Создайте простейший калькулятор, включающий основные действия
#для двух переменных ′ + ′, ′ − ′, ′ ∙ ′, ′ ÷ ′, а также вычисление следующих функций:e^x+y,cos(x+y),sin(x+y),x^y
import tkinter as tk
import math

def calculate():
    try:
        x = float(entry_x.get())
        y = float(entry_y.get())
        
        operation = operation_var.get()
        
        if operation == "+":
            result = x + y
        elif operation == "-":
            result = x - y
        elif operation == "*":
            result = x * y
        elif operation == "/":
            if y == 0:
                result = "Ошибка: деление на ноль"
            else:
                result = x / y
        elif operation == "e^x+y":
            result = math.exp(x + y)
        elif operation == "cos(x+y)":
            result = math.cos(x + y)
        elif operation == "sin(x+y)":
            result = math.sin(x + y)
        elif operation == "x^y":
            result = x ** y
        else:
            result = "Неизвестная операция"
        
        result_label.config(text="Результат: " + str(result))
    except ValueError:
        result_label.config(text="Ошибка: Введите числовые значения")
    

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор")

# Поле для ввода переменных
entry_x = tk.Entry(root, width=10)
entry_x.pack()
entry_y = tk.Entry(root, width=10)
entry_y.pack()

# Выбор операции
operation_var = tk.StringVar()
operations = ["+", "-", "*", "/", "e^x+y", "cos(x+y)", "sin(x+y)", "x^y"]
operation_var.set("+")  # Значение по умолчанию
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.pack()

# Кнопка для выполнения вычислений
calculate_button = tk.Button(root, text="Вычислить", command=calculate)
calculate_button.pack()

# Отображение результата
result_label = tk.Label(root, text="")
result_label.pack()

# Запуск GUI
root.mainloop()
