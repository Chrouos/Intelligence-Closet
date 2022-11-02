drop view v_village


create view v_village
AS
	select
		vi.Id,
		vi.CityId,
		ci.CityName,
		vi.VillageName
	from village as vi
		inner join city as ci on ci.Id = vi.CityId;

select *
from v_village

