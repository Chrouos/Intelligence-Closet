DROP TABLE user_combs

CREATE TABLE user_combs(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	Clothes1Id bigint, --��Ӧ�clothes�����
	Clothes2Id bigint, --��Ӧ�clothes�����
	UserLike bigint, -- �ϥΪ̳ߦn��
	CreateTime datetime NOT NULL,-- �|
	ModifyTime datetime NOT NULL,
);


