# 🧠 Redes Neurais

## 📌 O que são Redes Neurais?
Redes neurais são **modelos computacionais** inspirados no funcionamento do **cérebro humano**. Elas são compostas por **neurônios artificiais** (perceptrons), que processam informações e aprendem com os dados.

### **Componentes Básicos**
1. **Neurônios (Nós)**: Unidades que processam entradas e produzem saídas.
2. **Conexões (Sinapses)**: Ligações entre neurônios com pesos que influenciam o aprendizado.
3. **Camadas**:
   - **Entrada**: Recebe os dados.
   - **Ocultas**: Processam informações.
   - **Saída**: Produz o resultado final.
4. **Função de Ativação**: Introduz **não-linearidade** para permitir que a rede aprenda padrões complexos.
5. **Pesos e Bias**: Ajustáveis durante o treinamento.

---

# 🔹 Tipos de Redes Neurais

## **1️⃣ Perceptron Simples (Single-Layer Perceptron)**
O **Perceptron Simples** resolve **problemas de classificação binária** (ex: Sim/Não, 0/1).

### **Funcionamento**
1. **Recebe entradas** (`x1, x2, ..., xn`).
2. **Multiplica por pesos** (`w1, w2, ..., wn`).
3. **Soma ponderada**:  
   \[
   z = (w1 \cdot x1 + w2 \cdot x2 + ... + wn \cdot xn) + bias
   \]
4. **Aplica uma função de ativação** para determinar a saída (`0` ou `1`).

### **⚠️ Limitação**
- Só resolve problemas **linearmente separáveis** (não consegue resolver **XOR**).

---

## **2️⃣ Redes Neurais com Múltiplas Camadas (MLP)**
As **Redes Neurais Multicamadas (MLPs)** possuem **camadas ocultas**, permitindo aprender padrões **não-lineares**.

### **Funcionamento**
1. **Camada de Entrada** → Recebe os dados.
2. **Camadas Ocultas** → Processam informações.
3. **Camada de Saída** → Produz o resultado final.

### **Backpropagation (Aprendizado)**
1. **Forward Propagation**: Calcula a saída.
2. **Cálculo do Erro**: Mede a diferença entre a saída prevista e a real.
3. **Backpropagation**: Ajusta os pesos usando **Gradiente Descendente**.
4. **Repetição**: Até minimizar o erro.

### **Funções de Ativação**
| Função | Fórmula | Vantagens | Desvantagens |
|--------|---------|-----------|-------------|
| **Sigmoid** | \( f(x) = \frac{1}{1 + e^{-x}} \) | Boa para probabilidades | Sofre com **vanishing gradient** |
| **Tanh** | \( f(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} \) | Melhor que sigmoid | Também sofre **vanishing gradient** |
| **ReLU** | \( f(x) = \max(0, x) \) | Rápida e eficiente | Pode sofrer de **neurônios mortos** |
| **Softmax** | \( f(x_i) = \frac{e^{x_i}}{\sum e^{x_j}} \) | Para **classificação multiclasse** | - |

---

## **3️⃣ Redes Neurais Profundas (DNNs)**
As **Redes Neurais Profundas (DNNs)** possuem **múltiplas camadas ocultas**, permitindo aprender representações **abstratas**.

### **Vantagens das DNNs**
✅ Capturam padrões **altamente não-lineares**.  
✅ Usadas em **reconhecimento de imagem, NLP, previsão de séries temporais**.  

### **Desafios das DNNs**
⚠️ **Overfitting** → Aprende muito bem o treino, mas falha nos dados reais.  
⚠️ **Exploding/Vanishing Gradient** → Os gradientes ficam grandes ou pequenos demais.  
⚠️ **Tempo de Treinamento** → Redes grandes precisam de mais dados e computação.

### **Técnicas para Melhorar DNNs**
✅ **Dropout** → Desativa neurônios aleatoriamente para evitar overfitting.  
✅ **Batch Normalization** → Normaliza ativações para acelerar o aprendizado.  
✅ **Inicialização de Pesos (Xavier, He)** → Evita problemas com gradientes.  

---

# 🚀 **Técnicas Avançadas**
| Técnica | Descrição |
|---------|----------|
| **Regularização L2** | Penaliza pesos altos para evitar overfitting. |
| **Momentum** | Acelera o gradiente descendente, evitando mínimos locais. |
| **Adam Optimizer** | Um dos otimizadores mais eficientes. |
| **CNNs** | Especializadas para **imagens**. |
| **RNNs** | Usadas para **textos e séries temporais**. |

---

# **📌 Resumo**
✅ **Perceptron Simples** → Apenas problemas **linearmente separáveis**.  
✅ **MLPs (Redes com uma camada oculta)** → Aprendem padrões **não-lineares**.  
✅ **DNNs (Redes Profundas)** → Aprendem representações **abstratas** e **complexas**.  
✅ **Técnicas como Dropout e Adam** melhoram o desempenho.  

---