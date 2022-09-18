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

TRUNCATE TABLE node_graph


INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 7, null, -1, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(1, 8, null, -1, GETDATE(), GETDATE());


INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 7, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(2, 8, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 7, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(3, 8, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 5, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 6, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 7, null, 2, GETDATE(), GETDATE());

INSERT INTO intelligence_closet.dbo.node_graph
	(UpperId, LowerId, OtherId, UserLike, CreateTime, ModifyTime)
VALUES(4, 8, null, 2, GETDATE(), GETDATE());
