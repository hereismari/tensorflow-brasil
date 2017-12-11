# TensorFlow Brasil :brazil:

Esse repositório contém códigos e materiais sobre TensorFlow em português a fim de ajudar pessoas interessadas a aprender mais sobre Machine Learning, Deep Learning e TensorFlow.

Todos os códigos estão em Python, no formato de [Jupyter Notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) para fins didáticos.

## Outros materiais recomendados

Aqui você encontra materiais e recursos, em sua grande maioria em inglês, sobre TensorFlow e Deep Learning. Os materiais em português são apresentados em negrito.

Materiais mais específicos (ex: GANs, Reinforcement Learning, ...) podem ser acessados neste [nesse link](https://github.com/mari-linhares/DeepLearning). Bom aprendizado!

### TensorFlow

[Tutoriais e samples de código](https://www.tensorflow.org)

[TensorFlow lite](https://www.tensorflow.org/mobile/tflite/)

[TensorBoard](https://www.tensorflow.org/get_started/summaries_and_tensorboard)

[TensorBoard - exemplo rodando via web](projector.tensorflow.org)

[Estimators API](https://www.tensorflow.org/extend/estimators)

[Datasets API](https://www.tensorflow.org/programmers_guide/datasets)

[TensorFlow Eager](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/contrib/eager/README.md)

[TensorFlow Serving](https://www.tensorflow.org/serving/)

### Deep Learning

[Curso de Stanford CS231n](https://cs231n.github.io)

[Machine Learning Nanodegree do Udacity](https://goo.gl/ODpXj4)

[Intro. a Deep Learning com TensorFlow Udacity](https://goo.gl/iHssII)

[Google Recipes - Começando com ML e DL](https://goo.gl/KewA03)


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

### Erros ou melhorias em materiais já existentes

Criar uma issue é suficiente, fique a vontade para resolver o problema através de um Pull Request após a criação da issue.

### Novos Materiais

Caso queira contribuir com um novo material siga o padrão/formato dos materiais já existentes e coloque todos os links de referência no início dos notebooks.

Todo material:

* Deve conter qual versão do TensorFlow deve ser usada para rodar o notebook no topo do notebook.
* Contém todas as dependências importadas juntas no início do notebook para facilitar a execução.

> The code and resources available in this repository are in Brazilian Portuguese.
