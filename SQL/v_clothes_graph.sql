-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

-- dbo.v_clothes_graph source

CREATE view v_clothes_graph as
select * from(
select 
	ROW_NUMBER() OVER (ORDER BY coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0 + ng.UserLike) DESC) as Id,

	vcn_u.Id as UpperClothesId, 
	vcn_u.[Position] as UpperPosition,
	vcn_u.SubCategoryId as UpperSubCategory,
	vcn_u.ColorId as UpperColorId,
	vcn_u.UserPreferences as UpperUserPreferences,
	vcn_u.FilePosition as UpperFilePosition,
	
	-- vcn_u.IsFavorite as upperIsFavorite,
	
	vcn_l.Id as LowerClothesId, 
	vcn_l.[Position] as LowerPosition,
	vcn_l.SubCategoryId as LowerSubCategory,
	vcn_l.ColorId as LowerColorId,
	vcn_l.UserPreferences as LowerUserPreferences,
	vcn_l.FilePosition as LowerFilePosition,
	
	-- vcn_l.IsFavorite as LowerIsFavorite,
	
	 vcn_o.Id as OtherClothesId, 
	 vcn_o.[Position] as OtherPosition,
	 vcn_o.SubCategoryId as OtherSubCategory,
	 vcn_o.ColorId as OtherColorId,
	 vcn_o.UserPreferences as OtherUserPreferences,
	 vcn_o.FilePosition as OtherFilePosition,
	 
--	 vcn_o.IsFavorite as OtherIsFavorite
	
	coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalPreferences,
	-- 	coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalColorCombs,
	ng.UserLike, -- 權重須加重
	-- 天氣分數
	coalesce(vcn_u.Score, 0) + coalesce(vcn_l.Score, 0) + coalesce(vcn_o.Score, 0) as TotalScore,
	vcg.ColorScore
	
from 
	node_graph ng  
left join v_clothes_node vcn_u on vcn_u.CategoryId = 1 and ng.UpperId = vcn_u.Id  
left join v_clothes_node vcn_l on vcn_l.CategoryId = 2 and ng.LowerId  = vcn_l.Id 
left join v_clothes_node vcn_o on vcn_o.CategoryId != 1 and vcn_o.CategoryId != 2 and ng.OtherId = vcn_o.Id
left join v_color_graph vcg on vcg.UpperColorId = vcn_u.ColorId and vcg.LowerColorId = vcn_l.ColorId
) as merge_graph
WHERE ((LowerClothesId is not null and LowerPosition is not null)  and  (UpperClothesId is not null and UpperPosition is not null))
or (OtherClothesId is not null and OtherPosition is not null);