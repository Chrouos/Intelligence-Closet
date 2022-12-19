-- 存放衣服種類的數量
SELECT SubCategoryName, count(SubCategoryName) as SubCategoryCount
FROM 
v_clothes_node vcn
GROUP BY SubCategoryName
ORDER BY SubCategoryCount DESC 

-- 存放衣服顏色的數量
SELECT ColorName, count(ColorName) as ColorCount
FROM 
v_clothes_node vcn
GROUP BY ColorName
ORDER BY ColorCount DESC 

-- 最常拿出來的衣服
SELECT TOP(1) FilePosition 
from 
v_clothes_node vcn2 
WHERE UsageCounter = (
	SELECT 
		MAX(UsageCounter)
	FROM v_clothes_node vcn
)



