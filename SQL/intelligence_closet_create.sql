drop table clothes_information

create table clothes_information
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int Unique,-- 放在衣櫃裡面的位置( 0 ~ 9)
	Category varchar(50) NOT NULL,-- 衣物分類( upper, lower... ) => 阿亮
	Color varchar(50) NOT NULL,-- 衣物顏色 => 阿亮
	-- WeatherScore int NOT NULL,-- 衣物天氣分數 
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	ClothesType varchar(255) NOT NULL,--衣物種類 ( short_TShirt, long_skirt... ) => 阿亮
	ClothesStyle varchar(255) NULL,-- 衣物風格 => 阿亮
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text--圖片位置
);

select * from clothes_information


insert into clothes_information (Category, Color, ClothesType, UsageCounter, CreateTime, ModifyTime) VALUES('upper', 'blue', 'short_TShirt', 0, GETDATE(), GETDATE() )

