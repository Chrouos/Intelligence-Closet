CREATE TABLE node_graph
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	UpperId bigint,--串來自clothes的資料
	LowerId bigint,--串來自clothes的資料
	OtherId bigint,
	UserLike bigint,-- 使用者喜好度
	Postion bigint,-- 位置
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
);
