-- 負責存取有關於台灣目前開放中央氣象局所提供之API站別的所有縣市。

drop table city

create table city
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	CityName varchar(50), -- 縣市名稱
	DayAPIId varchar(50), -- 縣市兩日API ID
	WeekAPIId varchar(50) -- 縣市一周API ID
);

insert into city
values
	('宜蘭縣', '001', '003')

insert into city
values
	('桃園市', '005', '007')

insert into city
values
	('新竹縣', '009', '011')

insert into city
values
	('苗栗縣', '013', '015')

insert into city
values
	('彰化縣', '017', '019')

insert into city
values
	('南投縣', '021', '023')

insert into city
values
	('雲林縣', '025', '027')

insert into city
values
	('嘉義縣', '029', '031')

insert into city
values
	('屏東縣', '033', '035')

insert into city
values
	('臺東縣', '037', '039')

insert into city
values
	('花蓮縣', '041', '043')

insert into city
values
	('澎湖縣', '045', '047')

insert into city
values
	('基隆市', '049', '051')

insert into city
values
	('新竹市', '053', '055')

insert into city
values
	('嘉義市', '057', '059')

insert into city
values
	('臺北市', '061', '063')

insert into city
values
	('高雄市', '065', '067')

insert into city
values
	('新北市', '069', '071')

insert into city
values
	('臺中市', '073', '075')

insert into city
values
	('臺南市', '077', '079')

insert into city
values
	('連江縣', '081', '083')

insert into city
values
	('金門縣', '085', '087')