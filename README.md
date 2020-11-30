# H.E.M.L
## Projeto para a feira de ciências da ETEC de 2019

<p align="center" style="display: flex; align-items: center; justify-content: space-around">
  <img src="https://pluspng.com/img-png/python-logo-png-speeding-up-python-and-numpy-c-ing-the-way-360.png" alt="python" width="100">
  <img src="https://avatars3.githubusercontent.com/u/17349883?s=400&v=4" alt="python" width="150">
</p>

  O projeto é um classificador binario que consegue reconher a partir de uma imagem desenhada no paint um número, o projeto foi feito em python
usando as bibliotecas MatPlotLib, SkLearn e NumPy.
  O projeto usa o dataset MNIST para fazer o treinamento para reconhecimento dos números e a partir disso tenta reconhecer o seu número baseado nos
dados que ele tem, lembrando que são números de 0 a 9.

  Para começar, garanta que você tem o Python 3 instalado em seu computador, se não baixe-o aqui: https://www.python.org/downloads/
Após isso instale as bibliotecas:

```console
hello@world:~$ pip install numpy
hello@world:~$ pip install matplotlib
hello@world:~$ pip install -U scikit-learn
```

  Após isso você já pode testar o programa pois ja vem com uma imagem de teste, se quiser testar seu próprio número, edite o arquivo num.png 
(recomendo que edite usando o paint) e lembrando que a imagem deve ser obrigatoriamente 28x28, salve ela e pronto, ja pode testar novamente

```console
hello@world:~$ python main.py
```

Só lembrando que não é 100% preciso ;)
OBS: Na época que criei isso, ainda não conhecia Multi Label Classification, portanto peço desculpas a quantidade de IF's que tem :D
