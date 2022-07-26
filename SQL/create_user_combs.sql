DROP TABLE user_combs

CREATE TABLE user_combs(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	Clothes1Id bigint, --串來自clothes的資料
	Clothes2Id bigint, --串來自clothes的資料
	UserLike bigint, -- 使用者喜好度
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
);

