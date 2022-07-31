drop view v_clothes_graph

CREATE view v_clothes_graph
as
	select
		ROW_NUMBER() OVER (ORDER BY cn2.Id ASC) as ViewId,
		cn1.Id as Clothes1Id,
		cn2.Id as Clothes2Id,
		cn1.Position as Clothes1Position,
		cn2.Position as Clothes2Position,
		sc1.CategoryId as Clothes1CategoryId,
		sc2.CategoryId as Clothes2CategoryId,
		sc1.Name as Clothes1ClothesName,
		sc2.Name as Clothes2ClothesName,
		sc1.Score as Clothes1WS,
		sc2.Score as Clothes2WS,
		cg.ColorScore as ColorScore,
		cn1.ColorId as Clothes1Color,
		cn2.ColorId as Clothes2Color,
		c1.ColorName as Clothes1ColorName,
		c2.ColorName as Clothes2ColorName,
		coalesce(sc1.Score, 0) + coalesce(sc2.Score, 0) as AdaptationScore,
		cn1.UserPreferences as Clothes1UserPreferences,
		cn2.UserPreferences as Clothes2UserPreferences,
		coalesce(cn1.UserPreferences, 0) + coalesce(cn2.UserPreferences, 0) as TotalPreferences
	from clothes_node as cn2
		inner join sub_category as sc2 on sc2.Id = cn2.SubCategoryId and (sc2.CategoryId = 1 or sc2.CategoryId = 2)
		inner join clothes_node as cn1 on sc2.CategoryId != 2
		inner join sub_category as sc1 on sc1.Id = cn1.SubCategoryId and sc1.CategoryId != 8 and sc2.CategoryId != 8 and sc1.CategoryId != sc2.CategoryId and (sc1.CategoryId = 1 or sc1.CategoryId = 2)
		inner join color_graph  as cg on cg.ColorId1 = cn1.ColorId and cg.ColorId2 = cn2.ColorId
		inner join color 		as c1 on c1.Id = cn1.ColorId
		inner join color		as c2 on c2.Id  = cn2.ColorId
;


select *
from v_clothes_graph
