
create view v_clothes_information
AS
  select
    ci.Position,
    ci.Color,
    ci.Category,
    ci.ClothesType,
    ci.ClothesStyle,
    ws.Score,
    ci.UserPreferences,
    ci.UsageCounter,
    ci.CreateTime,
    ci.ModifyTime,
    ci.FilePosition
  from clothes_information as ci
    inner join weather_score as ws on ws.Category = ci.Category and ws.ClothesType = ci.ClothesType

select *
from v_clothes_information