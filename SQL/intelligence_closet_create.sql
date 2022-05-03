drop table clothes_information

create table clothes_information
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	Position int Unique,-- ��b���d�̭�����m( 0 ~ 9)
	Category varchar(50) NOT NULL,-- �窫����( upper, lower... ) => ���G
	Color varchar(50) NOT NULL,-- �窫�C�� => ���G
	-- WeatherScore int NOT NULL,-- �窫�Ѯ���� 
	UserPreferences int NULL,-- �ϥΪ̳ߦn�{�� (0~10)
	ClothesType varchar(255) NOT NULL,--�窫���� ( short_TShirt, long_skirt... ) => ���G
	ClothesStyle varchar(255) NULL,-- �窫���� => ���G
	UsageCounter int NOT NULL,-- �窫�ϥΦ���
	CreateTime datetime NOT NULL,--��J�ɶ�
	ModifyTime datetime NOT NULL,
	FilePosition text--�Ϥ���m
);

select * from clothes_information


insert into clothes_information (Category, Color, ClothesType, UsageCounter, CreateTime, ModifyTime) VALUES('upper', 'blue', 'short_TShirt', 0, GETDATE(), GETDATE() )

