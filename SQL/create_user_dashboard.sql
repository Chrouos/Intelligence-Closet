drop table user_dashboard

create table user_dashboard
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	UserName nvarchar(50) Null,--使用者名稱
	WeatherLike int Not Null,--喜歡的天氣(5為最熱)
	ModifyTime datetime Not Null,--異動時間
	StationName nvarchar (50) Null,--可以記錄使用者目前所在城市
	Clock datetime,
	-- StationName, CityName 地區
	CityId bigint
);

select *
from user_dashboard

insert into user_dashboard
VALUES ('DiuDu', 5, GETDATE(), 0, GETDATE(), 0)