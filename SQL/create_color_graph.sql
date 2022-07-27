drop table color_graph

create table color_graph
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,
	-- �s�� ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL,
	-- �C��t��1
	ColorId2 bigint NOT NULL,
	-- �C��t��2
	ColorScore float NOT NULL
	-- �t�����
);

select *
from color_graph

insert color_graph
values
	(5, 5, 1)
--�� �� 1
insert color_graph
values
	(5, 6, 3)
--�� �� 3
insert color_graph
values
	(5, 7, 4)
--�� �� 4
insert color_graph
values
	(5, 8, 3.5)
--�� �� 3.5
insert color_graph
values
	(5, 2, 2)
--�� �� 2
insert color_graph
values
	(5, 9, 3.5)
--�� �� 3.5
insert color_graph
values
	(5, 3, 4)
--�� �� 4
insert color_graph
values
	(5, 10, 4)
--�� �� 0
insert color_graph
values
	(5, 4, 4)
--�� �� 2.5

insert color_graph
values
	(6, 5, 3)
--�� �� 3
insert color_graph
values
	(6, 6, 2)
--�� �� 2
insert color_graph
values
	(6, 7, 3.5)
--�� �� 3.5
insert color_graph
values
	(6, 8, 1)
--�� �� 1
insert color_graph
values
	(6, 2, 0)
--�� �� 0
insert color_graph
values
	(6, 9, 2)
--�� �� 2
insert color_graph
values
	(6, 3, 3)
--�� �� 3
insert color_graph
values
	(6, 10, 0)
--�� �� 0
insert color_graph
values
	(6, 4, 4)
--�� �� 4

insert color_graph
values
	(7, 5, 4)
--�� �� 4
insert color_graph
values
	(7, 6, 4.5)
--�� �� 4.5
insert color_graph
values
	(7, 7, 3)
--�� �� 3
insert color_graph
values
	(7, 8, 3)
--�� �� 3
insert color_graph
values
	(7, 2, 1)
--�� �� 1
insert color_graph
values
	(7, 9, 0)
--�� �� 0
insert color_graph
values
	(7, 3, 3)
--�� �� 3
insert color_graph
values
	(7, 10, 0)
--�� �� 0
insert color_graph
values
	(7, 4, 4)
--�� �� 4

insert color_graph
values
	(8, 5, 3.5)
--�� �� 3.5
insert color_graph
values
	(8, 6, 1)
--�� �� 1
insert color_graph
values
	(8, 7, 3)
--�� �� 3
insert color_graph
values
	(8, 8, 2)
--�� �� 2
insert color_graph
values
	(8, 2, 3.5)
--�� �� 3.5
insert color_graph
values
	(8, 9, 0)
--�� �� 0
insert color_graph
values
	(8, 3, 3)
--�� �� 3
insert color_graph
values
	(8, 10, 2)
--�� �� 2
insert color_graph
values
	(8, 4, 3)
--�� �� 3

insert color_graph
values
	(2, 5, 2)
--�� �� 2
insert color_graph
values
	(2, 6, 0)
--�� �� 0
insert color_graph
values
	(2, 7, 1)
--�� �� 1
insert color_graph
values
	(2, 8, 3)
--�� �� 3
insert color_graph
values
	(2, 2, 4)
--�� �� 4
insert color_graph
values
	(2, 9, 4.5)
--�� �� 4.5
insert color_graph
values
	(2, 3, 4.5)
--�� �� 4.5
insert color_graph
values
	(2, 10, 2)
--�� �� 2
insert color_graph
values
	(2, 4, 5)
--�� �� 5

insert color_graph
values
	(9, 5, 3.5)
--�� �� 3.5
insert color_graph
values
	(9, 6, 1)
--�� �� 1
insert color_graph
values
	(9, 7, 3)
--�� �� 3
insert color_graph
values
	(9, 8, 2)
--�� �� 2
insert color_graph
values
	(9, 2, 3.5)
--�� �� 3.5
insert color_graph
values
	(9, 9, 0)
--�� �� 0
insert color_graph
values
	(9, 3, 3)
--�� �� 3
insert color_graph
values
	(9, 10, 2)
--�� �� 2
insert color_graph
values
	(9, 4, 3)
--�� �� 3

insert color_graph
values
	(3, 5, 0)
--�� �� 0
insert color_graph
values
	(3, 6, 0)
--�� �� 0
insert color_graph
values
	(3, 7, 0)
--�� �� 0
insert color_graph
values
	(3, 8, 0)
--�� �� 0
insert color_graph
values
	(3, 2, 1)
--�� �� 1
insert color_graph
values
	(3, 9, 1)
--�� �� 1
insert color_graph
values
	(3, 3, 5)
--�� �� 5
insert color_graph
values
	(3, 10, 4.5)
--�� �� 4.5
insert color_graph
values
	(3, 4, 4.5)
--�� �� 4.5

insert color_graph
values
	(10, 5, 0)
--�� �� 0
insert color_graph
values
	(10, 6, 0)
--�� �� 0
insert color_graph
values
	(10, 7, 0)
--�� �� 0
insert color_graph
values
	(10, 8, 0)
--�� �� 0
insert color_graph
values
	(10, 2, 3)
--�� �� 3
insert color_graph
values
	(10, 9, 3)
--�� �� 3
insert color_graph
values
	(10, 3, 4.5)
--�� �� 4.5
insert color_graph
values
	(10, 10, 5)
--�� �� 5
insert color_graph
values
	(10, 4, 4)
--�� �� 4

insert color_graph
values
	(4, 5, 4.5)
--�� �� 4.5
insert color_graph
values
	(4, 6, 3)
--�� �� 3
insert color_graph
values
	(4, 7, 3)
--�� �� 3
insert color_graph
values
	(4, 8, 2)
--�� �� 2
insert color_graph
values
	(4, 2, 3)
--�� �� 3
insert color_graph
values
	(4, 9, 2.5)
--�� �� 2.5
insert color_graph
values
	(4, 3, 4)
--�� �� 4
insert color_graph
values
	(4, 10, 5)
--�� �� 5
insert color_graph
values
	(4, 4, 3.5) --�� �� 3.5
