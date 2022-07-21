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



select *
from clothes_information


INSERT INTO clothes_information
VALUES (0, 16, '3', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_1.jpg')

INSERT INTO clothes_information
VALUES( 1, 14, '2', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_2.jpg')

INSERT INTO clothes_information
VALUES( 2, 6, '3', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_3.jpg')

INSERT INTO clothes_information
VALUES
	( 3, 8, '4', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_4.jpg')

INSERT INTO clothes_information
VALUES(4, 8, '4', Null, Null, 0, '2022-6-26', '2022-6-26', 'UI/web/public/src/clothes_5.jpg')
