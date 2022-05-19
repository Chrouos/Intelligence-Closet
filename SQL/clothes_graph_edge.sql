drop table clothes_graph_edge

create table clothes_graph_edge(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- 編號 ( 1, 2, 3 ... )
	Clothes1Position int Not Null, -- 衣服一號位置
	Clothes2Position int Not Null, -- 衣服二號位置
	AdaptationScore	bigint Null, -- 總分
	Clothes1Preferences	int Null, -- 衣服一使用者喜好
	Clothes2Preferences	int	Null, -- 衣服二使用者喜好
	TotalPreferences int Null, -- 喜好程度總分

);

select * from clothes_graph_edge

