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

- Usuários criados:
	```
	username=user1 password=password
	username=user2 password=password
	username=user3 password=password
	```

- Rodar os testes
	```
	make test
	```

### Endpoints

<a href="http://localhost:8000/admin/" style="color: #33C3DA;">
	<b>Página do Admin</b>
</a>
<br>
<a href="http://localhost:8000/me/dashboard/" style="color: #33C3DA;">
	<b>Árvores plantas pelo usuário</b>
</a>
<br>
<a href="http://localhost:8000/accounts/dashboard/" style="color: #33C3DA;">
	<b>Árvores plantadas por todas as contas do usuário</b>
</a>
<br>
<a href="http://localhost:8000/api/me/planted_trees/" style="color: #33C3DA;">
	<b>Api com todas as Árvores plantadas pelo usuário</b>
</a>
<br>
<a href="http://localhost:8000/api/me/planted_trees/1/" style="color: #33C3DA;">
	<b>Api mostrando os dados de uma árvores plantada pelo ID</b>
</a>