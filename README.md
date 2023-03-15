# Karaoke Backend

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
Instalados todos os pacotes, utilize o comando do Django para **rodar o servidor**:
~~~ bash
python3 manage.py runserver
~~~
:warning: **ATENÇÃO:** Caso o Django informe que existem migrações para serem feitas (texto em vermelho assim que o servidor começar a rodar), utilize o comando:
~~~ bash
python3 manage.py migrate
~~~