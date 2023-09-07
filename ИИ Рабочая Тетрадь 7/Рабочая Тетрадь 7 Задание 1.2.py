class NeuralNetwork2:
    def __init__(self):
        # Инициализация весов и порогов
        self.weights = [1, 0]
        self.bias = 1

    def feedforward(self, inputs):
        # Считаем взвешенную сумму входов и применяем функцию активации (линейную)
        total = sum(w * x for w, x in zip(self.weights, inputs)) + self.bias
        return total

# Пример использования
nn2 = NeuralNetwork2()
inputs2 = [0.8, 0.6]
output2 = nn2.feedforward(inputs2)
print("Output for Neural Network 2:", output2)
