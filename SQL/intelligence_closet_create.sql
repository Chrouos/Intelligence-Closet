drop table clothes_information

create table clothes_information
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	WeatherScoreId	bigint NOT NULL,-- 衣物分類( 0, 1... ) => 阿亮
	Color varchar(50) NOT NULL,-- 衣物顏色 => 阿亮
	-- WeatherScore int NOT NULL,-- 衣物天氣分數 
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	CategoryId bigint NOT NULL,--衣物種類 ( weather_score.id ) => 阿亮
	ClothesStyle varchar(255) NULL,-- 衣物風格 => 阿亮
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text--圖片位置
);

insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(2, 'blue', 1, 0, GETDATE(), GETDATE() )
insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(2, 'red',  2, 0, GETDATE(), GETDATE() )


insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(1, 'blue', 4, 0, GETDATE(), GETDATE() )
insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(1, 'black',5, 0, GETDATE(), GETDATE() )

select *
from clothes_information
