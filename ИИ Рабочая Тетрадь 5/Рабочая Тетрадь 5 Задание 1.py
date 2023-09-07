import math

class TrigonometryCalculator:
    @staticmethod
    def calculate_cosine(angle_in_degrees):
        """
        Вычисляет косинус угла в градусах.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        return math.cos(angle_in_radians)

    @staticmethod
    def calculate_sine(angle_in_degrees):
        """
        Вычисляет синус угла в градусах.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        return math.sin(angle_in_radians)

    @staticmethod
    def calculate_tangent(angle_in_degrees):
        """
        Вычисляет тангенс угла в градусах.
        """
        angle_in_radians = math.radians(angle_in_degrees)
        return math.tan(angle_in_radians)

    @staticmethod
    def calculate_arcsine(value):
        """
        Вычисляет арксинус заданного значения и возвращает результат в градусах.
        """
        angle_in_radians = math.asin(value)
        return math.degrees(angle_in_radians)

    @staticmethod
    def calculate_arccosine(value):
        """
        Вычисляет арккосинус заданного значения и возвращает результат в градусах.
        """
        angle_in_radians = math.acos(value)
        return math.degrees(angle_in_radians)

    @staticmethod
    def calculate_arctangent(value):
        """
        Вычисляет арктангенс заданного значения и возвращает результат в градусах.
        """
        angle_in_radians = math.atan(value)
        return math.degrees(angle_in_radians)

    @staticmethod
    def degrees_to_radians(degrees):
        """
        Переводит значение из градусов в радианы.
        """
        return math.radians(degrees)

# Пример использования класса:
angle_degrees = 45
calculator = TrigonometryCalculator()
print(f"Косинус {angle_degrees} градусов: {calculator.calculate_cosine(angle_degrees)}")
print(f"Синус {angle_degrees} градусов: {calculator.calculate_sine(angle_degrees)}")
print(f"Тангенс {angle_degrees} градусов: {calculator.calculate_tangent(angle_degrees)}")
print(f"Арксинус 0.5: {calculator.calculate_arcsine(0.5)} градусов")
print(f"Арккосинус 0.5: {calculator.calculate_arccosine(0.5)} градусов")
print(f"Арктангенс 1: {calculator.calculate_arctangent(1)} градусов")
print(f"{angle_degrees} градусов в радианах: {calculator.degrees_to_radians(angle_degrees)}")
