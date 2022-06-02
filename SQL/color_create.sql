drop table color

create table color(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- 編號 ( 1, 2, 3 ... )
	ColorEngName varchar(30)　NOT NULL, -- 顏色名稱(英文版本)
	ColorName nvarchar(30)-- 顏色名稱(中文版本)

);

select * from color

insert color values ('Undefined', NULL)
insert color values ('BLUE', '藍色')
insert color values ('BLACK', '黑色')
insert color values ('WHITE', '白色')
insert color values ('RED', '紅色')
insert color values ('ORANGE', '橘色')
insert color values ('YELLOW', '黃色')
insert color values ('GREEN', '綠色')
insert color values ('PURPLE', '紫色')

