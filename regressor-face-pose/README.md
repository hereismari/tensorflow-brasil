Nesse tutorial, nós vamos treinar um modelo para prever o roll, pitch e yaw de uma face mostrada para a câmera. Você pode conferir o modelo rodando em CPU no gif abaixo:

![](https://media.giphy.com/media/pPhEG3Grfxh4z2Hk6I/giphy.gif)

O conteúdo dessa pasta foi inspirado [nesse artigo](https://medium.com/@arnaldog12/face-pose-estimation-with-deep-learning-eebd0e62dbaf).

# Dados

Você pode baixar os dados utilizados nesse problema [aqui](https://drive.google.com/file/d/1e4GHFBYgx4wfcrdUjf7O4anhhVgu9Iz6/view?usp=sharing). Extraia esse arquivo na pasta "data".

# Estrutura de Pastas

Use a seguinte estrutura de pastas para rodar o arquivo estimators.ipynb:

```
├── data (unzip dataset here)
├── images
├── models
├── estimators.ipynb
```

# Depedências

Além das dependências descritas no README.md da raiz desse repositório, você também irá precisar instalar os seguintes pacotes:

- opencv
- dlib
- scikit-learn

Para instalar esses pacotes, basta rodar o código abaixo no terminal:

```
pip install opencv scikit-learn dlib
```
