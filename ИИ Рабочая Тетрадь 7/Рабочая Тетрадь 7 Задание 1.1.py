class NeuralNetwork1:
    def __init__(self):
        # Инициализация весов и порогов
        self.weights = [0.5, 0.5, 0.5]
        self.bias = 0

    def feedforward(self, inputs):
        # Считаем взвешенную сумму входов и применяем функцию активации (линейную)
        total = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return total

# Пример использования
nn1 = NeuralNetwork1()
inputs1 = [0.2, 0.4, 0.6]
output1 = nn1.feedforward(inputs1)
print("Output for Neural Network 1:", output1)
