
select 
	cg.ColorId1 as 'UpperColorId',
	cg.ColorId2 as 'LowerColorId',
	c1.ColorEngName as 'UpperEngName',
	c2.ColorEngName as 'LowerEngName',
	c1.ColorName as 'UpperColor',
	c2.ColorName as 'LowerColor',
	cg.ColorScore
from color_graph as cg
inner join color as c1 on c1.Id = cg.ColorId1
inner join color as c2 on c2.Id = cg.ColorId2