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
- Dar a carga inicial no banco de dados pelas fixtures
	```
	make load_data
	```
- Criar usuário admin do Django com make admin
	```
	make admin
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
<img src="https://github.com/user-attachments/assets/49fc0333-d5fe-417d-9041-6f9573654daa">
<a href="http://localhost>8000/login/ style="color: #33C3DA;">
	<b>Página de Login</b>
</a>
<img src="https://github.com/user-attachments/assets/5dc0de8e-d939-44af-8150-24ed9bcf6280">
<br>
<a href="http://localhost:8000/me/dashboard/" style="color: #33C3DA;">
	<b>Árvores plantas pelo usuário</b>
</a>
<img src="https://github.com/user-attachments/assets/b50255dd-cc70-4122-89b1-5592a43cf2e7">
<br>
<a href="http://localhost:8000/accounts/dashboard/" style="color: #33C3DA;">
	<b>Árvores plantadas por todas as contas do usuário</b>
</a>
<img src="https://github.com/user-attachments/assets/b31dbe2b-d50a-4497-82a2-eb6f7115347c">
<br>
<a href="http://localhost:8000/api/me/planted_trees/" style="color: #33C3DA;">
	<b>Api com todas as Árvores plantadas pelo usuário</b>
</a>
<img src="https://github.com/user-attachments/assets/7524e19a-1a70-42d6-8fea-881016491011">
<br>
<a href="http://localhost:8000/api/me/planted_trees/1/" style="color: #33C3DA;">
	<b>Api mostrando os dados de uma árvores plantada pelo ID</b>
</a>
<img src="https://github.com/user-attachments/assets/76b08c7e-632d-4989-8891-ca7b4d065a66">
