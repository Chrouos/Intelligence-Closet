drop table clothes_graph

create table clothes_graph(
	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- �s�� ( 1, 2, 3 ... )
	ClothesId1 bigint NOT NULL, -- ��A1��
	ClothesId2 bigint NOT NULL, -- ��A2��
	CombScore bigint -- �զX����
);

TRUNCATE TABLE clothes_graph

INSERT INTO clothes_graph(ClothesId1, ClothesId2) select Id,1 from clothes_information where CategoryId = 2

DELETE clothes_graph WHERE Id = 3

select * from clothes_graph