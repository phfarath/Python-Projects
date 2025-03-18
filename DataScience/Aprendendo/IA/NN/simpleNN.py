import numpy as np

# Criar dataset: horas de estudo e notas esperadas
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]])  # Horas de estudo
y = np.array([[2], [3], [5], [6], [8], [10], [12], [14], [16], [18]])  # Notas obtidas

# Criar a rede neural
class SimpleNN:
    def __init__(self, learning_rate=0.001, epochs=10000):
        self.weight = np.random.rand(1, 1)
        self.bias = np.random.rand(1)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return x  # Função identidade (para regressão)

    def activation_derivative(self, x):
        return 1  # Derivada da função identidade

    def predict(self, X):
        return self.activation(np.dot(X, self.weight) + self.bias)

    def train(self, X, y):
        for epoch in range(self.epochs):
            output = self.predict(X)
            error = y - output

            # Ajuste dos pesos
            d_weight = np.dot(X.T, error) / len(X)
            d_bias = np.sum(error) / len(X)

            lambda_reg = 0.0001  # Define a intensidade da regularização (IDEAL -> learning_rate / 10)

            self.weight += self.learning_rate * d_weight
            self.bias += self.learning_rate * d_bias
            self.weight -= lambda_reg * self.weight  # Regularização

            if epoch % 1000 == 0:
                print(f"Época {epoch}, Erro médio: {np.mean(np.abs(error))}")

# Treinar o modelo
nn = SimpleNN(learning_rate=0.01, epochs=5000)
nn.train(X, y)

# Testar previsões
print("\nTestando previsões:")
test_data = np.array([[11], [12], [13]])
print(nn.predict(test_data))
