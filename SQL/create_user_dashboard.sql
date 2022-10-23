-- 負責儲存使用者自己的使用習慣，例如比較怕冷或是怕熱，喜歡穿什麼類型的衣物，使用習慣等等。
drop table user_dashboard

create table user_dashboard
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	UserName nvarchar(50) Null,--使用者名稱
	WeatherLike int Not Null,--喜歡的天氣(5為最熱)
	ModifyTime datetime Not Null,--異動時間
	CityId bigint,
	VilageName nvarchar (50) Null,--可以記錄使用者目前所在鄉鎮區
	Clock datetime,
	-- StationName, CityName 地區
	-- TODO: 把程式碼內(包含資料庫的)staionName改成VilageName
	-- TODO: weatherController 內也要改API 

);

select *
from user_dashboard

insert into user_dashboard
VALUES
	('DiuDu', 5, GETDATE(), 0, GETDATE(), 0)