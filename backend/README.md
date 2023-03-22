# Karaoke Backend
Um projeto de karaokê desenvolvido de amigos para amigos. Esse repositório é referente ao back-end do projeto, mas você pode conferir também o [repositório do front-end](https://github.com/artursennass/karaoque-role-de-migos) para ter uma visão mais completa do projeto.

## Rodando projeto
Primeiro crie o **ambiente virtual** dentro da raiz do projeto:
~~~bash
python3 -m venv venv
~~~
Ative o ambiente virtual:
~~~bash
source ./venv/bin/activate
~~~
Com o ambiente virtual ativo, **instale os pacotes necessários**:
~~~bash
pip install -r requirements.txt
~~~
Será necessário também, **gerar uma chave secreta para seu repositório local**. Para isso, utilize o comando:
~~~ bash
python3 manage.py shell
~~~
Depois, import a função que gera a chave:
~~~ python
from django.core.management.utils import get_random_secret_key  
~~~
Execute a função e copie a chave gerada no terminal:
~~~ python
get_random_secret_key()
~~~
Agora, na raiz do projeto, crie um arquivo `.env` e adicione a variável de ambiente `SECRET_KEY`, recebendo sua nova chave secreta e **certifique-se de remover as aspas da chave copiada e os sinais de maior e menor do exemplo abaixo**:
~~~ bash
SECRET_KEY=<cole_sua_chave_secreta_sem_aspas>
~~~
Instalados todos os pacotes e gerada a sua chave secreta, utilize o comando do Django para **rodar o servidor**:
~~~ bash
python3 manage.py runserver
~~~
Por último, caso o Django informe que existem migrações para serem feitas (texto em vermelho assim que o servidor começar a rodar), utilize o comando:
~~~ bash
python3 manage.py migrate
~~~