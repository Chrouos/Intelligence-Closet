CREATE TABLE node_graph
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	UpperId bigint,--��Ӧ�clothes�����
	LowerId bigint,--��Ӧ�clothes�����
	OtherId bigint,
	UserLike bigint,-- �ϥΪ̳ߦn��
	Postion bigint,-- ��m
	CreateTime datetime NOT NULL,--��J�ɶ�
	ModifyTime datetime NOT NULL,
);
