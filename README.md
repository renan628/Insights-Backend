
## Rodando o projeto

### Backend

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

Agora, para subir o backend, vá com um terminal na pasta myapi e rode os comandos:
```
python manage.py makemigrations
python manage.py migrate
```

Com isso o banco de dados foi devidamente criado e está pronto para a aplicação

#### Para subir a aplicação em modo debug/desenvolvimento

Para subir em modo desenvolvimento rode:
```
python manage.py runserver
```

Se tudo ocorreu bem, a API já está disponível para uso, rodando na porta 8000

#### Para subir em modo de uso real

São necessárias alguma modificações no arquivo **settings.py**

- Primeiramente é necessário definir a flag de *DEBUG* para *FALSE*

- Depois é necessário passar um novo valor ao campo *SECRET_KEY*, que recomendadamente deve ser carregado de um arquivo interno ao servidor

- Por fim a lista *ALLOWED_HOSTS* deve receber nomes dos hosts que estão habilitados a se comunicar com a API. Use *'127.0.0.1'* e *'localhost'* se as requisições apenas da própria máquina, use *'*'* para aceitar requisições de qualquer origem

Agora rode:
```
python manage.py runserver
```

Se tudo ocorreu bem, a API já está disponível para uso, rodando na porta 8000

Para ver a documentação da API, acesse:
http://127.0.0.1:8000/swagger/

Para rodar os testes, na pasta myapi rode:
python manage.py test

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

## Frontend

Primeiramente é necessário ter o [Node e NMP](https://nodejs.org/en/download/) 

Na pasta Frontend que foi extraida do projeto, abra um terminal e execute

```
npm install
```

Isso irá instalar todas as dependências do projeto

### Para subir em modo debug/desenvolvimento

Ainda no terminal na pasta projeto, rode:

```
npm start
```

A aplicação então, subirá na porta 3000

### Para subir em modo de uso real

Primeiramente rode
```
npm run build
```
Agora é necessário instalar um servidor simples para rodar a aplicação, mas esse isso só precisa ser feito uma única vez
```
npm install -g serve
```

E por fim, servir a aplicação, que deve iniciar na porta 5000
```
serve -s build
```

Essa é claro, uma solução simples. É possível servir a aplicação em algum servidor web conhecido, como por exemplo o [NGINX](https://www.nginx.com/)