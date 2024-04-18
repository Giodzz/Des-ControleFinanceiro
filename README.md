# (Des)Controle Financeiro
Projeto django para auxiliar no planejamento e controle financeiro de alguém, que suporte a utilização de diversas contas bancárias e as diversas formas de pagamento.


## Configuração do Ambiente Virtual

É recomendado o uso de um ambiente virtual para evitar conflitos de dependências com outros projetos. Para criar e ativar um ambiente virtual, execute:

**No Windows:**
```
python -m venv .venv
.venv\Scripts\activate
```

**Linux ou MAC**
```
python3 -m venv .venv
source .venv/bin/activate
```

## Instalando Dependências
Com o ambiente virtual ativado, instale as dependências do projeto com o comando:
```
pip install -r requirements.txt
```

## Configuração Inicial
Antes de executar o projeto pela primeira vez, você precisará realizar as migrações do banco de dados 
```
python manage.py migrate
```
Para criar um superusuário administrador, execute:
```
python manage.py createsuperuser
```
Siga as instruções no terminal para configurar o usuário administrador.

## Executando o Servidor de Desenvolvimento
Para iniciar o servidor de desenvolvimento do Django, use o comando:
```
python manage.py runserver
```
O servidor irá iniciar no endereço http://127.0.0.1:8000/ por padrão. Abra o endereço em seu navegador para visualizar o projeto.
