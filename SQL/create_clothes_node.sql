drop table clothes_node

create table clothes_node
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	SubCategoryId bigint NOT NULL,-- 衣物分類( 0, 1... )
	ColorId varchar(50) NOT NULL,-- 衣物顏色ID
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text--圖片位置
);

TRUNCATE TABLE clothes_node

select *
from clothes_node


