drop table clothes_graph_edge

create table clothes_graph_edge(

	Id bigint PRIMARY KEY NOT NULL IDENTITY, -- �s�� ( 1, 2, 3 ... )
	Clothes1Position int Not Null, -- ��A�@����m
	Clothes2Position int Not Null, -- ��A�G����m
	AdaptationScore	bigint Null, -- �`��
	Clothes1Preferences	int Null, -- ��A�@�ϥΪ̳ߦn
	Clothes2Preferences	int	Null, -- ��A�G�ϥΪ̳ߦn
	TotalPreferences int Null, -- �ߦn�{���`��

);

select * from clothes_graph_edge

