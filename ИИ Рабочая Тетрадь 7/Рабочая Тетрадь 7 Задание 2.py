import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        self.weights_input_hidden = np.random.randn(input_size, hidden_size)
        self.bias_input_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.randn(hidden_size, output_size)
        self.bias_hidden_output = np.zeros((1, output_size))

    def forward(self, inputs):
        # Прямое распространение сигнала
        self.inputs = inputs
        self.hidden_input = np.dot(inputs, self.weights_input_hidden) + self.bias_input_hidden
        self.hidden_output = self.activation(self.hidden_input)
        self.final_input = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_hidden_output
        self.final_output = self.activation(self.final_input)
        return self.final_output

    def activation(self, x):
        # В этом базовом классе используется линейная активация (подклассы переопределят этот метод)
        return x

    def backward(self, d_output, learning_rate):
        # Обратное распространение ошибки
        d_final_input = d_output * self.activation_derivative(self.final_input)
        d_hidden_output = np.dot(d_final_input, self.weights_hidden_output.T)
        d_hidden_input = d_hidden_output * self.activation_derivative(self.hidden_input)

        # Обновление весов и смещений
        self.weights_hidden_output -= np.dot(self.hidden_output.T, d_final_input) * learning_rate
        self.bias_hidden_output -= np.sum(d_final_input, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden -= np.dot(self.inputs.T, d_hidden_input) * learning_rate
        self.bias_input_hidden -= np.sum(d_hidden_input, axis=0, keepdims=True) * learning_rate

    def activation_derivative(self, x):
        # Производная функции активации (подклассы переопределят этот метод)
        return 1

class LeakyReLU_NeuralNetwork(NeuralNetwork):
    def activation(self, x):
        return np.where(x > 0, x, 0.01 * x)  # 0.01 - коэффициент утечки

    def activation_derivative(self, x):
        return np.where(x > 0, 1, 0.01)


class SoftmaxActivation(NeuralNetwork):
    def activation(self, z):
        # Рассчитываем softmax для входного вектора z
        exp_z = np.exp(z - np.max(z))  # Вычитаем максимальное значение для стабильности
        softmax = exp_z / exp_z.sum(axis=0, keepdims=True)
        return softmax

    def deractive_activation(self, z):
        pass

# Пример использования
input_size = 3 # Пример размера входных данных для нейронной сети MNIST
hidden_size = 4
output_size = 2 

softmax_network = SoftmaxActivation(input_size,hidden_size,output_size)
leaky_relu = LeakyReLU_NeuralNetwork(input_size,hidden_size,output_size)

inputs = np.array([0.5, -0.2, 0.1])
output_softmax = softmax_network.forward(inputs)
output_relu = leaky_relu.forward(inputs)

print("softmax activation output:",output_softmax)
print("Leaky ReLu activation output:",output_relu)
