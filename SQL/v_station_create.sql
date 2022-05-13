drop view v_station


create view v_station
AS
  select
	st.Id,
	st.StationNumber,
    st.StationName,
	st.CityId,
	ci.CityName,
	st.Address,
	st.Remark,
	st.CreateTime,
	st.ModifyTime,
	st.Work
  from station as st
    inner join city as ci on ci.Id = st.CityId
	
select *
from v_station

SELECT * FROM v_station WHERE CityName = '·s¥_¥«'