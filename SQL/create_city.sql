drop table city

create table city(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	CityName varchar(50) -- ����W��
);

-- INSERT INTO city VALUES ('�s�_��')

SELECT * FROM city

SELECT * FROM city WHERE CityName = '��饫'

SELECT * FROM city Where CityName = '�s�_��'