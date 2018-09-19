O conteúdo dessa pasta foi inspirado [nesse artigo](https://medium.com/@tuennermann/convolutional-neural-networks-to-find-cars-43cbc4fb713).

# Datasets
Foram utilizandos ambos [vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/vehicles.zip) e [non-vehicle](https://s3.amazonaws.com/udacity-sdc/Vehicle_Tracking/non-vehicles.zip) datasets para treinar o modelo.

# Estrutura de Pastas
Use a seguinte estrutura de pastas para rodar o arquivo _estimators.ipynb_:

```
├── data (unzip datasets here)
├── models
├── estimators.ipynb
```

# Dependências
Além das dependências descritas no README.md da raiz desse repositório, você também irá precisar instalar os seguintes pacotes:

- opencv3
- scikit-learn

Para instalar esses pacotes, basta rodar o código abaixo no terminal:
```sh
pip install opencv3 scikit-learn
```