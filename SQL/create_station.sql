drop table station

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


select *
from station

select *
from station
where Work != 0