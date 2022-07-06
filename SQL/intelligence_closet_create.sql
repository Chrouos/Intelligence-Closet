drop table clothes_information

create table clothes_information
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	Position int,-- ��b���d�̭�����m( 0 ~ 9)
	WeatherScoreId bigint NOT NULL,-- �窫����( 0, 1... ) 
	ColorId varchar(50) NOT NULL,-- �窫�C��ID
	-- WeatherScore int NOT NULL,-- �窫�Ѯ���� 
	UserPreferences int NULL,-- �ϥΪ̳ߦn�{�� (0~10)
	-- CategoryId bigint NOT NULL,--�窫���� ( weather_score.id )
	ClothesStyle varchar(255) NULL,-- �窫����
	UsageCounter int NOT NULL,-- �窫�ϥΦ���
	CreateTime datetime NOT NULL,--��J�ɶ�
	ModifyTime datetime NOT NULL,
	FilePosition text--�Ϥ���m
);

TRUNCATE TABLE clothes_information

delete clothes_information where Id = 3


select *
from clothes_information


INSERT INTO clothes_information
VALUES
	(1, 0, 16, '3', None, None, 0, datetime.datetime(2022, 6, 26, 19, 51, 41, 350000), datetime.datetime(2022, 6, 26, 19, 51, 41, 350000), 'UI/web/public/src/clothes_1.jpg')
INSERT INTO clothes_information
VALUES
	(2, 1, 14, '2', None, None, 0, datetime.datetime(2022, 6, 26, 22, 13, 9, 13000), datetime.datetime(2022, 6, 26, 22, 13, 9, 13000), 'UI/web/public/src/clothes_2.jpg')
INSERT INTO clothes_information
VALUES
	(4, 2, 6, '3', None, None, 0, datetime.datetime(2022, 6, 26, 22, 14, 47, 267000), datetime.datetime(2022, 6, 26, 22, 14, 47, 267000), 'UI/web/public/src/clothes_3.jpg')
INSERT INTO clothes_information
VALUES
	(5, 3, 8, '4', None, None, 0, datetime.datetime(2022, 6, 26, 22, 15, 13, 217000), datetime.datetime(2022, 6, 26, 22, 15, 13, 217000), 'UI/web/public/src/clothes_4.jpg')
INSERT INTO clothes_information
VALUES
	(6, 4, 8, '4', None, None, 0, datetime.datetime(2022, 6, 26, 22, 15, 34, 570000), datetime.datetime(2022, 6, 26, 22, 15, 34, 570000), 'UI/web/public/src/clothes_5.jpg')
