drop view v_user_dashboard


create view v_user_dashboard
as
	select
		ud.Id,
		ud.UserName, 
		ud.WeatherLike, 
		ud.ModifyTime,
		ud.Clock,
		ud.VillageId, 
		vi.VillageName,
		vi.CityId,
		ci.CityName
	from user_dashboard as ud
		inner join village as vi on vi.Id = ud.VillageId 
		inner join city as ci on ci.Id = vi.CityId;

select *
from v_user_dashboard

