import numpy as np

class PerceptronOR:
    def __init__(self, n_inputs, learning_rate=0.1, epochs=10):
        self.weights = np.random.rand(n_inputs)  # Inicializa pesos aleatórios
        self.bias = np.random.rand(1)  # Inicializa o viés
        self.learning_rate = learning_rate  # Taxa de aprendizado
        self.epochs = epochs  # Número de épocas
    
    def activation(self, x):
        """Função de ativação degrau."""
        return 1 if x >= 0 else 0
    
    def predict(self, inputs):
        """Calcula a saída do perceptron."""
        z = np.dot(inputs, self.weights) + self.bias  # Soma ponderada
        return self.activation(z)  # Aplica função de ativação
    
    def train(self, X, y):
        """Treina o perceptron com o conjunto de dados."""
        for epoch in range(self.epochs):
            for inputs, target in zip(X, y):
                prediction = self.predict(inputs)  # Faz previsão
                error = target - prediction  # Calcula erro
                self.weights += self.learning_rate * error * inputs  # Atualiza pesos
                self.bias += self.learning_rate * error  # Atualiza viés
                
                # Print dos ajustes
                print(f"Época {epoch+1}, Entrada: {inputs}, Previsão: {prediction}, Erro: {error}")

# Dados de entrada (X1, X2) e saída esperada (OR)
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 1, 1, 1])  # Saídas esperadas para o OR

# Criar e treinar o modelo
perceptron = PerceptronOR(n_inputs=2, learning_rate=0.1, epochs=10)
perceptron.train(X, y)

# Testar com novas entradas
print("\nTestes:")
for inputs in X:
    print(f"Entrada: {inputs}, Previsão: {perceptron.predict(inputs)}")
