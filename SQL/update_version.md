
## 20221004
+ 為了新版的抓取資料
```sql

drop table city

create table city
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- ½s¸¹ ( 1, 2, 3 ... )
	CityName varchar(50)-- «°Âí¦WºÙ
);

insert into city
values
	('宜蘭縣')

insert into city
values
	('桃園市')
	
insert into city
values
	('新竹縣')

insert into city
values
	('苗栗縣')
	
insert into city
values
	('彰化縣')

insert into city
values
	('南投縣')
	
insert into city
values
	('雲林縣')

insert into city
values
	('嘉義縣')
	
insert into city
values
	('屏東縣')

insert into city
values
	('臺東縣')
	
insert into city
values
	('花蓮縣')

insert into city
values
	('澎湖縣')
	
insert into city
values
	('基隆市')

insert into city
values
	('新竹市')
	
insert into city
values
	('嘉義市')

insert into city
values
	('臺北市')

insert into city
values
	('高雄市')
	
insert into city
values
	('新北市')
	
insert into city
values
	('臺中市')

insert into city
values
	('臺南市')
	
insert into city
values
	('連江縣')

insert into city
values
	('金門縣')

create table village (
	Id bigint PRIMARY KEY NOT NULL IDENTITY,
	CityId bigint NOT NULL,
	VillageName varchar(50)
);

insert into village
values
	(1,'頭城鎮'),(1,'礁溪鄉'),(1,'壯圍鄉'),(1,'員山鄉'),(1,'宜蘭市'),(1,'大同鄉'),(1,'五結鄉'),(1,'三星鄉'),
	(1,'羅東鎮'),(1,'冬山鄉'),(1,'南澳鄉'),(1,'蘇澳鎮')

insert into village
values
	(2,'大園區'),(2,'蘆竹區'),(2,'觀音區'),(2,'龜山區'),(2,'桃園區'),(2,'中壢區'),(2,'新屋區'),(2,'八德區'),
	(2,'平鎮區'),(2,'楊梅區'),(2,'大溪區'),(2,'龍潭區'),(2,'復興區')

insert into village
values
	(3,'新豐鄉'),(3,'湖口鄉'),(3,'新埔鎮'),(3,'竹北市'),(3,'關西鎮'),(3,'芎林鄉'),(3,'竹東鎮'),(3,'寶山鄉'),
	(3,'尖石鄉'),(3,'橫山鄉'),(3,'北埔鄉'),(3,'峨眉鄉'),(3,'五峰鄉')
	
insert into village
values
	(4,'竹南鎮'),(4,'頭份市'),(4,'三灣鄉'),(4,'造橋鄉'),(4,'後龍鎮'),(4,'南庄鄉'),(4,'頭屋鄉'),(4,'獅潭鄉'),
	(4,'苗栗市'),(4,'西湖鄉'),(4,'通霄鎮'),(4,'公館鄉'),(4,'銅鑼鄉'),(4,'泰安鄉'),(4,'苑裡鎮'),(4,'大湖鄉'),
	(4,'三義鄉'),(4,'卓蘭鎮')
	
insert into village
values
	(5,'伸港鄉'),(5,'和美鎮'),(5,'線西鄉'),(5,'鹿港鎮'),(5,'彰化市'),(5,'秀水鄉'),(5,'福興鄉'),(5,'花壇鄉'),
	(5,'芬園鄉'),(5,'芳苑鄉'),(5,'埔鹽鄉'),(5,'大村鄉'),(5,'二林鎮'),(5,'員林市'),(5,'溪湖鎮'),(5,'埔心鄉'),
	(5,'永靖鄉'),(5,'社頭鄉'),(5,'埤頭鄉'),(5,'田尾鄉'),(5,'大城鄉'),(5,'田中鎮'),(5,'北斗鎮'),(5,'竹塘鄉'),
	(5,'溪州鄉'),(5,'二水鄉')

insert into village
values
	(6,'仁愛鄉'),(6,'國姓鄉'),(6,'埔里鎮'),(6,'草屯鎮'),(6,'中寮鄉'),(6,'南投市'),(6,'魚池鄉'),(6,'水里鄉'),
	(6,'名間鄉'),(6,'信義鄉'),(6,'集集鎮'),(6,'竹山鎮'),(6,'鹿谷鄉')
	
insert into village
values
	(7,'麥寮鄉'),(7,'二崙鄉'),(7,'崙背鄉'),(7,'西螺鎮'),(7,'莿桐鄉'),(7,'林內鄉'),(7,'臺西鄉'),(7,'土庫鎮'),
	(7,'虎尾鎮'),(7,'褒忠鄉'),(7,'東勢鄉'),(7,'斗南鎮'),(7,'四湖鄉'),(7,'古坑鄉'),(7,'元長鄉'),(7,'大埤鄉'),
	(7,'口湖鄉'),(7,'北港鎮'),(7,'水林鄉'),(7,'斗六市')

insert into village
values
	(8,'大林鎮'),(8,'溪口鄉'),(8,'阿里山鄉'),(8,'梅山鄉'),(8,'新港鄉'),(8,'民雄鄉'),(8,'六腳鄉'),(8,'竹崎鄉'),
	(8,'東石鄉'),(8,'太保市'),(8,'番路鄉'),(8,'朴子市'),(8,'水上鄉'),(8,'中埔鄉'),(8,'布袋鎮'),(8,'鹿草鄉'),
	(8,'義竹鄉'),(8,'大埔鄉')

insert into village
values
	(9,'高樹鄉'),(9,'三地門鄉'),(9,'霧臺鄉'),(9,'里港鄉'),(9,'鹽埔鄉'),(9,'九如鄉'),(9,'長治鄉'),(9,'瑪家鄉'),
	(9,'屏東市'),(9,'內埔鄉'),(9,'麟洛鄉'),(9,'泰武鄉'),(9,'萬巒鄉'),(9,'竹田鄉'),(9,'萬丹鄉'),(9,'來義鄉'),
	(9,'潮州鎮'),(9,'新園鄉'),(9,'崁頂鄉'),(9,'新埤鄉'),(9,'南州鄉'),(9,'東港鎮'),(9,'林邊鄉'),(9,'佳冬鄉'),
	(9,'春日鄉'),(9,'獅子鄉'),(9,'琉球鄉'),(9,'枋山鄉'),(9,'牡丹鄉'),(9,'滿州鄉'),(9,'車城鄉'),(9,'恆春鎮'),
	(9,'枋寮鄉')

insert into village
values
	(10,'長濱鄉'),(10,'海端鄉'),(10,'池上鄉'),(10,'成功鎮'),(10,'關山鎮'),(10,'東河鄉'),(10,'鹿野鄉'),(10,'延平鄉'),
	(10,'卑南鄉'),(10,'臺東市'),(10,'太麻里鄉'),(10,'綠島鄉'),(10,'達仁鄉'),(10,'大武鄉'),(10,'蘭嶼鄉'),(10,'金峰鄉')

insert into village
values
	(11,'秀林鄉'),(11,'新城鄉'),(11,'花蓮市'),(11,'吉安鄉'),(11,'壽豐鄉'),(11,'萬榮鄉'),(11,'鳳林鎮'),(11,'豐濱鄉'),
	(11,'光復鄉'),(11,'卓溪鄉'),(11,'瑞穗鄉'),(11,'玉里鎮'),(11,'富里鄉')

insert into village
values
	(12,'白沙鄉'),(12,'西嶼鄉'),(12,'湖西鄉'),(12,'馬公市'),(12,'望安鄉'),(12,'七美鄉')

insert into village
values
	(13,'安樂區'),(13,'中山區'),(13,'中正區'),(13,'七堵區'),(13,'信義區'),(13,'仁愛區'),(13,'暖暖區')

insert into village
values
	(14,'北區'),(14,'香山區'),(14,'東區')

insert into village
values
	(15,'東區'),(15,'西區')

insert into village
values
	(16,'北投區'),(16,'士林區'),(16,'內湖區'),(16,'中山區'),(16,'大同區'),(16,'松山區'),(16,'南港區'),(16,'中正區'),
	(16,'萬華區'),(16,'信義區'),(16,'大安區'),(16,'文山區')	

insert into village
values
	(17,'楠梓區'),(17,'左營區'),(17,'三民區'),(17,'鼓山區'),(17,'苓雅區'),(17,'新興區'),(17,'前金區'),(17,'鹽埕區'),
	(17,'前鎮區'),(17,'旗津區'),(17,'小港區'),(17,'那瑪夏區'),(17,'甲仙區'),(17,'六龜區'),(17,'杉林區'),(17,'內門區'),
	(17,'茂林區'),(17,'美濃區'),(17,'旗山區'),(17,'田寮區'),(17,'湖內區'),(17,'茄萣區'),(17,'阿蓮區'),(17,'路竹區'),
	(17,'永安區'),(17,'岡山區'),(17,'燕巢區'),(17,'彌陀區'),(17,'橋頭區'),(17,'大樹區'),(17,'梓官區'),(17,'大社區'),
	(17,'仁武區'),(17,'鳥松區'),(17,'大寮區'),(17,'鳳山區'),(17,'林園區'),(17,'桃源區')

insert into village
values
	(18,'石門區'),(18,'三芝區'),(18,'金山區'),(18,'淡水區'),(18,'萬里區'),(18,'八里區'),(18,'汐止區'),(18,'林口區'),
	(18,'五股區'),(18,'瑞芳區'),(18,'蘆洲區'),(18,'雙溪區'),(18,'三重區'),(18,'貢寮區'),(18,'平溪區'),(18,'泰山區'),
	(18,'新莊區'),(18,'石碇區'),(18,'板橋區'),(18,'深坑區'),(18,'永和區'),(18,'樹林區'),(18,'中和區'),(18,'土城區'),
	(18,'新店區'),(18,'坪林區'),(18,'鶯歌區'),(18,'三峽區'),(18,'烏來區')

insert into village
values
	(19,'北屯區'),(19,'西屯區'),(19,'北區'),(19,'南屯區'),(19,'西區'),(19,'東區'),(19,'中區'),(19,'南區'),
	(19,'和平區'),(19,'大甲區'),(19,'大安區'),(19,'外埔區'),(19,'后里區'),(19,'清水區'),(19,'東勢區'),(19,'神岡區'),
	(19,'龍井區'),(19,'石岡區'),(19,'豐原區'),(19,'梧棲區'),(19,'新社區'),(19,'沙鹿區'),(19,'大雅區'),(19,'潭子區'),
	(19,'大肚區'),(19,'太平區'),(19,'烏日區'),(19,'大里區'),(19,'霧峰區')

insert into village
values
	(20,'安南區'),(20,'中西區'),(20,'安平區'),(20,'東區'),(20,'南區'),(20,'北區'),(20,'白河區'),(20,'後壁區'),
	(20,'鹽水區'),(20,'新營區'),(20,'東山區'),(20,'北門區'),(20,'柳營區'),(20,'學甲區'),(20,'下營區'),(20,'六甲區'),
	(20,'南化區'),(20,'將軍區'),(20,'楠西區'),(20,'麻豆區'),(20,'官田區'),(20,'佳里區'),(20,'大內區'),(20,'七股區'),
	(20,'玉井區'),(20,'善化區'),(20,'西港區'),(20,'山上區'),(20,'安定區'),(20,'新市區'),(20,'左鎮區'),(20,'新化區'),
	(20,'永康區'),(20,'歸仁區'),(20,'關廟區'),(20,'龍崎區'),(20,'仁德區')

insert into village
values
	(21,'南竿鄉'),(21,'北竿鄉'),(21,'莒光鄉'),(21,'東引鄉')

insert into village
values
	(22,'金城鎮'),(22,'金湖鎮'),(22,'金沙鎮'),(22,'金寧鄉'),(22,'烈嶼鄉'),(22,'烏坵鄉')

```


+ 補充粉紅色 米白跟軍綠拿掉
```sql

drop table color

create table color
(

    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    ColorEngName varchar(30) NOT NULL,-- 顏色名稱(英文)
    ColorName nvarchar(30)-- 顏色名稱(中文)

);


insert color
values
    ('Undefined', ' ')--1
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
    ('PINK', '粉紅色')--11
insert color
values
    ('CYAN', '青色') --12
    

select *
from color


```


----


## 20221002

```sql
drop view v_color_graph
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
		inner join color as c2 on c2.Id = cg.ColorId2;

drop view v_clothes_node
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
		inner join color colors on colors.Id = cn.ColorId;

drop view v_clothes_graph
CREATE view v_clothes_graph
as
	select
		ROW_NUMBER() OVER (ORDER BY coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0 + ng.UserLike) DESC) as Id,

		vcn_u.Id as UpperClothesId,
		vcn_u.[Position] as UpperPosition,
		vcn_u.SubCategoryId as UpperSubCategory,
		vcn_u.ColorId as UpperColorId,
		vcn_u.UserPreferences as UpperUserPreferences,
		vcn_u.FilePosition as UpperFilePosition,

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

		--	 vcn_o.IsFavorite as OtherIsFavorite

		coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalPreferences,
		vcg.ColorScore,
		-- 	coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalColorCombs,
		ng.UserLike
	-- 權重須加重

	from
		node_graph ng
		left join v_clothes_node vcn_u on vcn_u.CategoryId = 1 and ng.UpperId = vcn_u.Id
		left join v_clothes_node vcn_l on vcn_l.CategoryId = 2 and ng.LowerId  = vcn_l.Id
		left join v_clothes_node vcn_o on vcn_o.CategoryId != 1 and vcn_o.CategoryId != 2 and ng.OtherId = vcn_o.Id
		left join v_color_graph vcg on vcg.UpperColorId = vcn_u.ColorId and vcg.LowerColorId = vcn_l.ColorId;


```


---
## 20220919

增加clothes_node
作用是為了不要拆表，全部都用同一張表來做存儲
```sql
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

INSERT INTO intelligence_closet.dbo.clothes_node
	([Position], SubCategoryId, ColorId, UserPreferences, ClothesStyle, UsageCounter, CreateTime, ModifyTime, FilePosition, IsFavorite, WarmLevel)
VALUES(10, 11, 3, 0, '', 0, GETDATE(), GETDATE(), './public/src/clothes_8.jpg', 0, 0);
```

讓所有衣物分成上半身、下半身、其他並做計算
```sql
drop view v_clothes_graph



CREATE view v_clothes_graph as
select 
	ROW_NUMBER() OVER (ORDER BY coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0 + ng.UserLike) DESC) as Id,

	vcn_u.Id as UpperClothesId, 
	vcn_u.[Position] as UpperPosition,
	vcn_u.SubCategoryId as UpperSubCategory,
	vcn_u.ColorId as UpperColorId,
	vcn_u.UserPreferences as UupperUserPreferences,
	vcn_u.FilePosition as UupperFilePosition,
	
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
	 
--	 vcn_o.IsFavorite as OtherIsFavorite
	
	coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalPreferences,
	-- coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalColorCombs
	ng.UserLike -- 權重須加重
	
from 
	node_graph ng  
left join v_clothes_node vcn_u on vcn_u.CategoryId = 1 and ng.UpperId = vcn_u.Id 
left join v_clothes_node vcn_l on vcn_l.CategoryId = 2 and ng.LowerId  = vcn_l.Id 
left join v_clothes_node vcn_o on vcn_o.CategoryId != 1 and vcn_o.CategoryId != 2 and ng.OtherId = vcn_o.Id;

```

整理節點的資料
```sql
drop view v_clothes_node

CREATE view v_clothes_node as
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

```

新增graph假資料
```sql
TRUNCATE TABLE node_graph

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 7, null, -1, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 8, null, -1, GETDATE(), GETDATE());


INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 7, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 8, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 7, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 8, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 7, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 8, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(null, null, 9, 2, GETDATE(), GETDATE());
```
-----