# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

# Input functions
from input_fn import mnist_treino_input, mnist_teste_input

# Model functions
from model_fn import model_fn

# Permite imprimir logs do TensorFlow
tf.logging.set_verbosity(tf.logging.INFO)

print ('Versão do TensorFlow:', tf.__version__)

# Criando nosso modelo simples
model_params = {
  'optimizer': 'Adam',
  'learning_rate': 1e-4,
  'model': 'simples'
}

# model_dir indica onde salvar os dados do modelo (pesos, logs, arquivos tensorboard)
modelo_simples = tf.estimator.Estimator(model_fn=model_fn, params=model_params, model_dir='output/simples/')

# Treino por 10000 passos
modelo_simples.train(input_fn=mnist_treino_input, steps=10000)

# Avaliando modelo
print (modelo_simples.evaluate(input_fn=mnist_teste_input))


model_params['model'] = 'CNN'
modelo_cnn = tf.estimator.Estimator(model_fn=model_fn, params=model_params, model_dir='output/cnn/')

# Treino por 10000 passos
modelo_cnn.train(input_fn=mnist_treino_input, steps=10000)

# Avaliando modelo
print (modelo_cnn.evaluate(input_fn=mnist_teste_input))

