-- �t�d�x�s�ϥΪ̦ۤv���ϥβߺD�A�Ҧp����ȧN�άO�ȼ��A���w�擄���������窫�A�ϥβߺD�����C
drop table user_dashboard

create table user_dashboard
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	UserName nvarchar(50) Null,--�ϥΪ̦W��
	WeatherLike int Not Null,--���w���Ѯ�(5���̼�)
	ModifyTime datetime Not Null,--���ʮɶ�
	CityId bigint,
	VilageName nvarchar (50) Null,--�i�H�O���ϥΪ̥ثe�Ҧb�m���
	Clock datetime,
	-- StationName, CityName �a��
	-- TODO: ��{���X��(�]�t��Ʈw��)staionName�令VilageName
	-- TODO: weatherController ���]�n��API 

);

select *
from user_dashboard

insert into user_dashboard
VALUES
	('DiuDu', 5, GETDATE(), 0, GETDATE(), 0)