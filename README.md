## *Projeto desenvolvido e testado no VS Code (Linux)*

### Especificações
- python 3.12
- mongoDB
- redis

### Contextualização
Este repositório serve como uma extensão do projeto <a href="https://github.com/hiGuigo/pymongo-crud">**pymongo-crud**</a> e, portanto, foi desenvolvido tendo em mente a configuração e ambiente base estabelecidos por essa aplicação.

As funcionalidades do **pymongo-redis** envolvem:
 1. Coletar o que existe nas collections disponíveis na base de dados original
 2. Popular a base de dados do Redis com o que foi coletado
 3. Atualizar a collection original com base nas alterações feitas através da interface do Redis
 4. Login utilizando "expire" do Regis
 5. Validação do login

 ### Manual do usuário
 1. Acessar <a href="https://github.com/hiGuigo/pymongo-crud">**pymongo-crud**</a> e seguir o manual do usuário
 2. Configurar as variáveis de ambiente: `cp .env_template .env`
 3. Criar e ativar o ambiente virtual: `python3 -m venv .venv` -> `source python3 .venv/bin/activate` (linux)
 4. Iniciar a aplicação: `cd src` -> `python3 main.py`

