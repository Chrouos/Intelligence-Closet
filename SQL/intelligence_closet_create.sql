drop table clothes_infomation

create table clothes_infomation(
	position int PRIMARY KEY NOT NULL , -- �x�s��m ( 1, 2, 3 ... )
	category varchar(50) NOT NULL,  -- �窫����( upper, lower... )
	color varchar(50) NOT NULL, 
	weather_score int NOT NULL, -- �窫�Ѯ����
	clothes_type VARCHAR(255) NOT NULL, --�窫���� ( short, long ... )
	clothes_style VARCHAR(255) NULL, -- �窫����
	usageCounter int NOT NULL, 
	createTime smalldatetime NOT NULL
);