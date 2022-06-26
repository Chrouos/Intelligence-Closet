drop view v_clothes_graph_edge

create view v_clothes_graph_edge
as
select
	cg.Id,
	ci1.Position as Clothes1Position,
	ci2.Position as Clothes2Position,
	w1.Name as Clothes1ClothesName,
	w2.Name as Clothes2ClothesName,
	w1.Score as Clothes1WS,
	w2.Score as Clothes2WS,
	coalesce(w1.Score, 0)  +coalesce(w2.Score, 0) as AdaptationScore,
	ci1.UserPreferences as Clothes1UserPreferences,
	ci2.UserPreferences as Clothes2UserPreferences,
	coalesce(ci1.UserPreferences, 0) + coalesce(ci2.UserPreferences, 0) as TotalPreferences,
	ci1.Id as Clothes1Id,
	ci2.Id as Clothes2Id
	cg.CombScore
from clothes_graph　as cg　
inner join clothes_information as ci1 on ci1.Id = cg.ClothesId1 -- 這裡要多下 and 判斷是否ci1, ci2的類型重疊
inner join clothes_information as ci2 on ci2.Id = cg.ClothesId2
inner join weather_score as w2 on w2.Id = ci2.WeatherScoreId
inner join weather_score as w1 on w1.Id = ci1.WeatherScoreId


select * from v_clothes_graph_edge