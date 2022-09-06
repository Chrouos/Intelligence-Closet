drop view v_category_clothes

create view v_category_clothes
as
	select
		sc.Id,
		sc.CategoryId,
		cat.CategoryName,
		sc.ClothesType,
		sc.Score,
		sc.Name,
		cat.Level
	from sub_category as sc
		inner join category as cat on cat.Id = sc.CategoryId

select *
from v_category_clothes

select *
from sub_category

select *
from category
