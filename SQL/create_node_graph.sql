CREATE TABLE intelligence_closet.dbo.node_graph
(
	Id bigint IDENTITY(1,1) NOT NULL,
	UpperId bigint NULL,-- �W�b���窫Id
	LowerId bigint NULL,-- �U�b���窫Id
	OtherId bigint NULL,-- ��L�窫Id
	UserLike bigint NULL,-- �ϥΪ̳ߦn��
	CreateTime datetime NOT NULL,
	ModifyTime datetime NOT NULL,
	CONSTRAINT PK__node_gra__3214EC0755D155C9 PRIMARY KEY (Id)
);