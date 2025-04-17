import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

# 1️⃣ Carregar o dataset MNIST
mnist = keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2️⃣ Normalizar os valores das imagens (0-255[0-preto, 255-branco] → 0-1[0-preto, 1-branco])
X_train = X_train / 255.0
X_test = X_test / 255.0

# 3️⃣ Adicionar uma dimensão extra para representar os canais da imagem (necessário para CNNs)
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)

# 4️⃣ Criar a Rede Neural Convolucional (CNN)
model = keras.Sequential([
    # Camada Convolucional 1 (32 filtros de 3x3, ReLU)
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    keras.layers.MaxPooling2D((2,2)),  # Camada de Pooling

    # Camada Convolucional 2 (64 filtros de 3x3, ReLU)
    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.MaxPooling2D((2,2)),  # Camada de Pooling

    # Achatar os dados para alimentar a camada densa
    keras.layers.Flatten(),

    # Camada totalmente conectada (densa)
    keras.layers.Dense(128, activation='relu'),

    # Camada de saída (Softmax para classificação de 10 dígitos)
    keras.layers.Dense(10, activation='softmax')
])

# 5️⃣ Compilar o modelo
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 6️⃣ Treinar a CNN
model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# 7️⃣ Avaliar o modelo
test_loss, test_acc = model.evaluate(X_test, y_test)
print(f"\nAcurácia no conjunto de teste: {test_acc * 100:.2f}%")

# 8️⃣ Testar com uma imagem do conjunto de teste
plt.imshow(X_test[1].reshape(28,28), cmap="gray")
plt.title(f"Previsão: {np.argmax(model.predict(X_test[0].reshape(1,28,28,1)))}")
plt.show()
