CREATE TABLE intelligence_closet.dbo.node_graph
(
	Id bigint IDENTITY(1,1) NOT NULL,
	UpperId bigint NULL,-- 上半身衣物Id
	LowerId bigint NULL,-- 下半身衣物Id
	OtherId bigint NULL,-- 其他衣物Id
	UserLike bigint NULL,-- 使用者喜好度
	CreateTime datetime NOT NULL,
	ModifyTime datetime NOT NULL,
	CONSTRAINT PK__node_gra__3214EC0755D155C9 PRIMARY KEY (Id)
);