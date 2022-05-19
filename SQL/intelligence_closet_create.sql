drop table clothes_information

create table clothes_information
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	Position int,-- ��b���d�̭�����m( 0 ~ 9)
	WeatherScoreId	bigint NOT NULL,-- �窫����( 0, 1... ) => ���G
	Color varchar(50) NOT NULL,-- �窫�C�� => ���G
	-- WeatherScore int NOT NULL,-- �窫�Ѯ���� 
	UserPreferences int NULL,-- �ϥΪ̳ߦn�{�� (0~10)
	CategoryId bigint NOT NULL,--�窫���� ( weather_score.id ) => ���G
	ClothesStyle varchar(255) NULL,-- �窫���� => ���G
	UsageCounter int NOT NULL,-- �窫�ϥΦ���
	CreateTime datetime NOT NULL,--��J�ɶ�
	ModifyTime datetime NOT NULL,
	FilePosition text--�Ϥ���m
);

insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(2, 'blue', 1, 0, GETDATE(), GETDATE() )
insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(2, 'red',  2, 0, GETDATE(), GETDATE() )


insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(1, 'blue', 4, 0, GETDATE(), GETDATE() )
insert into clothes_information (CategoryId, Color, WeatherScoreId, UsageCounter, CreateTime, ModifyTime) VALUES(1, 'black',5, 0, GETDATE(), GETDATE() )

select *
from clothes_information
