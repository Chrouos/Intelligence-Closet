DROP TABLE user_clothes

CREATE TABLE user_clothes(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- 編號 ( 1, 2, 3 ... )
	ClothesId bigint, --串來自clothes的資料
	UserLike bigint, -- 使用者喜好度
	CreateTime datetime NOT NULL,--放入時間
	ModifyTime datetime NOT NULL,
);

