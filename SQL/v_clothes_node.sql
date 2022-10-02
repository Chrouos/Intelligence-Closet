-- dbo.v_clothes_node source

-- dbo.v_clothes_node source

-- dbo.v_clothes_node source

-- dbo.v_clothes_node source

-- dbo.v_clothes_node source

CREATE view v_clothes_node
as
	SELECT
		cn.Id,
		cn.Position,
		cn.SubCategoryId,
		sc.Name as SubCategoryName,
		sc.CategoryId,
		sc.Score ,
		categorys.CategoryName ,
		cn.ColorId ,
		colors.ColorEngName ,
		colors.ColorName ,
		cn.UserPreferences ,
		cn.WarmLevel ,
		cn.ClothesStyle ,
		cn.UsageCounter ,
		cn.CreateTime ,
		cn.ModifyTime ,
		cn.FilePosition ,
		cn.IsFavorite
	from clothes_node cn
		inner join sub_category sc on sc.Id = cn.SubCategoryId
		inner join category categorys on categorys.Id = sc.CategoryId
		inner join color colors on colors.Id = cn.ColorId;