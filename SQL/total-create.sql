create table category
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	CategoryName varchar(50) Not Null,-- 衣物分類
	[Level] int Not Null-- 衣物層級
);

insert into category
values
	('upper', 1)

insert into category
values
	('lower', 1)

insert into category
values
	('dress', 1)

insert into category
values
	('coat', 2)

insert into category
values
	('accessories', 3)

insert into category
values
	('cap', 3)

insert into category
values
	('shoes', 1)

insert into category
values
	('Not_sure', 0)


----------------------------------------------------------
create table city
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	CityName varchar(50), -- 縣市名稱
	DayAPIId varchar(50), -- 縣市兩日API ID
	WeekAPIId varchar(50) -- 縣市一周API ID
);
----------------------------------------------------------
create table clothes_node_upper
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	SubCategoryId bigint NOT NULL,-- 衣物分類( 0, 1... )
	ColorId bigint NOT NULL,-- 衣物顏色ID
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	WarmLevel bigint,-- 保暖程度
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text,--圖片位置
	IsFavorite int--衣物我的最愛
);

create table clothes_node_lower
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	SubCategoryId bigint NOT NULL,-- 衣物分類( 0, 1... )
	ColorId bigint NOT NULL,-- 衣物顏色ID
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	WarmLevel bigint,-- 保暖程度
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text,--圖片位置
	IsFavorite int--衣物我的最愛
);

create table clothes_node_other
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	SubCategoryId bigint NOT NULL,-- 衣物分類( 0, 1... )
	ColorId bigint NOT NULL,-- 衣物顏色ID
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	WarmLevel bigint,-- 保暖程度
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text,--圖片位置
	IsFavorite int--衣物我的最愛
);


INSERT INTO intelligence_closet.dbo.clothes_node_upper
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(0, 6, 10, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_1.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_upper
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(1, 1, 11, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_2.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_upper
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(2, 1, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_3.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_upper
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(3, 3, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_4.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_lower
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(4, 9, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_5.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_lower
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(5, 8, 11, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_6.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_lower
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(6, 8, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_7.jpg', 0);

INSERT INTO intelligence_closet.dbo.clothes_node_lower
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite)
VALUES(7, 9, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_8.jpg', 0);



----------------------------------------------------------



create table clothes_node
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Position int,-- 放在衣櫃裡面的位置( 0 ~ 9)
	SubCategoryId bigint NOT NULL,-- 衣物分類( 0, 1... )
	ColorId bigint NOT NULL,-- 衣物顏色ID
	UserPreferences int NULL,-- 使用者喜好程度 (0~10)
	WarmLevel bigint,-- 保暖程度
	ClothesStyle varchar(255) NULL,-- 衣物風格
	UsageCounter int NOT NULL,-- 衣物使用次數
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
	FilePosition text,--圖片位置
	IsFavorite int--衣物我的最愛
);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(0, 6, 10, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_1.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(1, 1, 11, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_2.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(2, 1, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_3.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(3, 3, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_4.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(4, 9, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_5.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(5, 8, 11, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_6.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(6, 8, 2, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_7.jpg', 0, 0);

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(7, 9, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_8.jpg', 0, 0);

-------


create table color_graph
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,
	-- 編號 ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL,
	-- 顏色配對1
	ColorId2 bigint NOT NULL,
	-- 顏色配對2
	ColorScore float NOT NULL
	-- 配對分數
);


------------------------w
insert color_graph
values
	(5, 5, 1)
--紅 紅 1
insert color_graph
values
	(5, 6, 3)
--紅 橘 3
insert color_graph
values
	(5, 7, 4)
--紅 黃 4
insert color_graph
values
	(5, 8, 3.5)
--紅 綠 3.5
insert color_graph
values
	(5, 2, 2)
--紅 藍 2
insert color_graph
values
	(5, 9, 3.5)
--紅 紫 3.5
insert color_graph
values
	(5, 3, 4)
--紅 黑 4
insert color_graph
values
	(5, 10, 4)
--紅 灰 0
insert color_graph
values
	(5, 4, 4)
--紅 白 2.5
insert color_graph
values
	(5, 11, 4)
--紅 米白 2.5
insert color_graph
values
	(5, 12, 4)
--紅 軍綠 0
insert color_graph
values
	(5, 13, 4)
--紅 卡其 3

insert color_graph
values
	(6, 5, 3)
--橘 紅 3
insert color_graph
values
	(6, 6, 2)
--橘 橘 2
insert color_graph
values
	(6, 7, 3.5)
--橘 黃 3.5
insert color_graph
values
	(6, 8, 1)
--橘 綠 1
insert color_graph
values
	(6, 2, 0)
--橘 藍 0
insert color_graph
values
	(6, 9, 2)
--橘 紫 2
insert color_graph
values
	(6, 3, 3)
--橘 黑 3
insert color_graph
values
	(6, 10, 0)
--橘 灰 0
insert color_graph
values
	(6, 4, 4)
--橘 白 4
insert color_graph
values
	(6, 11, 4)
--橘 米白 2.5
insert color_graph
values
	(6, 12, 4)
--橘 軍綠 0
insert color_graph
values
	(6, 13, 4)
--橘 卡其 3

insert color_graph
values
	(7, 5, 4)
--黃 紅 4
insert color_graph
values
	(7, 6, 4.5)
--黃 橘 4.5
insert color_graph
values
	(7, 7, 3)
--黃 黃 3
insert color_graph
values
	(7, 8, 3)
--黃 綠 3
insert color_graph
values
	(7, 2, 1)
--黃 藍 1
insert color_graph
values
	(7, 9, 0)
--黃 紫 0
insert color_graph
values
	(7, 3, 3)
--黃 黑 3
insert color_graph
values
	(7, 10, 0)
--黃 灰 0
insert color_graph
values
	(7, 4, 4)
--黃 白 4
insert color_graph
values
	(7, 11, 4)
--黃 米白 4.5
insert color_graph
values
	(7, 12, 4)
--黃 軍綠 3
insert color_graph
values
	(7, 13, 4)
--黃 卡其 4.5

insert color_graph
values
	(8, 5, 3.5)
--綠 紅 3.5
insert color_graph
values
	(8, 6, 1)
--綠 橘 1
insert color_graph
values
	(8, 7, 3)
--綠 黃 3
insert color_graph
values
	(8, 8, 2)
--綠 綠 2
insert color_graph
values
	(8, 2, 3.5)
--綠 藍 3.5
insert color_graph
values
	(8, 9, 0)
--綠 紫 0
insert color_graph
values
	(8, 3, 3)
--綠 黑 3
insert color_graph
values
	(8, 10, 2)
--綠 灰 2
insert color_graph
values
	(8, 4, 3)
--綠 白 3
insert color_graph
values
	(8, 11, 4)
--綠 米白 3
insert color_graph
values
	(8, 12, 4)
--綠 軍綠 4
insert color_graph
values
	(8, 13, 4)
--綠 卡其 1.5

insert color_graph
values
	(2, 5, 2)
--藍 紅 2
insert color_graph
values
	(2, 6, 0)
--藍 橘 0
insert color_graph
values
	(2, 7, 1)
--藍 黃 1
insert color_graph
values
	(2, 8, 3)
--藍 綠 3
insert color_graph
values
	(2, 2, 4)
--藍 藍 4
insert color_graph
values
	(2, 9, 4.5)
--藍 紫 4.5
insert color_graph
values
	(2, 3, 4.5)
--藍 黑 4.5
insert color_graph
values
	(2, 10, 2)
--藍 灰 2
insert color_graph
values
	(2, 4, 5)
--藍 白 5
insert color_graph
values
	(2, 11, 4)
--藍 米白 4.5
insert color_graph
values
	(2, 12, 4)
--藍 軍綠 2
insert color_graph
values
	(2, 13, 4)
--藍 卡其 2.5

insert color_graph
values
	(9, 5, 3.5)
--紫 紅 3.5
insert color_graph
values
	(9, 6, 1)
--紫 橘 1
insert color_graph
values
	(9, 7, 3)
--紫 黃 3
insert color_graph
values
	(9, 8, 2)
--紫 綠 2
insert color_graph
values
	(9, 2, 3.5)
--紫 藍 3.5
insert color_graph
values
	(9, 9, 0)
--紫 紫 0
insert color_graph
values
	(9, 3, 3)
--紫 黑 3
insert color_graph
values
	(9, 10, 2)
--紫 灰 2
insert color_graph
values
	(9, 4, 3)
--紫 白 3
insert color_graph
values
	(9, 11, 4)
--紫 米白 3
insert color_graph
values
	(9, 12, 4)
--紫 軍綠 0
insert color_graph
values
	(9, 13, 4)
--紫 卡其 0

insert color_graph
values
	(3, 5, 0)
--黑 紅 0
insert color_graph
values
	(3, 6, 0)
--黑 橘 0
insert color_graph
values
	(3, 7, 0)
--黑 黃 0
insert color_graph
values
	(3, 8, 0)
--黑 綠 0
insert color_graph
values
	(3, 2, 1)
--黑 藍 1
insert color_graph
values
	(3, 9, 1)
--黑 紫 1
insert color_graph
values
	(3, 3, 5)
--黑 黑 5
insert color_graph
values
	(3, 10, 4.5)
--黑 灰 4.5
insert color_graph
values
	(3, 4, 4.5)
--黑 白 4.5
insert color_graph
values
	(3, 11, 4)
--黑 米白 4
insert color_graph
values
	(3, 12, 4)
--黑 軍綠 4
insert color_graph
values
	(3, 13, 4)
--黑 卡其 3.5

insert color_graph
values
	(10, 5, 0)
--灰 紅 0
insert color_graph
values
	(10, 6, 0)
--灰 橘 0
insert color_graph
values
	(10, 7, 0)
--灰 黃 0
insert color_graph
values
	(10, 8, 0)
--灰 綠 0
insert color_graph
values
	(10, 2, 3)
--灰 藍 3
insert color_graph
values
	(10, 9, 3)
--灰 紫 3
insert color_graph
values
	(10, 3, 4.5)
--灰 黑 4.5
insert color_graph
values
	(10, 10, 5)
--灰 灰 5
insert color_graph
values
	(10, 4, 4)
--灰 白 4
insert color_graph
values
	(10, 11, 4)
--灰 米白 4.5
insert color_graph
values
	(10, 12, 4)
--灰 軍綠 2
insert color_graph
values
	(10, 13, 4)
--灰 卡其 3.5

insert color_graph
values
	(4, 5, 4.5)
--白 紅 4.5
insert color_graph
values
	(4, 6, 3)
--白 橘 3
insert color_graph
values
	(4, 7, 3)
--白 黃 3
insert color_graph
values
	(4, 8, 2)
--白 綠 2
insert color_graph
values
	(4, 2, 3)
--白 藍 3
insert color_graph
values
	(4, 9, 2.5)
--白 紫 2.5
insert color_graph
values
	(4, 3, 4)
--白 黑 4
insert color_graph
values
	(4, 10, 5)
--白 灰 5
insert color_graph
values
	(4, 4, 3.5)
--白 白 3.5
insert color_graph
values
	(4, 11, 4)
--白 米白 2.5
insert color_graph
values
	(4, 12, 4)
--白 軍綠 3
insert color_graph
values
	(4, 13, 4)
--白 卡其 5

insert color_graph
values
	(11, 5, 0)
--米白 紅 0
insert color_graph
values
	(11, 6, 0)
--米白 橘 0
insert color_graph
values
	(11, 7, 1)
--米白 黃 1
insert color_graph
values
	(11, 8, 0)
--米白 綠 0
insert color_graph
values
	(11, 2, 0)
--米白 藍 0
insert color_graph
values
	(11, 9, 0)
--米白 紫 0
insert color_graph
values
	(11, 3, 4.5)
--米白 黑 4.5
insert color_graph
values
	(11, 10, 4)
--米白 灰 4
insert color_graph
values
	(11, 4, 3.5)
--米白 白 3.5
insert color_graph
values
	(11, 11, 3)
--米白 米白 3
insert color_graph
values
	(11, 12, 2)
--米白 軍綠 2
insert color_graph
values
	(11, 13, 4)
--米白 卡其 4

insert color_graph
values
	(12, 5, 0)
--軍綠 紅 0
insert color_graph
values
	(12, 6, 0)
--軍綠 橘 0
insert color_graph
values
	(12, 7, 0)
--軍綠 黃 0
insert color_graph
values
	(12, 8, 0)
--軍綠 綠 0
insert color_graph
values
	(12, 2, 0)
--軍綠 藍 0
insert color_graph
values
	(12, 9, 0)
--軍綠 紫 0
insert color_graph
values
	(12, 3, 4.5)
--軍綠 黑 4.5
insert color_graph
values
	(12, 10, 2)
--軍綠 灰 2
insert color_graph
values
	(12, 4, 4)
--軍綠 白 4.5
insert color_graph
values
	(12, 11, 3)
--軍綠 米白 3
insert color_graph
values
	(12, 12, 2.5)
--軍綠 軍綠 2.5
insert color_graph
values
	(12, 13, 4)
--軍綠 卡其 4

insert color_graph
values
	(13, 5, 0)
--卡其 紅 0
insert color_graph
values
	(13, 6, 0)
--卡其 橘 0
insert color_graph
values
	(13, 7, 2.5)
--卡其 黃 2
insert color_graph
values
	(13, 8, 1)
--卡其 綠 1
insert color_graph
values
	(13, 2, 0)
--卡其 藍 0
insert color_graph
values
	(13, 9, 0)
--卡其 紫 0
insert color_graph
values
	(13, 3, 5)
--卡其 黑 5
insert color_graph
values
	(13, 10, 4)
--卡其 灰 4
insert color_graph
values
	(13, 4, 4.5)
--卡其 白 4.5
insert color_graph
values
	(13, 11, 4)
--卡其 米白 4
insert color_graph
values
	(13, 12, 1)
--卡其 軍綠 1
insert color_graph
values
	(13, 13, 2.5)
--卡其 卡其 2.5

----------------------------------------------------------
create table node_graph
(
	Id bigint IDENTITY(1,1) NOT NULL,
	UpperId bigint NULL,-- 上半身衣物Id
	LowerId bigint NULL,-- 下半身衣物Id
	OtherId bigint NULL,-- 其他衣物Id
	UserLike bigint NULL,-- 使用者喜好度
	CreateTime datetime NOT NULL,
	ModifyTime datetime NOT NULL,
	CONSTRAINT PK__node_gra__3214EC0755D155C9 PRIMARY KEY (Id)
);
----------------------------------------------------------
create table station
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	StationNumber varchar(20),-- 站號	
	StationName nvarchar(50),-- 站名
	CityId bigint NOT NULL,-- 城市編號
	[Address] nvarchar(255),-- 地址
	Remark nvarchar(255),-- 備註
	CreateTime date,-- 資料起始日期
	ModifyTime date,-- 異動時間
	Work int,-- 是否運作
);
----------------------------------------------------------
create table color
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	ColorEngName varchar(30) NOT NULL,-- 顏色名稱(英文)
	ColorName nvarchar(30)-- 顏色名稱(中文)

);

insert color
values
	('Undefined', NULL)--1
insert color
values
	('BLUE', '藍色')--2
insert color
values
	('BLACK', '黑色')--3
insert color
values
	('WHITE', '白色')--4
insert color
values
	('RED', '紅色')--5
insert color
values
	('ORANGE', '橘色')--6
insert color
values
	('YELLOW', '黃色')--7
insert color
values
	('GREEN', '綠色')--8
insert color
values
	('PURPLE', '紫色')--9
insert color
values
	('GRAY', '灰色')--10
insert color
values
	('CREAMY WHITE', '米白色')--11
insert color
values
	('ARMY GREEN', '軍綠色')--12
insert color
values
	('KHAKI', '卡其色')--13
insert color
values
	('CYAN', '青色')
--14

----------------------------------------------------------
create table sub_category
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	CategoryId bigint NOT NULL,-- 衣物分類( 0, 1, 2 )
	ClothesType varchar(255) NOT NULL,--衣物種類 ( short, long skirt... )
	Score bigint NOT NULL,-- 天氣分數(衣物本身的保暖程度)
	Name nvarchar(255)-- 衣物名稱
);

INSERT INTO sub_category
VALUES(1, 'T-Shirt', 1, 'T恤')
INSERT INTO sub_category
VALUES(1, 'Undershirt', 1, '背心')
INSERT INTO sub_category
VALUES(1, 'Shirt', 1, '襯衫')
INSERT INTO sub_category
VALUES(1, 'Polo', 1, '運動衫')
INSERT INTO sub_category
VALUES(1, 'Longsleeve', 3, '長袖')
INSERT INTO sub_category
VALUES(1, 'Hoodie', 4, '帽T')
INSERT INTO sub_category
VALUES(4, 'Outwear', 4, '外套')

INSERT INTO sub_category
VALUES(2, 'Shorts', 1, '短褲')
INSERT INTO sub_category
VALUES(2, 'Pants', 3, '長褲')
INSERT INTO sub_category
VALUES(2, 'Skirt', 2, '裙子')

INSERT INTO sub_category
VALUES(3, 'Dress', 3, '洋裝')
INSERT INTO sub_category
VALUES(3, 'Body', 2, '連身衣')

INSERT INTO sub_category
VALUES(4, 'Blazer', 4, '西裝外套')

INSERT INTO sub_category
VALUES(8, 'Not_sure', 0, '不確定')

select *
from sub_category;
----------------------------------------------------------
create table user_dashboard
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	UserName nvarchar(50) Null,--使用者名稱
	WeatherLike int Not Null,--喜歡的天氣(5為最熱)
	ModifyTime datetime Not Null,--異動時間
	VillageId bigint,--可以記錄使用者目前所在城市&鄉鎮
	Clock datetime,
);

insert into user_dashboard
VALUES
	('DiuDu', 5, GETDATE(), 1, GETDATE())

----------------------------------------------------------
----------------------------------------------------------
create view v_category_clothes
as
	select
		sc.Id,
		sc.CategoryId,
		cat.CategoryName,
		sc.ClothesType,
		sc.Score,
		sc.Name,
		cat.[Level]
	from sub_category as sc
		inner join category as cat on cat.Id = sc.CategoryId
----------------

CREATE view v_clothes_node
as
	SELECT
		cn.Id,
		cn.Position,
		cn.SubCategoryId,
		sc.Name as SubCategoryName,
		sc.CategoryId,
		sc.Score ,
		categorys.CategoryName ,
		cn.ColorId ,
		colors.ColorEngName ,
		colors.ColorName ,
		cn.UserPreferences ,
		cn.WarmLevel ,
		cn.ClothesStyle ,
		cn.UsageCounter ,
		cn.CreateTime ,
		cn.ModifyTime ,
		cn.FilePosition ,
		cn.IsFavorite
	from clothes_node cn
		inner join sub_category sc on sc.Id = cn.SubCategoryId
		inner join category categorys on categorys.Id = sc.CategoryId
		inner join color colors on colors.Id = cn.ColorId

----------------------------------------------------------

CREATE view v_clothes_graph
as
	select
		vcn_u.Id as UpperClothesId,
		vcn_u.[Position] as UpperPosition,
		vcn_u.SubCategoryId as UpperSubCategory,
		vcn_u.ColorId as upperColorId,
		vcn_u.UserPreferences as upperUserPreferences,
		vcn_u.FilePosition as upperFilePosition,
		-- vcn_u.IsFavorite as upperIsFavorite,

		vcn_l.Id as LowerClothesId,
		vcn_l.[Position] as LowerPosition,
		vcn_l.SubCategoryId as LowerSubCategory,
		vcn_l.ColorId as LowerColorId,
		vcn_l.UserPreferences as LowerUserPreferences,
		vcn_l.FilePosition as LowerFilePosition,
		-- vcn_l.IsFavorite as LowerIsFavorite,

		vcn_o.Id as OtherClothesId,
		vcn_o.[Position] as OtherPosition,
		vcn_o.SubCategoryId as OtherSubCategory,
		vcn_o.ColorId as OtherColorId,
		vcn_o.UserPreferences as OtherUserPreferences,
		vcn_o.FilePosition as OtherFilePosition,
		-- vcn_o.IsFavorite as OtherIsFavorite

		coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalPreferences,
		-- coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalColorCombs
		ng.UserLike
	from
		node_graph ng
		inner join v_clothes_node vcn_u on vcn_u.CategoryId = 1 and ng.UpperId = vcn_u.Id
		inner join v_clothes_node vcn_l on vcn_l.CategoryId = 2 and ng.LowerId  = vcn_u.Id
		inner join v_clothes_node vcn_o on vcn_o.CategoryId != 1 and vcn_u.CategoryId != 2 and ng.OtherId = vcn_o.Id


----------------------------------------------------------
create view v_color_graph
as
	select
		cg.ColorId1 as 'UpperColorId',
		cg.ColorId2 as 'LowerColorId',
		c1.ColorEngName as 'UpperEngName',
		c2.ColorEngName as 'LowerEngName',
		c1.ColorName as 'UpperColor',
		c2.ColorName as 'LowerColor',
		cg.ColorScore
	from color_graph as cg
		inner join color as c1 on c1.Id = cg.ColorId1
		inner join color as c2 on c2.Id = cg.ColorId2

----------------------------------------------------------
create view v_station
AS
	select
		st.Id,
		st.StationNumber,
		st.StationName,
		st.CityId,
		ci.CityName,
		st.Address,
		st.Remark,
		st.CreateTime,
		st.ModifyTime,
		st.Work
	from station as st
		inner join city as ci on ci.Id = st.CityId

----------------------------------------------------------
create view v_station
AS
	select
		st.Id,
		st.StationNumber,
		st.StationName,
		st.CityId,
		ci.CityName,
		st.Address,
		st.Remark,
		st.CreateTime,
		st.ModifyTime,
		st.Work
	from station as st
		inner join city as ci on ci.Id = st.CityId

----------------------------------------------------------
create view v_user_dashboard
as
	select
		ud.Id,
		ud.UserName, 
		ud.WeatherLike, 
		ud.ModifyTime,
		ud.Clock,
		ud.VillageId, 
		vi.VillageName,
		vi.CityId,
		ci.CityName
	from user_dashboard as ud
		inner join village as vi on vi.Id = ud.VillageId 
		inner join city as ci on ci.Id = vi.CityId;

----------------------------------------------------------
create view v_village
AS
	select
		vi.Id,
		vi.CityId,
		ci.CityName,
		vi.VillageName,
		ci.DayAPIId,
		ci.WeekAPIID 
	from village as vi
		inner join city as ci on ci.Id = vi.CityId;

----------------------------------------------------------