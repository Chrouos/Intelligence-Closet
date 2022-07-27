drop view v_clothes_graph

CREATE view v_clothes_graph
as
	select
		ROW_NUMBER() OVER (ORDER BY ci2.Id ASC) as ViewId,
		ci1.Position as Clothes1Position,
		ci2.Position as Clothes2Position,
		sc1.CategoryId as Clothes1CategoryId,
		sc2.CategoryId as Clothes2CategoryId,
		sc1.Name as Clothes1ClothesName,
		sc2.Name as Clothes2ClothesName,
		sc1.Score as Clothes1WS,
		sc2.Score as Clothes2WS,
		coalesce(sc1.Score, 0) + coalesce(sc2.Score, 0) as AdaptationScore,
		ci1.UserPreferences as Clothes1UserPreferences,
		ci2.UserPreferences as Clothes2UserPreferences,
		coalesce(ci1.UserPreferences, 0) + coalesce(ci2.UserPreferences, 0) as TotalPreferences
	from clothes_node as ci2
		inner join sub_category as sc2 on sc2.Id = ci2.SubCategoryId and (sc2.CategoryId = 1 or sc2.CategoryId = 2)
		inner join clothes_node as ci1 on sc2.CategoryId != 2
		inner join sub_category as sc1 on sc1.Id = ci1.SubCategoryId and sc1.CategoryId != 8 and sc2.CategoryId != 8 and sc1.CategoryId != sc2.CategoryId and (sc1.CategoryId = 1 or sc1.CategoryId = 2);


select *
from v_clothes_graph
