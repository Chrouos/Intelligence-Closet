drop table color_graph

create table color_graph(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- 編號 ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL, -- 顏色配對1
	ColorId2 bigint NOT NULL, -- 顏色配對2
	ColorScore float NOT NULL -- 配對分數
);

select * from color_graph

insert color_graph values (5, 5, 1)　-- ex1. 紅	紅	1
insert color_graph values (5, 8, 3.5)　-- ex2. 紅 綠	3.5
