drop TABLE category;

create table category
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號( 1, 2, 3 ... )
	CategoryName varchar(50) Not Null,-- 衣物名稱
	[ Level ] int Not Null-- 衣物層級
);

insert into category
values
	('upper', 1)

insert into category
values
	('lower', 1)

insert into category
values
	('dress', 1)

insert into category
values
	('coat', 2)

insert into category
values
	('accessories', 3)

insert into category
values
	('cap', 3)

insert into category
values
	('shoes', 1)

insert into category
values
	('Not_sure', 0)

select *
from category