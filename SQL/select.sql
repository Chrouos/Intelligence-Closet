select * from v_clothes_information

SELECT *
FROM clothes_information
WHERE position=1

INSERT  INTO clothes_information (Position, Category, Color, ClothesType, UsageCounter, CreateTime, ModifyTime , FilePosition)
values(1, 'upper', 'blue', 'long_Tshirt', 0, GETDATE(), GETDATE(), 'E:\ProgrammingLanguage\git\Intelligence-Closet')

UPDATE clothes_information SET Position = NULL WHERE Position = 1


