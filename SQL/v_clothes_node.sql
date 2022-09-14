-- dbo.v_clothes_node source

-- dbo.v_clothes_node source

-- dbo.v_clothes_node source

CREATE view v_clothes_node
as
	SELECT
		ROW_NUMBER() OVER (ORDER BY A.ClothesNodeId) as Id,
		Position,
		SubCategoryId,
		SubCategoryName,
		CategoryId,
		Score ,
		CategoryName ,
		ColorId ,
		ColorEngName ,
		ColorName ,
		UserPreferences ,
		WarmLevel ,
		ClothesStyle ,
		UsageCounter ,
		CreateTime ,
		ModifyTime ,
		FilePosition ,
		IsFavorite
	FROM
		(
										select
				cnu.Id as ClothesNodeId,
				cnu.Position,
				cnu.SubCategoryId,
				sc_u.Name as SubCategoryName,
				sc_u.CategoryId,
				sc_u.Score ,
				category_u.CategoryName ,
				cnu.ColorId ,
				color_u.ColorEngName ,
				color_u.ColorName ,
				cnu.UserPreferences ,
				cnu.WarmLevel ,
				cnu.ClothesStyle ,
				cnu.UsageCounter ,
				cnu.CreateTime ,
				cnu.ModifyTime ,
				cnu.FilePosition ,
				cnu.IsFavorite
			from clothes_node_upper cnu
				inner join sub_category sc_u on sc_u.Id = cnu.SubCategoryId
				inner join category category_u on category_u.Id = sc_u.CategoryId
				inner join color color_u on color_u.Id = cnu.ColorId
		UNION all
			select
				cnl.Id as ClothesNodeId,
				cnl.Position,
				cnl.SubCategoryId,
				sc_l.Name as SubCategoryName,
				sc_l.CategoryId,
				sc_l.Score ,
				category_l.CategoryName ,
				cnl.ColorId ,
				color_l.ColorEngName ,
				color_l.ColorName ,
				cnl.UserPreferences ,
				cnl.WarmLevel ,
				cnl.ClothesStyle ,
				cnl.UsageCounter ,
				cnl.CreateTime ,
				cnl.ModifyTime ,
				cnl.FilePosition ,
				cnl.IsFavorite
			from clothes_node_lower cnl
				inner join sub_category sc_l on sc_l.Id = cnl.SubCategoryId
				inner join category category_l on category_l.Id = sc_l.CategoryId
				inner join color color_l on color_l.Id = cnl.ColorId
		UNION all
			select
				cno.Id as ClothesNodeId,
				cno.Position,
				cno.SubCategoryId,
				sc_o.Name as SubCategoryName,
				sc_o.CategoryId,
				sc_o.Score ,
				category_o.CategoryName ,
				cno.ColorId ,
				color_o.ColorEngName ,
				color_o.ColorName ,
				cno.UserPreferences ,
				cno.WarmLevel ,
				cno.ClothesStyle ,
				cno.UsageCounter ,
				cno.CreateTime ,
				cno.ModifyTime ,
				cno.FilePosition ,
				cno.IsFavorite
			from clothes_node_other cno
				inner join sub_category sc_o on sc_o.Id = cno.SubCategoryId
				inner join category category_o on category_o.Id = sc_o.CategoryId
				inner join color color_o on color_o.Id = cno.ColorId
)	A