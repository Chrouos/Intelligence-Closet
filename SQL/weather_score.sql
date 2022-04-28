drop table weather_score;

create table weather_score
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Category varchar(50) NOT NULL,-- 衣物分類( upper, lower... )
	ClothesType varchar(255) NOT NULL,--衣物種類 ( short, long skirt... )
	Score bigint NOT NULL,
	Name nvarchar(255)-- 衣物名稱
);

select * from weather_score;

INSERT INTO weather_score VALUES ('upper', 'short_TShirt', 1, '短袖');
INSERT INTO weather_score VALUES ('upper', 'long_sleeves', 2, '薄長袖');
INSERT INTO weather_score VALUES ('upper', 'sweater', 3, '針織毛衣');
INSERT INTO weather_score VALUES ('upper', 'long_TShirt', 3, '長袖');
INSERT INTO weather_score VALUES ('lower', 'short_pants', 1, '短褲');
INSERT INTO weather_score VALUES ('lower', 'long_skirt', 2, '長裙');
INSERT INTO weather_score VALUES ('lower', 'long_pants', 3, '長褲');
INSERT INTO weather_score VALUES ('lower', 'short_skirt', 1, '短裙');
INSERT INTO weather_score VALUES ('coat', 'thick_coat', 5, '厚外套');
INSERT INTO weather_score VALUES ('coat', 'down_coat', 9, '羽絨衣');
INSERT INTO weather_score VALUES ('coat', 'thin_coat', 3, '薄外套');



