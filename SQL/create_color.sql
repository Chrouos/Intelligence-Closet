drop table color

create table color
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	ColorEngName varchar(30) NOT NULL,-- 顏色名稱(英文)
	ColorName nvarchar(30)-- 顏色名稱(中文)

);

select *
from color

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
