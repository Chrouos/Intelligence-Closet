drop table color_graph

create table color_graph(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- �s�� ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL, -- �C��t��1
	ColorId2 bigint NOT NULL, -- �C��t��2
	ColorScore bigint NOT NULL -- �t�����
);

select * from color_graph

insert color_graph values (2, 2, 3)�@-- ex1. �Ŧ�t�Ŧ� 3��
insert color_graph values (2, 8, 3)�@-- ex2. �Ŧ�t��� 3��
insert color_graph values (5, 5, 4)�@ 
insert color_graph values (3, 4, 5)�@