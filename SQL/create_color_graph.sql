-- 負責做顏色和顏色之間的搭配，然後儲存互相配對之後的分數。滿分10分，最低至0分。
drop table color_graph

create table color_graph
(

	Id bigint PRIMARY KEY NOT NULL IDENTITY,
	-- 編號 ( 1, 2, 3 ... )
	ColorId1 bigint NOT NULL,
	-- 顏色配對1
	ColorId2 bigint NOT NULL,
	-- 顏色配對2
	ColorScore float NOT NULL
	-- 配對分數
);

select *
from color_graph

insert color_graph
values
	(5, 5, 1)
--紅 紅 1
insert color_graph
values
	(5, 6, 3)
--紅 橘 3
insert color_graph
values
	(5, 7, 4)
--紅 黃 4
insert color_graph
values
	(5, 8, 3.5)
--紅 綠 3.5
insert color_graph
values
	(5, 2, 2)
--紅 藍 2
insert color_graph
values
	(5, 9, 3.5)
--紅 紫 3.5
insert color_graph
values
	(5, 3, 4)
--紅 黑 4
insert color_graph
values
	(5, 10, 4)
--紅 灰 0
insert color_graph
values
	(5, 4, 4)
--紅 白 2.5
insert color_graph
values
	(5, 11, 4)
--紅 粉紅 3
insert color_graph
values
	(5, 12, 0)
--紅 青 0

insert color_graph
values
	(6, 5, 3)
--橘 紅 3
insert color_graph
values
	(6, 6, 2)
--橘 橘 2
insert color_graph
values
	(6, 7, 3.5)
--橘 黃 3.5
insert color_graph
values
	(6, 8, 1)
--橘 綠 1
insert color_graph
values
	(6, 2, 0)
--橘 藍 0
insert color_graph
values
	(6, 9, 2)
--橘 紫 2
insert color_graph
values
	(6, 3, 3)
--橘 黑 3
insert color_graph
values
	(6, 10, 0)
--橘 灰 0
insert color_graph
values
	(6, 4, 4)
--橘 白 4
insert color_graph
values
	(6, 11, 4)
--橘 粉紅 3
insert color_graph
values
	(6, 12, 0)
--橘 青 0

insert color_graph
values
	(7, 5, 4)
--黃 紅 4
insert color_graph
values
	(7, 6, 4.5)
--黃 橘 4.5
insert color_graph
values
	(7, 7, 3)
--黃 黃 3
insert color_graph
values
	(7, 8, 3)
--黃 綠 3
insert color_graph
values
	(7, 2, 1)
--黃 藍 1
insert color_graph
values
	(7, 9, 0)
--黃 紫 0
insert color_graph
values
	(7, 3, 3)
--黃 黑 3
insert color_graph
values
	(7, 10, 0)
--黃 灰 0
insert color_graph
values
	(7, 4, 4)
--黃 白 4
insert color_graph
values
	(7, 11, 4)
--黃 粉紅 4
insert color_graph
values
	(7, 12, 4)
--黃 青 2

insert color_graph
values
	(8, 5, 3.5)
--綠 紅 3.5
insert color_graph
values
	(8, 6, 1)
--綠 橘 1
insert color_graph
values
	(8, 7, 3)
--綠 黃 3
insert color_graph
values
	(8, 8, 2)
--綠 綠 2
insert color_graph
values
	(8, 2, 3.5)
--綠 藍 3.5
insert color_graph
values
	(8, 9, 0)
--綠 紫 0
insert color_graph
values
	(8, 3, 3)
--綠 黑 3
insert color_graph
values
	(8, 10, 2)
--綠 灰 2
insert color_graph
values
	(8, 4, 3)
--綠 白 3
insert color_graph
values
	(8, 11, 4)
--綠 粉紅 0
insert color_graph
values
	(8, 12, 3)
--綠 青 3

insert color_graph
values
	(2, 5, 2)
--藍 紅 2
insert color_graph
values
	(2, 6, 0)
--藍 橘 0
insert color_graph
values
	(2, 7, 1)
--藍 黃 1
insert color_graph
values
	(2, 8, 3)
--藍 綠 3
insert color_graph
values
	(2, 2, 4)
--藍 藍 4
insert color_graph
values
	(2, 9, 4.5)
--藍 紫 4.5
insert color_graph
values
	(2, 3, 4.5)
--藍 黑 4.5
insert color_graph
values
	(2, 10, 2)
--藍 灰 2
insert color_graph
values
	(2, 4, 5)
--藍 白 5
insert color_graph
values
	(2, 11, 4)
--藍 粉紅 2.5
insert color_graph
values
	(2, 12, 3.5)
--藍 青 3.5

insert color_graph
values
	(9, 5, 3.5)
--紫 紅 3.5
insert color_graph
values
	(9, 6, 1)
--紫 橘 1
insert color_graph
values
	(9, 7, 3)
--紫 黃 3
insert color_graph
values
	(9, 8, 2)
--紫 綠 2
insert color_graph
values
	(9, 2, 3.5)
--紫 藍 3.5
insert color_graph
values
	(9, 9, 0)
--紫 紫 0
insert color_graph
values
	(9, 3, 3)
--紫 黑 3
insert color_graph
values
	(9, 10, 2)
--紫 灰 2
insert color_graph
values
	(9, 4, 3)
--紫 白 3
insert color_graph
values
	(9, 11, 4)
--紫 粉紅 3.5
insert color_graph
values
	(9, 12, 2)
--紫 青 2

insert color_graph
values
	(3, 5, 0)
--黑 紅 0
insert color_graph
values
	(3, 6, 0)
--黑 橘 0
insert color_graph
values
	(3, 7, 0)
--黑 黃 0
insert color_graph
values
	(3, 8, 0)
--黑 綠 0
insert color_graph
values
	(3, 2, 1)
--黑 藍 1
insert color_graph
values
	(3, 9, 1)
--黑 紫 1
insert color_graph
values
	(3, 3, 5)
--黑 黑 5
insert color_graph
values
	(3, 10, 4.5)
--黑 灰 4.5
insert color_graph
values
	(3, 4, 4.5)
--黑 白 4.5
insert color_graph
values
	(3, 11, 4)
--黑 粉紅 4
insert color_graph
values
	(3, 12, 4)
--黑 青 3.5

insert color_graph
values
	(10, 5, 0)
--灰 紅 0
insert color_graph
values
	(10, 6, 0)
--灰 橘 0
insert color_graph
values
	(10, 7, 0)
--灰 黃 0
insert color_graph
values
	(10, 8, 0)
--灰 綠 0
insert color_graph
values
	(10, 2, 3)
--灰 藍 3
insert color_graph
values
	(10, 9, 3)
--灰 紫 3
insert color_graph
values
	(10, 3, 4.5)
--灰 黑 4.5
insert color_graph
values
	(10, 10, 5)
--灰 灰 5
insert color_graph
values
	(10, 4, 4)
--灰 白 4
insert color_graph
values
	(10, 11, 4)
--灰 粉紅 3
insert color_graph
values
	(10, 12, 5)
--灰 青 5

insert color_graph
values
	(4, 5, 4.5)
--白 紅 4.5
insert color_graph
values
	(4, 6, 3)
--白 橘 3
insert color_graph
values
	(4, 7, 3)
--白 黃 3
insert color_graph
values
	(4, 8, 2)
--白 綠 2
insert color_graph
values
	(4, 2, 3)
--白 藍 3
insert color_graph
values
	(4, 9, 2.5)
--白 紫 2.5
insert color_graph
values
	(4, 3, 4)
--白 黑 4
insert color_graph
values
	(4, 10, 5)
--白 灰 5
insert color_graph
values
	(4, 4, 3.5)
--白 白 3.5
insert color_graph
values
	(4, 11, 4)
--白 粉紅 4
insert color_graph
values
	(4, 12, 4.5)
--白 青 4.5

insert color_graph
values
	(11, 5, 3.5)
--粉紅 紅 3.5
insert color_graph
values
	(11, 6, 2)
--粉紅 橘 2
insert color_graph
values
	(11, 7, 0)
--粉紅 黃 0
insert color_graph
values
	(11, 8, 0)
--粉紅 綠 0
insert color_graph
values
	(11, 2, 0)
--粉紅 藍 0
insert color_graph
values
	(11, 9, 3)
--粉紅 紫 3
insert color_graph
values
	(11, 3, 5)
--粉紅 黑 5
insert color_graph
values
	(11, 10, 4.5)
--粉紅 灰 4.5
insert color_graph
values
	(11, 4, 3)
--粉紅 白 3
insert color_graph
values
	(11, 11, 2)
--粉紅 粉紅 2
insert color_graph
values
	(11, 12, 0)
--粉紅 青 0

insert color_graph
values
	(12, 5, 3.5)
--青 紅 0
insert color_graph
values
	(12, 6, 2)
--青 橘 0
insert color_graph
values
	(12, 7, 0)
--青 黃 0
insert color_graph
values
	(12, 8, 0)
--青 綠 1
insert color_graph
values
	(12, 2, 0)
--青 藍 2
insert color_graph
values
	(12, 9, 3)
--青 紫 0
insert color_graph
values
	(12, 3, 5)
--青 黑 5
insert color_graph
values
	(12, 10, 4.5)
--青 灰 4.5
insert color_graph
values
	(12, 4, 3)
--青 白 3
insert color_graph
values
	(12, 11, 2)
--青 粉紅 0
insert color_graph
values
	(12, 12, 2) --青 青 2