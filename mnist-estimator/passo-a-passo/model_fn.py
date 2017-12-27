# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf
import numpy as np

def build_cnn(input_layer, mode):
    with tf.name_scope("conv1"):  
      conv1 = tf.layers.conv2d(inputs=input_layer,filters=32, kernel_size=[5, 5],
                               padding='same', activation=tf.nn.relu)

    with tf.name_scope("pool1"):  
      pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)

    with tf.name_scope("conv2"):  
      conv2 = tf.layers.conv2d(inputs=pool1,filters=64, kernel_size=[5, 5],
                               padding='same', activation=tf.nn.relu)

    with tf.name_scope("pool2"):  
      pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)

    with tf.name_scope("dense"):  
      pool2_flat = tf.reshape(pool2, [-1, 7 * 7 * 64])
      dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)

    with tf.name_scope("dropout"): 
      # dropout apenas se estivermos treinando
      # você pode aprender mais sobre dropout e CNNs aqui:
      # https://en.wikipedia.org/wiki/Convolutional_neural_network#Dropout 
      is_training_mode = mode == tf.estimator.ModeKeys.TRAIN
      dropout = tf.layers.dropout(inputs=dense, rate=0.4, training=is_training_mode)

    logits = tf.layers.dense(inputs=dropout, units=10)

    return logits

def model_fn(features, labels, mode, params):
  # Deve conter os seguintes passos:
  
  # 1. Definir o modelo via TF
  if params['model'] == 'simples':
    output = tf.layers.dense(inputs=features['x'], units=10)
  elif params['model'] == 'CNN':
    # mudando a shape da entrada para a esperada pela CNN
    input_layer = tf.reshape(features['x'], [-1, 28, 28, 1])
    output = build_cnn(input_layer, mode)
  
  
  # 2. Definir como gerar predições
  predicoes = {
      'classes': tf.argmax(input=output, axis=1),
      'probabilidades': tf.nn.softmax(output, name='softmax_tensor')
  }
  
  # Se estamos realizando predição precisamos apenas especificar estas operações ;)
  if mode == tf.estimator.ModeKeys.PREDICT:
    # Return an EstimatorSpec object
    return tf.estimator.EstimatorSpec(mode=mode, predictions=predicoes)
  
  
  # 3. Definir a loss function para treino e avaliação
  # loss => erro, como calcular nosso erro?
  loss =  tf.losses.softmax_cross_entropy(onehot_labels=labels, logits=output)


  # Se estamos treinando precisamos definir como otimizar nosso modelo
  # Para o Estimator esta definição é chamada train_op
  if mode == tf.estimator.ModeKeys.TRAIN:
    
    # 4. Definir como otimizar o modelo (optimizer)
    # como otimizar nosso modelo utilizando o erro que calculamos?
    # Neste exemplo estamos usando um algoritmo de otimizacao chamado Adam
    train_op = tf.contrib.layers.optimize_loss(
      loss=loss,
      global_step=tf.train.get_global_step(),
      learning_rate=params['learning_rate'],
      optimizer=params['optimizer'])
    
    return tf.estimator.EstimatorSpec(mode=mode, predictions=predicoes,
                                      loss=loss, train_op=train_op)
  
  
  # 5. Definir métricas para avaliação
  eval_metric_ops = {
      'acuracia': tf.metrics.accuracy(
          tf.argmax(input=output, axis=1),
          tf.argmax(input=labels, axis=1))
  }
  
  # 6. Retornar um EstimatorSpec definindo os passos acima
  return tf.estimator.EstimatorSpec(mode=mode, predictions=predicoes,
                                      loss=loss, eval_metric_ops=eval_metric_ops)
