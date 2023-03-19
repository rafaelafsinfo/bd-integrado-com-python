# criação da database
create database biblioteca;
use biblioteca;

#criação das tabelas
create table editora (id int primary key, 
nome varchar(255));
create table autor (id int primary key, 
nome varchar(255));
create table livros(id int primary key not null, 
	titulo varchar(255), 
	autor_id int not null, 
	editora_id int not null, 
	ano_publicacao int not null, 
	isbn int not null,
    foreign key(autor_id) references autor(id),
    foreign key(editora_id) references editora(id));
create table usuario(id int primary key not null, 
	nome varchar(255) not null,
	 endereco varchar(255) not null, 
	 telefone int not null,
	 email varchar(255) not null);
create table emprestimos(id int primary key not null, 
	 usuario_id int not null,
	 livro_id int not null, 
	 data_emprestimo date, 
	 data_devolucao date, 
	 foreign key(usuario_id) references usuario(id), 
	 foreign key(livro_id) references livros(id));