drop table color_graph

create table color_graph(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- �s�� ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL, -- �C��t��1
	ColorId2 bigint NOT NULL, -- �C��t��2
	ColorScore float NOT NULL -- �t�����
);

select * from color_graph

insert color_graph values (5, 5, 1)�@-- ex1. ��	��	1
insert color_graph values (5, 8, 3.5)�@-- ex2. �� ��	3.5
