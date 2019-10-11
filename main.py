# Importação de bibliotecas
from sklearn.linear_model import SGDClassifier
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
from PIL import Image
import PIL.ImageOps
import numpy as np
import matplotlib
import os

print('\nBaixando lista de treino (MNIST)...')
print('Aguarde pacientemente, enquanto isso veja os slides')

matplotlib.use(backend="TkAgg")


# Abre o dataset MNIST
mnist = fetch_openml('mnist_784', version=1, cache=False)
mnist.target = mnist.target.astype(np.int8)
print('OK\n')
# Nome da Imagem
filename = 'num'

# Deixando a imagem legivel para o algoritmo
print('Tratando a imagem...')
img = Image.open(filename + '.png').convert('L')
inverted_image = PIL.ImageOps.invert(img)
data = np.array(inverted_image, dtype='uint8')

np.save(filename + '.npy', data)
print('OK\n')

img_array = np.load(filename + '.npy')

# Treina o algoritmo a partir do MNIST
X, y = mnist["data"], mnist["target"]

print('Treinando algoritmo...')
X_train, X_test, y_train, y_test = X[:60000], X[60000:], y[:60000], y[60000:]
print('OK\n')

print('Testando algoritmo...')
shuffle_index = np.random.permutation(60000)
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]
print('OK\n')

print('Reconhecendo Imagem...')
# Passando os dados para o Binary Classifier
y_train_num0 = (y_train == 0)
y_test_num0 = (y_test == 0)

y_train_num1 = (y_train == 1)
y_test_num1 = (y_test == 1)

y_train_num2 = (y_train == 2)
y_test_num2 = (y_test == 2)

y_train_num3 = (y_train == 3)
y_test_num3 = (y_test == 3)

y_train_num4 = (y_train == 4)
y_test_num4 = (y_test == 4)

y_train_num5 = (y_train == 5)
y_test_num5 = (y_test == 5) 

y_train_num6 = (y_train == 6)
y_test_num6 = (y_test == 6)

y_train_num7 = (y_train == 7)
y_test_num7 = (y_test == 7)

y_train_num8 = (y_train == 8)
y_test_num8 = (y_test == 8)

y_train_num9 = (y_train == 9)
y_test_num9 = (y_test == 9)

sgd_clf = SGDClassifier(random_state=42)
reshaped_img = img_array.flatten()

num0 = sgd_clf.fit(X_train, y_train_num0)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 0')

sgd_clf.fit(X_train, y_train_num1)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 1')

sgd_clf.fit(X_train, y_train_num2)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 2')

sgd_clf.fit(X_train, y_train_num3)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 3')

sgd_clf.fit(X_train, y_train_num4)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 4')

sgd_clf.fit(X_train, y_train_num5)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 5')

sgd_clf.fit(X_train, y_train_num6)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 6')

sgd_clf.fit(X_train, y_train_num7)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 7')

sgd_clf.fit(X_train, y_train_num8)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 8')

sgd_clf.fit(X_train, y_train_num9)
resultado = sgd_clf.predict([reshaped_img])

if(resultado == True):
    print('Seu numero é 9')

else:
    print('Nenhum numero foi detectado :/')
	
os.system('pause')
