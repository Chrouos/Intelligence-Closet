drop table user_dashboard

create table user_dashboard
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	UserName nvarchar(50) Null,--�ϥΪ̦W��
	WeatherLike int Not Null,--���w���Ѯ�(5���̼�)
	ModifyTime datetime Not Null,--���ʮɶ�
	StationName nvarchar (50) Null,--�i�H�O���ϥΪ̥ثe�Ҧb����
	Clock datetime,
	-- StationName, CityName �a��
	CityId bigint
);

select *
from user_dashboard

insert into user_dashboard
VALUES ('DiuDu', 5, GETDATE(), 0, GETDATE(), 0)