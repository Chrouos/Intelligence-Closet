DROP TABLE user_clothes

CREATE TABLE user_clothes(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	ClothesId bigint, --��Ӧ�clothes�����
	UserLike bigint, -- �ϥΪ̳ߦn��
	CreateTime datetime NOT NULL,--��J�ɶ�
	ModifyTime datetime NOT NULL,
);

