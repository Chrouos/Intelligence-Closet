
CREATE view v_clothes_graph
as
	select
		vcn_u.Id as UpperClothesId,
		vcn_u.[Position] as UpperPosition,
		vcn_u.SubCategoryId as UpperSubCategory,
		vcn_u.ColorId as upperColorId,
		vcn_u.UserPreferences as upperUserPreferences,
		vcn_u.FilePosition as upperFilePosition,
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
		-- vcn_o.IsFavorite as OtherIsFavorite

		coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalPreferences,
		-- coalesce(vcn_u.UserPreferences, 0) + coalesce(vcn_l.UserPreferences, 0) + coalesce(vcn_o.UserPreferences, 0) as TotalColorCombs
		ng.UserLike
	from
		node_graph ng
		inner join v_clothes_node vcn_u on vcn_u.CategoryId = 1 and ng.UpperId = vcn_u.Id
		inner join v_clothes_node vcn_l on vcn_l.CategoryId = 2 and ng.LowerId  = vcn_u.Id
		inner join v_clothes_node vcn_o on vcn_o.CategoryId != 1 and vcn_u.CategoryId != 2 and ng.OtherId = vcn_o.Id 