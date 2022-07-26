drop view v_clothes_information

create view v_clothes_information
as
	select
		ci.Id,
		ci.Position,
		ci.WeatherScoreId as ClothesId,
		ws.Name,
		ws.ClothesType,
		ci.ColorId,
		color.ColorName,
		ci.UserPreferences,
		ws.CategoryId,
		ci.ClothesStyle,
		ci.UsageCounter,
		ci.CreateTime,
		ci.ModifyTime,
		ci.FilePosition,
		ws.Score,
		cat.Level
	from clothes_information as ci
		inner join weather_score as ws on ci.WeatherScoreId = ws.Id
		inner join category as cat on cat.Id = ws.CategoryId
		inner join color as color on ci.ColorId = color.Id


select *
from v_clothes_information
