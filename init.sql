-- init.sql for lab4_db
-- Cameron Wertelka

drop table if exists books cascade;
drop table if exists authors cascade;
drop table if exists book_authors cascade;

create table books (
	id serial,
	title text,
	isbn integer,
	primary key(id)
);

create table authors (
	id serial,
	author_name text,
	e_mail text unique,
	primary key(id)
);

create table book_authors (
	id serial,
	book_id integer references books(id),
	author_id integer references authors(id),
	primary key(id)
);

create or replace view books_view as
	select books.id as booksid, books.title, books.isbn,
	authors.id as authid, authors.author_name, authors.e_mail
	from books join book_authors on books.id=book_authors.book_id 
	join authors on book_authors.author_id=authors.id;
