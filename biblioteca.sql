# criação da database
create database biblioteca;
use biblioteca;

#criação das tabelas
create table editora (id int primary key, #forte
nome varchar(255)); #forte
create table autor (id int primary key, #forte
nome varchar(255)); #forte
create table livros(id int primary key not null, #forte
	titulo varchar(255), #forte
	autor_id int not null, #fraca
	editora_id int not null, #fraca
	ano_publicacao int not null, #forte
	isbn int not null, #forte
    foreign key(autor_id) references autor(id),
    foreign key(editora_id) references editora(id));
create table usuario(id int primary key not null, #forte
	nome varchar(255) not null, #forte
	 endereco varchar(255) not null, #forte
	 telefone int not null, #forte
	 email varchar(255) not null); #forte
create table emprestimos(id int primary key not null, #forte
	 usuario_id int not null, #fraca
	 livro_id int not null,  #fraca
	 data_emprestimo date, #forte
	 data_devolucao date,  #forte
	 foreign key(usuario_id) references usuario(id), 
	 foreign key(livro_id) references livros(id));