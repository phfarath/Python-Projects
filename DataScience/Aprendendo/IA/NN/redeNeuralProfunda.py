import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder

np.random.seed(634)

# 1. Carregar o dataset Iris
iris = datasets.load_iris()
X = iris.data  # 4 características (ex: comprimento e largura das pétalas)
y = iris.target.reshape(-1, 1)  # 3 classes (0, 1, 2)

# 2. Transformar os rótulos em One-Hot Encoding (0 -> [1,0,0], 1 -> [0,1,0], 2 -> [0,0,1])
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y)

# 3. Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=237)

# 4. Criar a Rede Neural Profunda
class DeepNeuralNetwork:
    def __init__(self, n_inputs, n_hidden1, n_hidden2, n_outputs, learning_rate=0.01, epochs=5000):
        np.random.seed(634)
        # Pesos e bias para a primeira camada oculta
        self.weights_hidden1 = np.random.rand(n_inputs, n_hidden1)
        self.bias_hidden1 = np.random.rand(n_hidden1)

        # Pesos e bias para a segunda camada oculta
        self.weights_hidden2 = np.random.rand(n_hidden1, n_hidden2)
        self.bias_hidden2 = np.random.rand(n_hidden2)

        # Pesos e bias para a camada de saída
        self.weights_output = np.random.rand(n_hidden2, n_outputs)
        self.bias_output = np.random.rand(n_outputs)

        # Parâmetros de treinamento
        self.learning_rate = learning_rate
        self.epochs = epochs

    def softmax(self, x):
        """Função de ativação para saída multiclasse"""
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))  # Estabilização numérica
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def relu(self, x):
        """Função de ativação ReLU"""
        return np.maximum(0, x)

    def relu_derivative(self, x):
        """Derivada da ReLU para backpropagation"""
        return np.where(x > 0, 1, 0)

    def predict(self, X):
        """Faz previsões"""
        hidden_input1 = np.dot(X, self.weights_hidden1) + self.bias_hidden1
        hidden_output1 = self.relu(hidden_input1)

        hidden_input2 = np.dot(hidden_output1, self.weights_hidden2) + self.bias_hidden2
        hidden_output2 = self.relu(hidden_input2)

        final_input = np.dot(hidden_output2, self.weights_output) + self.bias_output
        final_output = self.softmax(final_input)

        return np.argmax(final_output, axis=1)

    def train(self, X, y):
        """Treina a Rede Neural Profunda"""
        for epoch in range(self.epochs):
            # Forward Pass (Propagação para frente)
            hidden_input1 = np.dot(X, self.weights_hidden1) + self.bias_hidden1
            hidden_output1 = self.relu(hidden_input1)

            hidden_input2 = np.dot(hidden_output1, self.weights_hidden2) + self.bias_hidden2
            hidden_output2 = self.relu(hidden_input2)

            final_input = np.dot(hidden_output2, self.weights_output) + self.bias_output
            final_output = self.softmax(final_input)

            # Calcular erro
            error = y - final_output

            # Backpropagation (Ajuste dos Pesos)
            d_output = error
            d_hidden2 = np.dot(d_output, self.weights_output.T) * self.relu_derivative(hidden_output2)
            d_hidden1 = np.dot(d_hidden2, self.weights_hidden2.T) * self.relu_derivative(hidden_output1)

            lambda_reg = 0.0001  # Parâmetro de regularização

            # Atualizar pesos e bias
            self.weights_output += self.learning_rate * np.dot(hidden_output2.T, d_output)
            self.bias_output += self.learning_rate * np.sum(d_output, axis=0)
            self.weights_output -= lambda_reg * self.weights_output  # Regularização

            self.weights_hidden2 += self.learning_rate * np.dot(hidden_output1.T, d_hidden2)
            self.bias_hidden2 += self.learning_rate * np.sum(d_hidden2, axis=0)
            self.weights_hidden2 -= lambda_reg * self.weights_hidden2  # Regularização

            self.weights_hidden1 += self.learning_rate * np.dot(X.T, d_hidden1)
            self.bias_hidden1 += self.learning_rate * np.sum(d_hidden1, axis=0)
            self.weights_hidden1 -= lambda_reg * self.weights_hidden1  # Regularização

            # Mostrar erro a cada 3000 épocas
            if epoch % 3000 == 0:
                print(f"Época {epoch}, Erro médio: {np.mean(np.abs(error))}")

# 5. Treinar a DNN
dnn = DeepNeuralNetwork(n_inputs=4, n_hidden1=10, n_hidden2=10, n_outputs=3, learning_rate=0.0003, epochs=15000)
dnn.train(X_train, y_train)

# 6. Testar a Rede Neural Profunda
print("\nTestando previsões:")
predictions = dnn.predict(X_test)
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
predicoes = dnn.predict(novas_flores)

# Exibir resultados
print("\nPrevisões para novas amostras:")
for i, pred in enumerate(predicoes):
    print(f"Amostra {i+1}: Classe prevista -> {pred}")

    
