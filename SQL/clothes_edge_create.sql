--drop table clothes_edge

create table clothes_edge(
	position_A int NOT NULL , -- 儲存位置 ( 1, 2, 3 ... )
	position_B int NOT NULL , -- 儲存位置 ( 1, 2, 3 ... )
	weights int
);