# TensorFlow Brasil :brazil:

Esse repositório contém códigos e materiais sobre TensorFlow em português a fim de ajudar pessoas interessadas a aprender mais sobre Machine Learning, Deep Learning e TensorFlow.

Todos os códigos estão em Python, no formato de [Jupyter Notebooks](http://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/what_is_jupyter.html) para fins didáticos.

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

Se você não tiver familiariade com Jupyter notebooks visite o link da sessão anterior e tente se familiarizar com os conceitos, nada muito complicado, é suficiente instalar e rodar :smile:.

Outa dica é utilizar [**Colaboratory (Colab)**](colaboratory.jupyter.org) que é uma ferramenta desenvolvida pela Google para ajudar a compartilhar o ensino e pesquisa de Machine Learning. O colab é um jupyter notebook que roda na nuvem e portanto não requer nenhum tipo de configuração local, os notebooks são salvos no Google Drive e podem ser importardos/exportados facilmente. Uma ótima solução e gratuita! Consulte o [FAQ](https://research.google.com/colaboratory/faq.html) para mais informações.

## Como contribuir?

Contribuições são muito bem vindas!

### Erros ou melhorias em materiais já existentes

Criar uma issue é suficiente, fique a vontade para resolver o problema você mesmo(a) através de um Pull Request após a criação da issue.

### Novos Materiais

Caso queira contribuir com um novo material siga o padrão/formato dos materiais já existentes e coloque todos os links de referência no início dos notebooks.

Todo material:
  * Deve conter qual versão do TensorFlow deve ser usada para rodar o notebook no topo do notebook.
  * Contém todas as dependências importadas juntas no início do notebook para facilitar a execução.

> The code and resources available in this repository are in Brazilian Portuguese.
