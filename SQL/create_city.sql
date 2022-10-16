-- 負責存取有關於台灣目前開放中央氣象局所提供之API站別的所有縣市。

drop table city

create table city
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- ½s¸¹ ( 1, 2, 3 ... )
	CityName varchar(50)-- «°Âí¦WºÙ
);

insert into city
values
	('宜蘭縣')

insert into city
values
	('桃園市')

insert into city
values
	('新竹縣')

insert into city
values
	('苗栗縣')

insert into city
values
	('彰化縣')

insert into city
values
	('南投縣')

insert into city
values
	('雲林縣')

insert into city
values
	('嘉義縣')

insert into city
values
	('屏東縣')

insert into city
values
	('臺東縣')

insert into city
values
	('花蓮縣')

insert into city
values
	('澎湖縣')

insert into city
values
	('基隆市')

insert into city
values
	('新竹市')

insert into city
values
	('嘉義市')

insert into city
values
	('臺北市')

insert into city
values
	('高雄市')

insert into city
values
	('新北市')

insert into city
values
	('臺中市')

insert into city
values
	('臺南市')

insert into city
values
	('連江縣')

insert into city
values
	('金門縣')