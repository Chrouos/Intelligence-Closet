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

------------------------------------------------------------------------------- 

create table sub_category
(
    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    CategoryId bigint NOT NULL,-- 衣物分類( 0, 1, 2 )
    ClothesType varchar(255) NOT NULL,--衣物種類 ( short, long skirt... )
    Score bigint NOT NULL,-- 天氣分數(衣物本身的保暖程度)
    Name nvarchar(255)-- 衣物名稱
);
INSERT INTO intelligence_closet.dbo.sub_category
    (CategoryId,ClothesType,Score,Name)
VALUES
    (4, N'Blazer', 3, N'西裝外套'),
    (3, N'Dress', 3, N'洋裝'),
    (1, N'Top', 2, N'上半身'),
    (6, N'Hat', 1, N'帽子'),
    (1, N'Hoodie', 4, N'連帽衫'),
    (1, N'Longsleeve', 4, N'長袖'),
    (4, N'Outwear', 4, N'外套'),
    (2, N'Pants', 3, N'褲子'),
    (1, N'Polo', 2, N'Polo衫'),
    (1, N'Shirt', 2, N'襯衫');
INSERT INTO intelligence_closet.dbo.sub_category
    (CategoryId,ClothesType,Score,Name)
VALUES
    (7, N'Shoes', 1, N'鞋'),
    (2, N'Shorts', 1, N'短褲'),
    (2, N'Skirt', 1, N'裙子'),
    (1, N'T-Shirt', 2, N'T恤'),
    (1, N'Undershirt', 1, N'薄衫'),
    (8, N'Not_sure', 0, NULL);


-------------------------------------------------------------------------------    
create table city
(
    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- ½s¸¹ ( 1, 2, 3 ... )
    CityName varchar(50)-- «°Âí¦WºÙ
);

-------------------------------------------------------------------------------

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

-------------------------------------------------------------------------------

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

INSERT INTO intelligence_closet.dbo.clothes_node
    ([Position],SubCategoryId,ColorId,UserPreferences,ClothesStyle,UsageCounter,CreateTime,ModifyTime,FilePosition)
VALUES
    (0, 4, N'10', NULL, NULL, 0, '2022-08-09 14:28:18.243', '2022-08-09 14:28:18.243', N'./public/src/clothes_1.jpg'),
    (1, 13, N'2', NULL, NULL, 0, '2022-08-09 14:43:40.777', '2022-08-09 14:43:40.777', N'./public/src/clothes_2.jpg'),
    (2, 14, N'4', NULL, NULL, 0, '2022-08-09 14:47:25.72', '2022-08-09 14:47:25.72', N'./public/src/clothes_3.jpg'),
    (3, 12, N'9', NULL, NULL, 0, '2022-08-09 14:51:09.427', '2022-08-09 14:51:09.427', N'./public/src/clothes_4.jpg'),
    (4, 10, N'6', NULL, NULL, 0, '2022-08-09 14:57:05.37', '2022-08-09 14:57:05.37', N'./public/src/clothes_5.jpg'),
    (5, 6, N'3', NULL, NULL, 0, '2022-08-09 20:27:27.657', '2022-08-09 20:27:27.657', N'./public/src/clothes_6.jpg');

-------------------------------------------------------------------------------
create table color
(

    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    ColorEngName varchar(30) NOT NULL,-- 顏色名稱(英文版本)
    ColorName nvarchar(30)-- 顏色名稱(中文版本)

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

-------------------------------------------------------------------------------

create table color_graph
(

    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    ColorId1 bigint NOT NULL,-- 顏色配對1
    ColorId2 bigint NOT NULL,-- 顏色配對2
    ColorScore float NOT NULL-- 配對分數
);

select *
from color_graph

insert color_graph
values
    (5, 5, 1)--紅 紅 1
insert color_graph
values
    (5, 6, 3)--紅 橘 3
insert color_graph
values
    (5, 7, 4)--紅 黃 4
insert color_graph
values
    (5, 8, 3.5)--紅 綠 3.5
insert color_graph
values
    (5, 2, 2)--紅 藍 2
insert color_graph
values
    (5, 9, 3.5)--紅 紫 3.5
insert color_graph
values
    (5, 3, 4)--紅 黑 4
insert color_graph
values
    (5, 10, 4)--紅 灰 0
insert color_graph
values
    (5, 4, 4)--紅 白 2.5
insert color_graph
values
    (5, 11, 4)--紅 米白 2.5
insert color_graph
values
    (5, 12, 4)--紅 軍綠 0
insert color_graph
values
    (5, 13, 4)--紅 卡其 3

insert color_graph
values
    (6, 5, 3)--橘 紅 3
insert color_graph
values
    (6, 6, 2)--橘 橘 2
insert color_graph
values
    (6, 7, 3.5)--橘 黃 3.5
insert color_graph
values
    (6, 8, 1)--橘 綠 1
insert color_graph
values
    (6, 2, 0)--橘 藍 0
insert color_graph
values
    (6, 9, 2)--橘 紫 2
insert color_graph
values
    (6, 3, 3)--橘 黑 3
insert color_graph
values
    (6, 10, 0)--橘 灰 0
insert color_graph
values
    (6, 4, 4)--橘 白 4
insert color_graph
values
    (6, 11, 4)--橘 米白 2.5
insert color_graph
values
    (6, 12, 4)--橘 軍綠 0
insert color_graph
values
    (6, 13, 4)--橘 卡其 3

insert color_graph
values
    (7, 5, 4)--黃 紅 4
insert color_graph
values
    (7, 6, 4.5)--黃 橘 4.5
insert color_graph
values
    (7, 7, 3)--黃 黃 3
insert color_graph
values
    (7, 8, 3)--黃 綠 3
insert color_graph
values
    (7, 2, 1)--黃 藍 1
insert color_graph
values
    (7, 9, 0)--黃 紫 0
insert color_graph
values
    (7, 3, 3)--黃 黑 3
insert color_graph
values
    (7, 10, 0)--黃 灰 0
insert color_graph
values
    (7, 4, 4)--黃 白 4
insert color_graph
values
    (7, 11, 4)--黃 米白 4.5
insert color_graph
values
    (7, 12, 4)--黃 軍綠 3
insert color_graph
values
    (7, 13, 4)--黃 卡其 4.5

insert color_graph
values
    (8, 5, 3.5)--綠 紅 3.5
insert color_graph
values
    (8, 6, 1)--綠 橘 1
insert color_graph
values
    (8, 7, 3)--綠 黃 3
insert color_graph
values
    (8, 8, 2)--綠 綠 2
insert color_graph
values
    (8, 2, 3.5)--綠 藍 3.5
insert color_graph
values
    (8, 9, 0)--綠 紫 0
insert color_graph
values
    (8, 3, 3)--綠 黑 3
insert color_graph
values
    (8, 10, 2)--綠 灰 2
insert color_graph
values
    (8, 4, 3)--綠 白 3
insert color_graph
values
    (8, 11, 4)--綠 米白 3
insert color_graph
values
    (8, 12, 4)--綠 軍綠 4
insert color_graph
values
    (8, 13, 4)--綠 卡其 1.5

insert color_graph
values
    (2, 5, 2)--藍 紅 2
insert color_graph
values
    (2, 6, 0)--藍 橘 0
insert color_graph
values
    (2, 7, 1)--藍 黃 1
insert color_graph
values
    (2, 8, 3)--藍 綠 3
insert color_graph
values
    (2, 2, 4)--藍 藍 4
insert color_graph
values
    (2, 9, 4.5)--藍 紫 4.5
insert color_graph
values
    (2, 3, 4.5)--藍 黑 4.5
insert color_graph
values
    (2, 10, 2)--藍 灰 2
insert color_graph
values
    (2, 4, 5)--藍 白 5
insert color_graph
values
    (2, 11, 4)--藍 米白 4.5
insert color_graph
values
    (2, 12, 4)--藍 軍綠 2
insert color_graph
values
    (2, 13, 4)--藍 卡其 2.5

insert color_graph
values
    (9, 5, 3.5)--紫 紅 3.5
insert color_graph
values
    (9, 6, 1)--紫 橘 1
insert color_graph
values
    (9, 7, 3)--紫 黃 3
insert color_graph
values
    (9, 8, 2)--紫 綠 2
insert color_graph
values
    (9, 2, 3.5)--紫 藍 3.5
insert color_graph
values
    (9, 9, 0)--紫 紫 0
insert color_graph
values
    (9, 3, 3)--紫 黑 3
insert color_graph
values
    (9, 10, 2)--紫 灰 2
insert color_graph
values
    (9, 4, 3)--紫 白 3
insert color_graph
values
    (9, 11, 4)--紫 米白 3
insert color_graph
values
    (9, 12, 4)--紫 軍綠 0
insert color_graph
values
    (9, 13, 4)--紫 卡其 0

insert color_graph
values
    (3, 5, 0)--黑 紅 0
insert color_graph
values
    (3, 6, 0)--黑 橘 0
insert color_graph
values
    (3, 7, 0)--黑 黃 0
insert color_graph
values
    (3, 8, 0)--黑 綠 0
insert color_graph
values
    (3, 2, 1)--黑 藍 1
insert color_graph
values
    (3, 9, 1)--黑 紫 1
insert color_graph
values
    (3, 3, 5)--黑 黑 5
insert color_graph
values
    (3, 10, 4.5)--黑 灰 4.5
insert color_graph
values
    (3, 4, 4.5)--黑 白 4.5
insert color_graph
values
    (3, 11, 4)--黑 米白 4
insert color_graph
values
    (3, 12, 4)--黑 軍綠 4
insert color_graph
values
    (3, 13, 4)--黑 卡其 3.5

insert color_graph
values
    (10, 5, 0)--灰 紅 0
insert color_graph
values
    (10, 6, 0)--灰 橘 0
insert color_graph
values
    (10, 7, 0)--灰 黃 0
insert color_graph
values
    (10, 8, 0)--灰 綠 0
insert color_graph
values
    (10, 2, 3)--灰 藍 3
insert color_graph
values
    (10, 9, 3)--灰 紫 3
insert color_graph
values
    (10, 3, 4.5)--灰 黑 4.5
insert color_graph
values
    (10, 10, 5)--灰 灰 5
insert color_graph
values
    (10, 4, 4)--灰 白 4
insert color_graph
values
    (10, 11, 4)--灰 米白 4.5
insert color_graph
values
    (10, 12, 4)--灰 軍綠 2
insert color_graph
values
    (10, 13, 4)--灰 卡其 3.5

insert color_graph
values
    (4, 5, 4.5)--白 紅 4.5
insert color_graph
values
    (4, 6, 3)--白 橘 3
insert color_graph
values
    (4, 7, 3)--白 黃 3
insert color_graph
values
    (4, 8, 2)--白 綠 2
insert color_graph
values
    (4, 2, 3)--白 藍 3
insert color_graph
values
    (4, 9, 2.5)--白 紫 2.5
insert color_graph
values
    (4, 3, 4)--白 黑 4
insert color_graph
values
    (4, 10, 5)--白 灰 5
insert color_graph
values
    (4, 4, 3.5)--白 白 3.5
insert color_graph
values
    (4, 11, 4)--白 米白 2.5
insert color_graph
values
    (4, 12, 4)--白 軍綠 3
insert color_graph
values
    (4, 13, 4)--白 卡其 5

insert color_graph
values
    (11, 5, 0)--米白 紅 0
insert color_graph
values
    (11, 6, 0)--米白 橘 0
insert color_graph
values
    (11, 7, 1)--米白 黃 1
insert color_graph
values
    (11, 8, 0)--米白 綠 0
insert color_graph
values
    (11, 2, 0)--米白 藍 0
insert color_graph
values
    (11, 9, 0)--米白 紫 0
insert color_graph
values
    (11, 3, 4.5)--米白 黑 4.5
insert color_graph
values
    (11, 10, 4)--米白 灰 4
insert color_graph
values
    (11, 4, 3.5)--米白 白 3.5
insert color_graph
values
    (11, 11, 3)--米白 米白 3
insert color_graph
values
    (11, 12, 2)--米白 軍綠 2
insert color_graph
values
    (11, 13, 4)--米白 卡其 4

insert color_graph
values
    (12, 5, 0)--軍綠 紅 0
insert color_graph
values
    (12, 6, 0)--軍綠 橘 0
insert color_graph
values
    (12, 7, 0)--軍綠 黃 0
insert color_graph
values
    (12, 8, 0)--軍綠 綠 0
insert color_graph
values
    (12, 2, 0)--軍綠 藍 0
insert color_graph
values
    (12, 9, 0)--軍綠 紫 0
insert color_graph
values
    (12, 3, 4.5)--軍綠 黑 4.5
insert color_graph
values
    (12, 10, 2)--軍綠 灰 2
insert color_graph
values
    (12, 4, 4)--軍綠 白 4.5
insert color_graph
values
    (12, 11, 3)--軍綠 米白 3
insert color_graph
values
    (12, 12, 2.5)--軍綠 軍綠 2.5
insert color_graph
values
    (12, 13, 4)--軍綠 卡其 4

insert color_graph
values
    (13, 5, 0)--卡其 紅 0
insert color_graph
values
    (13, 6, 0)--卡其 橘 0
insert color_graph
values
    (13, 7, 2.5)--卡其 黃 2
insert color_graph
values
    (13, 8, 1)--卡其 綠 1
insert color_graph
values
    (13, 2, 0)--卡其 藍 0
insert color_graph
values
    (13, 9, 0)--卡其 紫 0
insert color_graph
values
    (13, 3, 5)--卡其 黑 5
insert color_graph
values
    (13, 10, 4)--卡其 灰 4
insert color_graph
values
    (13, 4, 4.5)--卡其 白 4.5
insert color_graph
values
    (13, 11, 4)--卡其 米白 4
insert color_graph
values
    (13, 12, 1)--卡其 軍綠 1
insert color_graph
values
    (13, 13, 2.5)--卡其 卡其 2.5


-------------------------------------------------------------------------------

CREATE TABLE user_combs
(
    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    Clothes1Id bigint,--串來自clothes的資料
    Clothes2Id bigint,--串來自clothes的資料
    UserLike bigint,-- 使用者喜好度
    CreateTime datetime NOT NULL,--放入時間
    ModifyTime datetime NOT NULL,
);
-------------------------------------------------------------------------------
create table user_dashboard
(
    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    UserName nvarchar(50) Null,--使用者名稱
    WeatherLike Int Not Null,--喜歡的天氣(5為最熱)
    ModifyTime datetime Not Null,--異動時間
    StationName nvarchar (50) Null,--可以記錄使用者目前所在城市
    Clock datetime,-- StationName, CityName 地區
);
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

create view v_category_clothes
as
    select
        ws.Id,
        ws.CategoryId,
        cat.CategoryName,
        ws.ClothesType,
        ws.Score,
        ws.Name,
        cat.Level
    from sub_category as ws
        inner join category as cat on cat.Id = ws.CategoryId

-------------------------------------------------------------------------------
CREATE view v_clothes_graph
as
    select
        ROW_NUMBER() OVER (ORDER BY cn2.Id ASC) as ViewId,
        cn1.Id as Clothes1Id,
        cn2.Id as Clothes2Id,
        cn1.Position as Clothes1Position,
        cn2.Position as Clothes2Position,
        sc1.CategoryId as Clothes1CategoryId,
        sc2.CategoryId as Clothes2CategoryId,
        sc1.Name as Clothes1ClothesName,
        sc2.Name as Clothes2ClothesName,
        sc1.Score as Clothes1WS,
        sc2.Score as Clothes2WS,
        cg.ColorScore as ColorScore,
        cn1.ColorId as Clothes1Color,
        cn2.ColorId as Clothes2Color,
        c1.ColorName as Clothes1ColorName,
        c2.ColorName as Clothes2ColorName,
        coalesce(sc1.Score, 0) + coalesce(sc2.Score, 0) as AdaptationScore,
        cn1.UserPreferences as Clothes1UserPreferences,
        cn2.UserPreferences as Clothes2UserPreferences,
        coalesce(cn1.UserPreferences, 0) + coalesce(cn2.UserPreferences, 0) as TotalPreferences
    from clothes_node as cn2
        inner join sub_category as sc2 on sc2.Id = cn2.SubCategoryId and (sc2.CategoryId = 1 or sc2.CategoryId = 2)
        inner join clothes_node as cn1 on sc2.CategoryId != 2
        inner join sub_category as sc1 on sc1.Id = cn1.SubCategoryId and sc1.CategoryId != 8 and sc2.CategoryId != 8 and sc1.CategoryId != sc2.CategoryId and (sc1.CategoryId = 1 or sc1.CategoryId = 2)
        inner join color_graph  as cg on cg.ColorId1 = cn1.ColorId and cg.ColorId2 = cn2.ColorId
        inner join color 		as c1 on c1.Id = cn1.ColorId
        inner join color		as c2 on c2.Id  = cn2.ColorId;
-------------------------------------------------------------------------------
create view v_clothes_node
as
    select
        ci.Id,
        ci.Position,
        ci.SubCategoryId as ClothesId,
        sc.Name,
        sc.ClothesType,
        ci.ColorId,
        color.ColorName,
        ci.UserPreferences,
        sc.CategoryId,
        ci.ClothesStyle,
        ci.UsageCounter,
        ci.CreateTime,
        ci.ModifyTime,
        ci.FilePosition,
        sc.Score,
        cat.Level
    from clothes_node as ci
        inner join sub_category as sc on ci.SubCategoryId = sc.Id
        inner join category as cat on cat.Id = sc.CategoryId
        inner join color as color on ci.ColorId = color.Id
-------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------
create table clothes_graph
(
    Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
    ClothesId1 bigint NOT NULL,-- 衣服1號
    ClothesId2 bigint NOT NULL,-- 衣服2號
    CombScore bigint-- 組合分數
);
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
-------------------------------------------------------------------------------
