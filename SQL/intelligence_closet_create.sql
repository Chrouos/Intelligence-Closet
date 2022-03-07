drop table clothes_infomation

create table clothes_infomation(
	position int PRIMARY KEY NOT NULL , -- 儲存位置 ( 1, 2, 3 ... )
	category varchar(50) NOT NULL,  -- 衣物分類( upper, lower... )
	color varchar(50) NOT NULL, 
	weather_score int NOT NULL, -- 衣物天氣分數
	clothes_type VARCHAR(255) NOT NULL, --衣物種類 ( short, long ... )
	clothes_style VARCHAR(255) NULL, -- 衣物風格
	usageCounter int NOT NULL, 
	createTime smalldatetime NOT NULL
);