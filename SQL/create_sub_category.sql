drop table sub_category;

create table sub_category
(
	Id bigint PRIMARY KEY NOT NULL IDENTITY,-- �s�� ( 1, 2, 3 ... )
	CategoryId bigint NOT NULL,-- �窫����( 0, 1, 2 )
	ClothesType varchar(255) NOT NULL,--�窫���� ( short, long skirt... )
	Score bigint NOT NULL,-- �Ѯ����(�窫�������O�x�{��)
	Name nvarchar(255)-- �窫�W��
);


INSERT INTO sub_category
VALUES(4, 'Blazer', 3, '��˥~�M')

INSERT INTO sub_category
VALUES(3, 'Dress', 3, '�v��')

INSERT INTO sub_category
VALUES(1, 'Top', 2, '�W�b��')

INSERT INTO sub_category
VALUES(6, 'Hat', 1, '�U�l')

INSERT INTO sub_category
VALUES(1, 'Hoodie', 4, '�s�U�m')

INSERT INTO sub_category
VALUES(1, 'Longsleeve', 3, '���S')

INSERT INTO sub_category
VALUES(4, 'Outwear', 3, '�~�M')

INSERT INTO sub_category
VALUES(2, 'Pants', 3, '�Ǥl')

INSERT INTO sub_category
VALUES(1, 'Polo', 2, 'Polo�m')

INSERT INTO sub_category
VALUES(1, 'Shirt', 2, 'Ũ�m')

INSERT INTO sub_category
VALUES(7, 'Shoes', 1, '�c')

INSERT INTO sub_category
VALUES(2, 'Shorts', 1, '�u��')

INSERT INTO sub_category
VALUES(2, 'Skirt', 1, '�Ȥl')

INSERT INTO sub_category
VALUES(1, 'T-Shirt', 2, 'T��')

INSERT INTO sub_category
VALUES(1, 'Undershirt', 1, 'T��')

INSERT INTO sub_category
VALUES(8, 'Not_sure', 0, Null)


select *
from sub_category;


