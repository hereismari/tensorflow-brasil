# TensorFlow Brasil :brazil:

Esse repositório contém códigos e materiais sobre TensorFlow em português escritos por brasileiros a fim de ajudar pessoas interessadas a aprender sobre Machine Learning, Deep Learning e TensorFlow.

Todos os exemplos são implementados em Python (compatíveis com Python2 e Python3), no formato de [Jupyter Notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) para fins didáticos.

## Outros materiais recomendados

Aqui você encontra materiais e recursos, em sua grande maioria em inglês, sobre TensorFlow e Deep Learning. Os materiais em português são apresentados em negrito.

Materiais mais específicos (ex: GANs, Reinforcement Learning, ...) podem ser acessados neste [nesse link](https://github.com/mari-linhares/DeepLearning). Bom aprendizado!

## Materiais

### Vídeos

* [19/04/2019 - Começando com TensorFlow 2.0](https://www.youtube.com/watch?time_continue=3&v=sQjOMOtQc6I), [código](https://github.com/smoreira/TensorFlow2/blob/master/nnTF2.ipynb)

### Blogs

 * [24/09/2018 - Introduction to Real-Time Face Pose Estimation with Deep Learning (Inglês apenas)](https://medium.com/analytics-vidhya/face-pose-estimation-with-deep-learning-eebd0e62dbaf)
* [29/04/2018 - TensorFlow Summit 2018 - Resumo de novidades](https://medium.com/@mariannelinharesm/tensorflow-summit-2018-resumo-de-novidades-73c77cd93529)
 * [27/12/2017 - Implementando Estimators](https://medium.com/@mariannelinharesm/tensorflow-v1-4-0-estimators-parte-1-1a58bbfc13ae)

### TensorFlow

 * [Tutoriais e samples de código](https://www.tensorflow.org)

 * [TensorFlow lite](https://www.tensorflow.org/mobile/tflite/)

 * [TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard)

 * [TensorBoard - exemplo rodando via web](projector.tensorflow.org)

 * [Estimators API](https://www.tensorflow.org/extend/estimators)

 * [Datasets API](https://www.tensorflow.org/programmers_guide/datasets)

 * [TensorFlow Eager](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/eager/README.md)

 * [TensorFlow Serving](https://www.tensorflow.org/serving/)

 * [TensorFlow For Poets](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/#0)

### Deep Learning

 * [Curso de Stanford CS231n](https://cs231n.github.io)
 
 * [Deep Learning Specialization (Coursera)](https://www.coursera.org/specializations/deep-learning)

 * [Machine Learning Nanodegree do Udacity](https://goo.gl/ODpXj4)
 
 * [Deep Learning Nanodegree do Udacity](https://br.udacity.com/course/deep-learning-nanodegree-foundation--nd101)

 * [Intro. a Deep Learning com TensorFlow Udacity](https://goo.gl/iHssII)
 
 * [Deep Learning Explained (Microsoft)](https://www.edx.org/course/deep-learning-explained)

 * [Google Recipes - Começando com ML e DL](https://goo.gl/KewA03)


## O que preciso para executar o código?

Considerando que você já tenha Python 2 ou 3 instalado na sua máquina...

### TensorFlow

Há vários modos de instalar o TensorFlow, para simplificar aconselho usar o [site de instalação](https://www.tensorflow.org/install/).

Caso queira (**recomendado**) você pode instalar TensorFlow e as demais depedências num ambiente virtual para melhor gerenciar as bibliotecas e suas versões, para tal você pode utilizar o [Virtualenv](https://virtualenv.pypa.io/en/stable/) como mostrado no [tutorial de instalação do TensorFlow](https://www.tensorflow.org/install/install_linux#installing_with_virtualenv). Outras opções como [Docker](https://www.docker.com/) ou [conda](https://conda.io/docs/index.html) também podem ser utilizadas.

### Instalar dependências

As principais dependências são:
  * Jupyter Notebooks
  * Numpy
  * Pandas
  * Matplotlib

Essas bibliotecas ser instaladas localmente com os comandos a seguir:
```
# python 2
python2 -m pip install jupyter numpy pandas matplotlib
```
```
# python 3
python3 -m pip install jupyter numpy pandas matplotlib
```

### Jupyter notebooks

Se você não tiver familiariade com Jupyter notebooks visite o link da [sessão anterior](https://github.com/mari-linhares/tensorflow-brasil#tensorflow-brasil-brazil) e tente se familiarizar com os conceitos, nada muito complicado, é suficiente instalar e rodar :smile:.

Outa dica é utilizar [**Colaboratory (Colab)**](https://colaboratory.jupyter.org) que é uma ferramenta desenvolvida pela Google para ajudar a compartilhar o ensino e pesquisa de Machine Learning. O colab é um jupyter notebook que roda na nuvem e portanto não requer nenhum tipo de configuração local, os notebooks são salvos no Google Drive e podem ser importardos/exportados facilmente. Uma ótima solução e gratuita! Consulte o [FAQ](https://research.google.com/colaboratory/faq.html) para mais informações.

## Como contribuir?

Contribuições são muito bem vindas!

### Melhorar ou consertar materiais já existentes

Criar uma issue é suficiente, fique a vontade para resolver o problema através de um Pull Request após a criação da issue.

### Novos Materiais

Caso queira contribuir com um novo material siga o padrão/formato dos materiais já existentes e coloque todos os links de referência no início dos notebooks.

Todo material:

* Deve conter qual versão do TensorFlow deve ser usada para rodar o notebook no topo do notebook.
* Contém todas as dependências importadas juntas no início do notebook para facilitar a execução.

> The code and resources available in this repository are not related to TensorFlow or Google in anyway.
