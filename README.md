# Pokedex - Projeto Django

Este é um projeto Django chamado Pokedex, que permite o gerenciamento e a pesquisa de informações sobre Pokémon. Ele inclui recursos como a adição de treinadores, Pokémon e itens, bem como a visualização de dados relacionados a Pokémon.

## Uso do Projeto

Para começar a usar o projeto Pokedex, siga estas etapas:

### Pré-requisitos

Certifique-se de ter os seguintes pré-requisitos instalados em seu sistema:

- Python 3.x
- Django
- PostgreSQL

### Configuração do Ambiente

1. Clone este repositório em sua máquina local:

   ```shell
   git clone https://github.com/JVictor011/Pokedex.git
2. Navegue até o diretório do projeto:
   ```shell
   cd Pokedex
3. Configure um ambiente virtual (recomendado) e ative-o:
   ```shell
   python -m venv venv
   source venv/bin/activate  # No Windows, use "venv\Scripts\activate"
4. Instale as dependências do Django:
   ```shell
   pip install -r requirements.txt
5. Configure o banco de dados PostgreSQL em settings.py. Substitua as configurações padrão pelo seu próprio banco de dados PostgreSQL:
   ```shell
     DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.postgresql',
          'NAME': 'seu_banco_de_dados',
          'USER': 'seu_usuario',
          'PASSWORD': 'sua_senha',
          'HOST': 'localhost',
          'PORT': '5432',
      }
    }
6. Execute as migrações do banco de dados para criar as tabelas necessárias:
   ```shell
   python manage.py migrate
7. Crie um superusuário para acessar a área administrativa (opcional):
   ```shell
   python manage.py createsuperuser
### Executando o Projeto
1. Inicie o servidor de desenvolvimento:
   ```shell
   python manage.py runserver
2. Acesse o projeto em seu navegador em http://localhost:8000/.

3. Você pode fazer login no painel administrativo em http://localhost:8000/admin/ usando as credenciais do superusuário que você criou.

### Funcionalidades
Aqui estão algumas das funcionalidades incluídas no projeto:

- **Login**: Acesse a página de login para autenticar-se como treinador.
- **Adicionar Treinador**: Crie uma nova conta de treinador com informações pessoais.
- **Adicionar Pokémon**: Adicione Pokémon à sua coleção, incluindo nome, nível e outras informações.
- **Adicionar Itens**: Adicione itens relacionados a Pokémon, como poções e revives.
- **Pesquisa de Pokémon**: Use a barra de pesquisa para procurar Pokémon pelo nome.
- **Visão Geral**: Obtenha uma visão geral das informações dos treinadores.

### Contribuição
Sinta-se à vontade para contribuir para este projeto.

