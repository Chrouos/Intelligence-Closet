
CREATE view v_clothes_graph
as
	select
		ucn.Id as upperClothesId,
		ucn.[Position] as upperPosition,
		ucn.SubCategoryId as upperSubCategory,
		ucn.ColorId as upperColorId,
		ucn.UserPreferences as upperUserPreferences,
		ucn.ClothesStyle as upperClothesStyle,
		ucn.FilePosition as upperFilePosition,
		ucn.IsFavorite as upperIsFavorite,
		lcn.Id as lowerClothesId,
		lcn.[Position] as lowerPosition,
		lcn.SubCategoryId as lowerSubCategory,
		lcn.ColorId as lowerColorId,
		lcn.UserPreferences as lowerUserPreferences,
		lcn.ClothesStyle as lowerClothesStyle,
		lcn.FilePosition as lowerFilePosition,
		lcn.IsFavorite as lowerIsFavorite,
		ng.Postion as ngPosition
	from
		node_graph ng
		inner join clothes_node_lower lcn on ng.LowerId = lcn.Id
		inner join clothes_node_upper ucn on ng.UpperId = ucn.Id;