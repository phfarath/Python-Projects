import numpy as np

import numpy as np

class NeuralNetwork:
    def __init__(self, learning_rate=0.01, epochs=10000):
        # Pesos e bias para a camada oculta (2 neurônios)
        self.weights_hidden = np.random.rand(2, 4)  # 2 entradas, 2 neurônios na camada oculta
        self.bias_hidden = np.random.rand(4)  

        # Pesos e bias para a camada de saída (1 neurônio)
        self.weights_output = np.random.rand(4, 1)  # Corrigido para matriz (2,1)
        self.bias_output = np.random.rand(1)  

        # Parâmetros de treinamento
        self.learning_rate = learning_rate  
        self.epochs = epochs  

    # funções de ativação
    # SIGMOID
    def sigmoid(self, x):
        """Função de ativação sigmóide."""
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        """Derivada da sigmóide para ajustar os pesos."""
        return x * (1 - x)

    # RELU
    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return np.where(x > 0, 1, 0)
    #📌 Vantagens:
    #✅ Resolve o problema do vanishing gradient da sigmóide.
    #✅ É mais eficiente para redes mais profundas.

    # TANH
    def tanh(self, x):
        return np.tanh(x)

    def tanh_derivative(self, x):
        return 1 - np.tanh(x) ** 2
    # 📌 Vantagens:
    # ✅ Retorna valores entre -1 e 1, sendo útil para normalização.
    # ✅ Pode aprender mais rápido que sigmóide.

    def predict(self, X):
        """Faz previsões para uma entrada X e arredonda para 0 ou 1."""
        hidden_input = np.dot(X, self.weights_hidden) + self.bias_hidden  
        hidden_output = self.tanh(hidden_input)  

        final_input = np.dot(hidden_output, self.weights_output) + self.bias_output  
        final_output = self.tanh(final_input)  

        return np.round(final_output)  # Arredonda para 0 ou 1

    def train(self, X, y):
        """Treina a rede neural."""
        for epoch in range(self.epochs):
            # Forward Pass
            hidden_input = np.dot(X, self.weights_hidden) + self.bias_hidden  
            hidden_output = self.tanh(hidden_input)  

            final_input = np.dot(hidden_output, self.weights_output) + self.bias_output  
            final_output = self.tanh(final_input)  

            # Calcular erro
            error = y - final_output  

            # Backpropagation (Ajuste dos pesos)
            d_output = error * self.tanh_derivative(final_output)  
            d_hidden = np.dot(d_output, self.weights_output.T) * self.tanh_derivative(hidden_output)

            lambda_reg = 0.001  # Define a intensidade da regularização (IDEAL -> learning_rate / 10)

            # Atualização dos pesos e bias
            self.weights_output += self.learning_rate * np.dot(hidden_output.T, d_output)
            self.bias_output += self.learning_rate * np.sum(d_output, axis=0)
            self.weights_output -= lambda_reg * self.weights_output  # Regularização

            self.weights_hidden += self.learning_rate * np.dot(X.T, d_hidden)
            self.bias_hidden += self.learning_rate * np.sum(d_hidden, axis=0)
            self.weights_hidden -= lambda_reg * self.weights_hidden  # Regularização

            # Exibir erro a cada 1000 épocas
            if epoch % 1000 == 0:
                print(f"Época {epoch}, Erro médio: {np.mean(np.abs(error))}")

# Dados de entrada (X1, X2) e saída esperada (XOR)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([[0], [1], [1], [0]])  # Saídas esperadas para XOR

# Criar e treinar a rede neural
nn = NeuralNetwork(learning_rate=0.1, epochs=10000)
nn.train(X, y)

# Testar a rede neural após o treinamento
print("\nTestes XOR:")
for inputs in X:
    print(f"Entrada: {inputs}, Previsão: {nn.predict(inputs)}")
