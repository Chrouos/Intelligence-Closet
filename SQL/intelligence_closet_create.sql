drop table clothes_information

create table clothes_information(
	id int PRIMARY KEY NOT NULL IDENTITY , -- 編號 ( 1, 2, 3 ... )
	position int Unique,
	category varchar(50) NOT NULL,  -- 衣物分類( upper, lower... )
	color varchar(50) NOT NULL, 
	weather_score int NOT NULL, -- 衣物天氣分數
	clothes_type VARCHAR(255) NOT NULL, --衣物種類 ( short, long ... )
	clothes_style VARCHAR(255) NULL, -- 衣物風格
	usageCounter int NOT NULL, 
	createTime smalldatetime NOT NULL,
	
	filePosition text
);