drop view v_clothes_node

-- dbo.v_clothes_node source

-- dbo.v_clothes_information source

create view v_clothes_node
as
	select
		ci.Id,
		ci.Position,
		ci.SubCategoryId as ClothesId,
		sc.Name,
		sc.ClothesType,
		ci.ColorId,
		color.ColorName,
		ci.UserPreferences,
		sc.CategoryId,
		ci.ClothesStyle,
		ci.UsageCounter,
		ci.CreateTime,
		ci.ModifyTime,
		ci.FilePosition,
		sc.Score,
		cat.Level
	from clothes_node as ci
		inner join sub_category as sc on ci.SubCategoryId = sc.Id
		inner join category as cat on cat.Id = sc.CategoryId
		inner join color as color on ci.ColorId = color.Id


select *
from v_clothes_node
