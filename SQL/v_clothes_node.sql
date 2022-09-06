drop view v_clothes_node

-- dbo.v_clothes_node source

-- dbo.v_clothes_information source

create view v_clothes_node
as
	select
		cn.Id,
		cn.Position,
		cn.SubCategoryId as ClothesId,
		sc.Name,
		sc.ClothesType,
		cn.ColorId,
		color.ColorName,
		cn.UserPreferences,
		sc.CategoryId,
		cn.ClothesStyle,
		cn.UsageCounter,
		cn.CreateTime,
		cn.ModifyTime,
		cn.FilePosition,
		sc.Score,
		cat.Level
	from clothes_node as cn
		inner join sub_category as sc on cn.SubCategoryId = sc.Id
		inner join category as cat on cat.Id = sc.CategoryId
		inner join color as color on cn.ColorId = color.Id


select *
from v_clothes_node
