
create view v_clothes_graph_edge
as
select 
	ci1.Position as Clothes1Position,
	ci2.Position as Clothes2Position,
	ci1.CategoryId as Clothes1CategoryId,
	ci2.CategoryId as Clothes2CategoryId,
	w1.Score as Clothes1WS,
	w2.Score as Clothes2WS,
	coalesce(w1.Score, 0)  +coalesce(w2.Score, 0) as AdaptationScore,
	ci1.UserPreferences as Clothes1UserPreferences,
	ci2.UserPreferences as Clothes2UserPreferences,
	coalesce(ci1.UserPreferences, 0)  +coalesce(ci2.UserPreferences, 0) as TotalPreferences
from clothes_information¡@as ci2¡@
inner join clothes_information as ci1 on ci1.CategoryId != ci2.CategoryId and ci2.CategoryId != 2
inner join weather_score as w2 on w2.Id = ci2.WeatherScoreId
inner join weather_score as w1 on w1.Id = ci1.WeatherScoreId

select * from v_clothes_graph_edge

