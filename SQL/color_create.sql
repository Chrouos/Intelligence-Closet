drop table color

create table color(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- �s�� ( 1, 2, 3 ... )
	ColorEngName varchar(30)�@NOT NULL, -- �C��W��(�^�媩��)
	ColorName nvarchar(30)-- �C��W��(���媩��)

);

select * from color

insert color values ('Undefined', NULL)
insert color values ('BLUE', '�Ŧ�')
insert color values ('BLACK', '�¦�')
insert color values ('WHITE', '�զ�')
insert color values ('RED', '����')
insert color values ('ORANGE', '���')
insert color values ('YELLOW', '����')
insert color values ('GREEN', '���')
insert color values ('PURPLE', '����')

