create table user_dashboard
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,
	-- �s�� ( 1, 2, 3 ... )
	UserName nvarchar(50) Null,
	--�ϥΪ̦W��
	WeatherLike Int Not Null,
	--���w���Ѯ�(5���̼�)
	ModifyTime datetime Not Null,
	--���ʮɶ�
	NowCity nvarchar (50) Null,
	--�i�H�O���ϥΪ̥ثe�Ҧb����

	-- StationName, CityName �a��
);

select *
from user_dashboard