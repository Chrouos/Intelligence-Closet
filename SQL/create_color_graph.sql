drop table color_graph

create table color_graph
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,
	-- ½s¸¹ ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL,
	-- ÃC¦â°t¹ï1
	ColorId2 bigint NOT NULL,
	-- ÃC¦â°t¹ï2
	ColorScore float NOT NULL
	-- °t¹ï¤À¼Æ
);

select *
from color_graph

insert color_graph
values
	(5, 5, 1)
--¬õ ¬õ 1
insert color_graph
values
	(5, 6, 3)
--¬õ ¾ï 3
insert color_graph
values
	(5, 7, 4)
--¬õ ¶À 4
insert color_graph
values
	(5, 8, 3.5)
--¬õ ºñ 3.5
insert color_graph
values
	(5, 2, 2)
--¬õ ÂÅ 2
insert color_graph
values
	(5, 9, 3.5)
--¬õ µµ 3.5
insert color_graph
values
	(5, 3, 4)
--¬õ ¶Â 4
insert color_graph
values
	(5, 10, 4)
--¬õ ¦Ç 0
insert color_graph
values
	(5, 4, 4)
--¬õ ¥Õ 2.5

insert color_graph
values
	(6, 5, 3)
--¾ï ¬õ 3
insert color_graph
values
	(6, 6, 2)
--¾ï ¾ï 2
insert color_graph
values
	(6, 7, 3.5)
--¾ï ¶À 3.5
insert color_graph
values
	(6, 8, 1)
--¾ï ºñ 1
insert color_graph
values
	(6, 2, 0)
--¾ï ÂÅ 0
insert color_graph
values
	(6, 9, 2)
--¾ï µµ 2
insert color_graph
values
	(6, 3, 3)
--¾ï ¶Â 3
insert color_graph
values
	(6, 10, 0)
--¾ï ¦Ç 0
insert color_graph
values
	(6, 4, 4)
--¾ï ¥Õ 4

insert color_graph
values
	(7, 5, 4)
--¶À ¬õ 4
insert color_graph
values
	(7, 6, 4.5)
--¶À ¾ï 4.5
insert color_graph
values
	(7, 7, 3)
--¶À ¶À 3
insert color_graph
values
	(7, 8, 3)
--¶À ºñ 3
insert color_graph
values
	(7, 2, 1)
--¶À ÂÅ 1
insert color_graph
values
	(7, 9, 0)
--¶À µµ 0
insert color_graph
values
	(7, 3, 3)
--¶À ¶Â 3
insert color_graph
values
	(7, 10, 0)
--¶À ¦Ç 0
insert color_graph
values
	(7, 4, 4)
--¶À ¥Õ 4

insert color_graph
values
	(8, 5, 3.5)
--ºñ ¬õ 3.5
insert color_graph
values
	(8, 6, 1)
--ºñ ¾ï 1
insert color_graph
values
	(8, 7, 3)
--ºñ ¶À 3
insert color_graph
values
	(8, 8, 2)
--ºñ ºñ 2
insert color_graph
values
	(8, 2, 3.5)
--ºñ ÂÅ 3.5
insert color_graph
values
	(8, 9, 0)
--ºñ µµ 0
insert color_graph
values
	(8, 3, 3)
--ºñ ¶Â 3
insert color_graph
values
	(8, 10, 2)
--ºñ ¦Ç 2
insert color_graph
values
	(8, 4, 3)
--ºñ ¥Õ 3

insert color_graph
values
	(2, 5, 2)
--ÂÅ ¬õ 2
insert color_graph
values
	(2, 6, 0)
--ÂÅ ¾ï 0
insert color_graph
values
	(2, 7, 1)
--ÂÅ ¶À 1
insert color_graph
values
	(2, 8, 3)
--ÂÅ ºñ 3
insert color_graph
values
	(2, 2, 4)
--ÂÅ ÂÅ 4
insert color_graph
values
	(2, 9, 4.5)
--ÂÅ µµ 4.5
insert color_graph
values
	(2, 3, 4.5)
--ÂÅ ¶Â 4.5
insert color_graph
values
	(2, 10, 2)
--ÂÅ ¦Ç 2
insert color_graph
values
	(2, 4, 5)
--ÂÅ ¥Õ 5

insert color_graph
values
	(9, 5, 3.5)
--µµ ¬õ 3.5
insert color_graph
values
	(9, 6, 1)
--µµ ¾ï 1
insert color_graph
values
	(9, 7, 3)
--µµ ¶À 3
insert color_graph
values
	(9, 8, 2)
--µµ ºñ 2
insert color_graph
values
	(9, 2, 3.5)
--µµ ÂÅ 3.5
insert color_graph
values
	(9, 9, 0)
--µµ µµ 0
insert color_graph
values
	(9, 3, 3)
--µµ ¶Â 3
insert color_graph
values
	(9, 10, 2)
--µµ ¦Ç 2
insert color_graph
values
	(9, 4, 3)
--µµ ¥Õ 3

insert color_graph
values
	(3, 5, 0)
--¶Â ¬õ 0
insert color_graph
values
	(3, 6, 0)
--¶Â ¾ï 0
insert color_graph
values
	(3, 7, 0)
--¶Â ¶À 0
insert color_graph
values
	(3, 8, 0)
--¶Â ºñ 0
insert color_graph
values
	(3, 2, 1)
--¶Â ÂÅ 1
insert color_graph
values
	(3, 9, 1)
--¶Â µµ 1
insert color_graph
values
	(3, 3, 5)
--¶Â ¶Â 5
insert color_graph
values
	(3, 10, 4.5)
--¶Â ¦Ç 4.5
insert color_graph
values
	(3, 4, 4.5)
--¶Â ¥Õ 4.5

insert color_graph
values
	(10, 5, 0)
--¦Ç ¬õ 0
insert color_graph
values
	(10, 6, 0)
--¦Ç ¾ï 0
insert color_graph
values
	(10, 7, 0)
--¦Ç ¶À 0
insert color_graph
values
	(10, 8, 0)
--¦Ç ºñ 0
insert color_graph
values
	(10, 2, 3)
--¦Ç ÂÅ 3
insert color_graph
values
	(10, 9, 3)
--¦Ç µµ 3
insert color_graph
values
	(10, 3, 4.5)
--¦Ç ¶Â 4.5
insert color_graph
values
	(10, 10, 5)
--¦Ç ¦Ç 5
insert color_graph
values
	(10, 4, 4)
--¦Ç ¥Õ 4

insert color_graph
values
	(4, 5, 4.5)
--¥Õ ¬õ 4.5
insert color_graph
values
	(4, 6, 3)
--¥Õ ¾ï 3
insert color_graph
values
	(4, 7, 3)
--¥Õ ¶À 3
insert color_graph
values
	(4, 8, 2)
--¥Õ ºñ 2
insert color_graph
values
	(4, 2, 3)
--¥Õ ÂÅ 3
insert color_graph
values
	(4, 9, 2.5)
--¥Õ µµ 2.5
insert color_graph
values
	(4, 3, 4)
--¥Õ ¶Â 4
insert color_graph
values
	(4, 10, 5)
--¥Õ ¦Ç 5
insert color_graph
values
	(4, 4, 3.5) --¥Õ ¥Õ 3.5
