drop table user_dashboard

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
	StationName nvarchar (50) Null,
	--�i�H�O���ϥΪ̥ثe�Ҧb����
	Clock datetime, 

	-- StationName, CityName �a��
);

select *
from user_dashboard