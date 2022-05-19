drop view v_category_clothes

create view v_category_clothes
as
select
	ws.Id,
	ws.CategoryId,
	cat.CategoryName,
	ws.ClothesType,
	ws.Score,
	ws.Name,
	cat.Level
from weather_score as ws
	inner join category as cat on cat.Id = ws.CategoryId

select * from v_category_clothes

select *
from weather_score

select *
from category
