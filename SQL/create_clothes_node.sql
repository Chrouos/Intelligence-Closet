drop table clothes_node

create table clothes_node
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	SubCategoryId bigint NOT NULL,-- 衣物分類( 0, 1... )
	ColorId bigint NOT NULL,-- 衣物顏色ID
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text,--圖片位置
	IsFavorite int
);

TRUNCATE TABLE clothes_node

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(0, 6, 10, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_1', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(1, 1, 11, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_2', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(2, 1, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_3', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(3, 3, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_4', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(4, 9, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_5', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(5, 8, 11, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_6', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(6, 8, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_7', 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(7, 9, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_8', 0);

select *
from clothes_node