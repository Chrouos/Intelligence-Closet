drop table station

create table station
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	StationNumber varchar(20),-- ����	
	StationName nvarchar(50),-- ���W
	CityId bigint NOT NULL,-- �����s��
	[Address] nvarchar(255),-- �a�}
	Remark nvarchar(255),-- �Ƶ�
	CreateTime date,-- ��ư_�l���
	ModifyTime date,-- ���ʮɶ�
	Work int,-- �O�_�B�@
);


select *
from station

select *
from station
where Work != 0