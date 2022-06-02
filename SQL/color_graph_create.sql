drop table color_graph

create table color_graph(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- 編號 ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL, -- 顏色配對1
	ColorId2 bigint NOT NULL, -- 顏色配對2
	ColorScore bigint NOT NULL -- 配對分數
);

select * from color_graph

insert color_graph values (2, 2, 3)　-- ex1. 藍色配藍色 3分
insert color_graph values (2, 8, 3)　-- ex2. 藍色配綠色 3分
insert color_graph values (5, 5, 4)　 
insert color_graph values (3, 4, 5)　