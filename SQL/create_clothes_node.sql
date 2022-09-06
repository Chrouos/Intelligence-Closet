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
	FilePosition text,--圖片位置
	IsFavorite int--衣物我的最愛
);

TRUNCATE TABLE clothes_node

INSERT INTO clothes_node
VALUES
	(0, 16, '3', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_1.jpg')

INSERT INTO clothes_node
VALUES( 1, 14, '2', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_2.jpg')

INSERT INTO clothes_node
VALUES( 2, 6, '3', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_3.jpg')

INSERT INTO clothes_node
VALUES
	( 3, 8, '4', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_4.jpg')

INSERT INTO clothes_node
VALUES(4, 8, '4', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_5.jpg')

select *
from clothes_node