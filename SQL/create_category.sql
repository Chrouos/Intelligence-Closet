-- category負責管理衣服種類，其中衣物種類分為上半身、下半身、外套、洋裝、配件、鞋子等，方便後續進行分類篩選，該資料庫將應用在各個衣物的資訊列表內的其中一項。

drop TABLE category;

create table category
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號( 1, 2, 3 ... )
	CategoryName varchar(50) Not Null,-- 衣物名稱
	[Level] int Not Null-- 衣物層級
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