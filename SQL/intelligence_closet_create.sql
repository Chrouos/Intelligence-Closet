drop table clothes_information

create table clothes_information
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	WeatherScoreId bigint NOT NULL,-- 衣物分類( 0, 1... ) 
	ColorId varchar(50) NOT NULL,-- 衣物顏色ID
	-- WeatherScore int NOT NULL,-- 衣物天氣分數 
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	-- CategoryId bigint NOT NULL,--衣物種類 ( weather_score.id )
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text--圖片位置
);

TRUNCATE TABLE clothes_information

delete clothes_information where Id = 3


select *
from clothes_information


INSERT INTO clothes_information
VALUES
	(1, 0, 16, '3', None, None, 0, datetime.datetime(2022, 6, 26, 19, 51, 41, 350000), datetime.datetime(2022, 6, 26, 19, 51, 41, 350000), 'UI/web/public/src/clothes_1.jpg')
INSERT INTO clothes_information
VALUES
	(2, 1, 14, '2', None, None, 0, datetime.datetime(2022, 6, 26, 22, 13, 9, 13000), datetime.datetime(2022, 6, 26, 22, 13, 9, 13000), 'UI/web/public/src/clothes_2.jpg')
INSERT INTO clothes_information
VALUES
	(4, 2, 6, '3', None, None, 0, datetime.datetime(2022, 6, 26, 22, 14, 47, 267000), datetime.datetime(2022, 6, 26, 22, 14, 47, 267000), 'UI/web/public/src/clothes_3.jpg')
INSERT INTO clothes_information
VALUES
	(5, 3, 8, '4', None, None, 0, datetime.datetime(2022, 6, 26, 22, 15, 13, 217000), datetime.datetime(2022, 6, 26, 22, 15, 13, 217000), 'UI/web/public/src/clothes_4.jpg')
INSERT INTO clothes_information
VALUES
	(6, 4, 8, '4', None, None, 0, datetime.datetime(2022, 6, 26, 22, 15, 34, 570000), datetime.datetime(2022, 6, 26, 22, 15, 34, 570000), 'UI/web/public/src/clothes_5.jpg')
