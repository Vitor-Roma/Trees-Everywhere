# Trees-Everywhere

# <b>Instalação</b>

- Instalar o <b><a style="color: #337BEA;" href="https://www.docker.com/">Docker</a></b>
- Instalar o <b><a href="https://docs.docker.com/compose/install/" style="color: #337BEA;">Docker Compose</a></b>
- Fazer o Clone do repositorio
- Trocar o nome do arquivo .env_sample para .env (Ou criar um .env e copiar o conteúdo)
- Rodar o comando make start no terminal
	```
	make start
	```
- Rodar as Migrates no seu banco de dados
	```
	make build
	```
 
- Criar usuário admin do Django com make admin
	```
	make admin
	```

- Dar a carga inicial no banco de dados pelas fixtures
	```
	make load_data
	```

- Rodar os testes
	```
	make test
	```
