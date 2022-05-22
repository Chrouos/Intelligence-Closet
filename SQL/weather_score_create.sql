drop table weather_score;

create table weather_score
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	-- Category varchar(50) NOT NULL,-- 衣物分類( upper, lower... )
	CategoryId bigint NOT NULL,-- 衣物分類( 0, 1, 2 )
	ClothesType varchar(255) NOT NULL,--衣物種類 ( short, long skirt... )
	Score bigint NOT NULL,
	-- 天氣分數(衣物本身的保暖程度)
	Name nvarchar(255)-- 衣物名稱
);

INSERT INTO weather_score
VALUES
	(1, 'short_TShirt', 1, '短袖');
--1
INSERT INTO weather_score
VALUES
	(1, 'long_sleeves', 2, '薄長袖');
--2
INSERT INTO weather_score
VALUES
	(1, 'sweater', 3, '針織毛衣');
--3
INSERT INTO weather_score
VALUES
	(1, 'long_TShirt', 3, '長袖');
--4
INSERT INTO weather_score
VALUES
	(2, 'short_pants', 1, '短褲');
--5
INSERT INTO weather_score
VALUES
	(2, 'long_skirt', 2, '長裙');
--6
INSERT INTO weather_score
VALUES
	(2, 'long_pants', 3, '長褲');
--7
INSERT INTO weather_score
VALUES
	(2, 'short_skirt', 1, '短裙');
--8
INSERT INTO weather_score
VALUES
	(4, 'thick_coat', 5, '厚外套');
--9
INSERT INTO weather_score
VALUES
	(4, 'down_coat', 9, '羽絨衣');
--10
INSERT INTO weather_score
VALUES
	(4, 'thin_coat', 3, '薄外套');
--11

select *
from weather_score;


