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