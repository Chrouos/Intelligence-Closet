drop table color

create table color
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	ColorEngName varchar(30) NOT NULL,-- �C��W��(�^�媩��)
	ColorName nvarchar(30)-- �C��W��(���媩��)

);

select *
from color

insert color
values
	('Undefined', NULL)--1
insert color
values
	('BLUE', '�Ŧ�')--2
insert color
values
	('BLACK', '�¦�')--3
insert color
values
	('WHITE', '�զ�')--4
insert color
values
	('RED', '����')--5
insert color
values
	('ORANGE', '���')--6
insert color
values
	('YELLOW', '����')--7
insert color
values
	('GREEN', '���')--8
insert color
values
	('PURPLE', '����')--9
insert color
values
	('GRAY', '�Ǧ�')--10
insert color
values
	('CREAMY WHITE', '�̥զ�')--11
insert color
values
	('ARMY GREEN', '�x���')--12
insert color
values
	('KHAKI', '�d���')--13
