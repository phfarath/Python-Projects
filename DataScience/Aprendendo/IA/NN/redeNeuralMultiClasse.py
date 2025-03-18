import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

np.random.seed(237)

# 1. Carregar o dataset Iris (3 tipos de flores, 4 características)
iris = datasets.load_iris()
X = iris.data  # 4 características (ex: comprimento e largura das pétalas)
y = iris.target.reshape(-1, 1)  # 3 classes (0, 1, 2)

# 2. Transformar os rótulos em One-Hot Encoding (0 -> [1,0,0], 1 -> [0,1,0], 2 -> [0,0,1])
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# 3. Dividir os dados em treino e teste (80% treino, 20% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=237)

# 4. Criar a Rede Neural Multiclasse
class NeuralNetworkMulticlass:
    def __init__(self, n_inputs, n_hidden, n_outputs, learning_rate=0.01, epochs=5000):
        np.random.seed(237)
        self.weights_hidden = np.random.rand(n_inputs, n_hidden)
        self.bias_hidden = np.random.rand(n_hidden)
        self.weights_output = np.random.rand(n_hidden, n_outputs)
        self.bias_output = np.random.rand(n_outputs)
        self.learning_rate = learning_rate
        self.epochs = epochs

    def softmax(self, x):
        """Função de ativação para classificação multiclasse"""
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))  # Estabilização numérica
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def predict(self, X):
        hidden_input = np.dot(X, self.weights_hidden) + self.bias_hidden
        hidden_output = self.sigmoid(hidden_input)
        final_input = np.dot(hidden_output, self.weights_output) + self.bias_output
        final_output = self.softmax(final_input)
        return np.argmax(final_output, axis=1)  # Retorna a classe com maior probabilidade

    def train(self, X, y):
        for epoch in range(self.epochs):
            # Forward Pass
            hidden_input = np.dot(X, self.weights_hidden) + self.bias_hidden
            hidden_output = self.sigmoid(hidden_input)
            final_input = np.dot(hidden_output, self.weights_output) + self.bias_output
            final_output = self.softmax(final_input)

            # Calcular erro
            error = y - final_output

            # Backpropagation
            d_output = error
            d_hidden = np.dot(d_output, self.weights_output.T) * self.sigmoid_derivative(hidden_output)

            lambda_reg = 0.004  # Define a intensidade da regularização

            # Atualizar pesos e bias
            self.weights_output += self.learning_rate * np.dot(hidden_output.T, d_output)
            self.bias_output += self.learning_rate * np.sum(d_output, axis=0)
            self.weights_output -= lambda_reg * self.weights_output  # Regularização

            self.weights_hidden += self.learning_rate * np.dot(X.T, d_hidden)
            self.bias_hidden += self.learning_rate * np.sum(d_hidden, axis=0)
            self.weights_hidden -= lambda_reg * self.weights_hidden  # Regularização

            # Mostrar erro a cada 1000 épocas
            if epoch % 1000 == 0:
                print(f"Época {epoch}, Erro médio: {np.mean(np.abs(error))}")

# 5. Treinar a rede neural
nn = NeuralNetworkMulticlass(n_inputs=4, n_hidden=10, n_outputs=3, learning_rate=0.01, epochs=10000)
nn.train(X_train, y_train)

# 6. Testar a rede neural
print("\nTestando previsões:")
predictions = nn.predict(X_test)
true_labels = np.argmax(y_test, axis=1)
accuracy = np.mean(predictions == true_labels)
print(f"Acurácia no conjunto de teste: {accuracy * 100:.2f}%")

# 7. Testar com novas amostras (medidas fictícias de flores)
novas_flores = np.array([
    [5.1, 3.5, 1.4, 0.2],  # Provavelmente Setosa (0)
    [6.1, 2.8, 4.7, 1.2],  # Provavelmente Versicolor (1)
    [6.9, 3.1, 5.4, 2.1]   # Provavelmente Virginica (2)
])

# Fazer previsões
predicoes = nn.predict(novas_flores)

# Exibir resultados
print("\nPrevisões para novas amostras:")
for i, pred in enumerate(predicoes):
    print(f"Amostra {i+1}: Classe prevista -> {pred}")