Essa é uma API desenvolvida para a aplicação Insights, e tem funções para cadastrar, consultar, atualizar e remover cards e tags da aplicação. A API foi desenvolvida em Python utilizando Django com o auxílio do Django REST Framework.

## Rodando o projeto

**Por favor rode os comandos listados com permissões de adminstrador**

É necessário que a máquina tenha o python 3.8 ou posterior instalado, veja como aqui:
[Download Python](https://www.python.org/downloads/)

Sinta-se a vontade para criar um ambiente virtual python para hospedar o projeto, não é obrigatório, mas recomendado, veja como aqui:
[Documentação Virtual Env](https://docs.python.org/pt-br/3/library/venv.html)

Agora é preciso instalar as dependências do projeto.
Na pasta em que você descarregou, rode o comando:
```
python -m pip install -r requirements.txt
```

Pronto. O pip já instalou as dependências.

Agora, para subir o backend, vá com um terminal na pasta insights_api e rode os comandos:
```
python manage.py makemigrations
python manage.py migrate
```

Com isso o banco de dados foi devidamente criado e está pronto para a aplicação

#### Para subir a aplicação em modo debug/desenvolvimento

Para subir em modo desenvolvimento rode:
```
python manage.py runserver 0.0.0.0:8000
```

Se tudo ocorreu bem, a API já está disponível para uso, rodando na porta 8000

#### Para subir em modo de uso real

São necessárias alguma modificações no arquivo **settings.py**

- Primeiramente é necessário definir a flag de *DEBUG* para *FALSE*

- Em um caso de subir de fato para produção *altamente recomendado* passar um novo valor ao campo *SECRET_KEY*

Agora rode:
```
python manage.py runserver 0.0.0.0:8000
```

Se tudo ocorreu bem, a API já está disponível para uso, rodando na porta 8000

Por fim, em ambos os casos, a lista *ALLOWED_HOSTS* deve receber nomes dos hosts que estão habilitados a se comunicar com a API. Use *'127.0.0.1'* e *'localhost'* se as requisições vierem apenas da própria máquina, mas como se trata de uma API web, use '*' para aceitar requisições de qualquer origem

Para ver a documentação da API, acesse:

http://127.0.0.1:8000/swagger/

**A documentação swagger só será acessível com a flag DEBUG de desenvolvimento igual a TRUE**

Para rodar os testes, na pasta insights_api rode:
```
python manage.py test
```

## CLI

O CLI uma ferramenta para importar os cards de um arquivo CSV e os cadastrar no banco via API, portanto, para utilizá-lo é necessário que a API esteja rodando

Caso o CLI esteja rodando em outra máquina ou virtualenv diferente do backend, é necessário instalar o [Download Python](https://www.python.org/downloads/), e posteriormente instalar a dependência:
```
python -m pip install requests
```

Após isso basta rodar 
```
ImportCards.py <caminho_do_arquivo> <url_api>
```

Por exemplo:
```
ImportCards.py cards.csv http://algumhost:8000/api/v1/cards/
```

O primeiro parâmetro é obrigatório, uma vez que o caminho do arquivo. Já o segundo é opcional, e caso não seja informado, enviará as requisições para http://127.0.0.1:8000/api/v1/cards/