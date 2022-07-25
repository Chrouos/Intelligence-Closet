drop table city

create table city(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	CityName varchar(50) -- 城鎮名稱
);

-- INSERT INTO city VALUES ('新北市')

SELECT * FROM city

SELECT * FROM city WHERE CityName = '桃園市'

SELECT * FROM city Where CityName = '新北市'