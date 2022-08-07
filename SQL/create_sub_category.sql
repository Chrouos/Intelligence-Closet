drop table sub_category;

create table sub_category
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	CategoryId bigint NOT NULL,-- 衣物分類( 0, 1, 2 )
	ClothesType varchar(255) NOT NULL,--衣物種類 ( short, long skirt... )
	Score bigint NOT NULL,-- 天氣分數(衣物本身的保暖程度)
	Name nvarchar(255)-- 衣物名稱
);


INSERT INTO sub_category
VALUES(4, 'Blazer', 3, '西裝外套')

INSERT INTO sub_category
VALUES(3, 'Dress', 3, '洋裝')

INSERT INTO sub_category
VALUES(1, 'Top', 2, '上半身')

INSERT INTO sub_category
VALUES(6, 'Hat', 1, '帽子')

INSERT INTO sub_category
VALUES(1, 'Hoodie', 4, '連帽衫')

INSERT INTO sub_category
VALUES(1, 'Longsleeve', 3, '長袖')

INSERT INTO sub_category
VALUES(4, 'Outwear', 3, '外套')

INSERT INTO sub_category
VALUES(2, 'Pants', 3, '褲子')

INSERT INTO sub_category
VALUES(1, 'Polo', 2, 'Polo衫')

INSERT INTO sub_category
VALUES(1, 'Shirt', 2, '襯衫')

INSERT INTO sub_category
VALUES(7, 'Shoes', 1, '鞋')

INSERT INTO sub_category
VALUES(2, 'Shorts', 1, '短褲')

INSERT INTO sub_category
VALUES(2, 'Skirt', 1, '裙子')

INSERT INTO sub_category
VALUES(1, 'T-Shirt', 2, 'T恤')

INSERT INTO sub_category
VALUES(1, 'Undershirt', 1, 'T恤')

INSERT INTO sub_category
VALUES(8, 'Not_sure', 0, Null)


select *
from sub_category;


