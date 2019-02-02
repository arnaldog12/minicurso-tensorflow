# Instalação
1. Baixe ou clone o repositório.
2. Baixe e instale o [Miniconda](https://conda.io/miniconda.html). (__Windows__: marque a opção de adicionar o conda às variáveis de ambiente (_$PATH_))
3. Abra o terminal e digite o seguinte comando para instalar o ambiente:
    ```sh
    $ conda create -n minicurso tensorflow==1.12.0 jupyter==1.0.0 matplotlib==3.0.2
    ```

# Uso do ambiente

> __Nota:  É obrigatório seguir as ordens da seção "Instalação" antes de utilizar o ambiente__.

Siga os passos abaixo sempre que quiser executar os códigos desse repositório.
1. Abra o terminal e digite:

    - __Windows__:
    ```sh
    $ activate mpdl
    ```
    - __Linux/Mac__:
    ```sh
    $ source activate mpdl
    ```
2. Execute o Jupyter Notebook:
    ```sh
    $ jupyter notebook
    ```
