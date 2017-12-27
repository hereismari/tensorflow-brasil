# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
# MNIST
from tensorflow.examples.tutorials.mnist import input_data

import numpy as np
 
print ('Versão do TensorFlow:', tf.__version__)

# Buscando dados de treino e teste
mnist = input_data.read_data_sets('/tmp/MNIST/', one_hot=True)

# x_treino: imagens, y_treino: labels
x_treino = mnist.train.images
y_treino = mnist.train.labels
x_teste = mnist.test.images
y_teste = mnist.test.labels


# Input function de treino
mnist_treino_input = tf.estimator.inputs.numpy_input_fn(
  # os dados devem ser passados como um dicionário, contendo cada feature
  # como nossa entrada é uma imagem, ou seja, apenas uma feature
  # temos apenas uma chave no dicionário 'x' cujo valor são as imagens  
  {'x': np.array(x_treino, dtype=np.float32) },
  # os labels esperados para numpy_input_fn é um vetor numpy
  np.array(y_treino, dtype=np.int32),
  # sempre importanto "misturar" os dados de treino
  shuffle=True,
  # este parâmetro = None, implica em repetir os dados de forma "circular"
  # iremos controlar o número de interações durante o treino do modelo.
  num_epochs=None)

# Input function de teste
mnist_teste_input = tf.estimator.inputs.numpy_input_fn(
  # da mesma forma os dados devem ser passados como um dicionário
  {'x':np.array(x_teste, dtype=np.float32)},
  # labels
  np.array(y_teste, dtype=np.int32),
  # misturando os dados
  shuffle=True,
  # sem repetir os dados
  num_epochs=1)

