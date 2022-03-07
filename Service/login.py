import pyodbc
import pandas as pd

from nodeCRUD import nodeCRUD


crud = nodeCRUD()
print(crud.queryData())
# crud.updatePositionToNull(3)
# print(crud.queryData())
# crud.deleteByPosition(1)

# crud.createtData('upper', 'blue', '55', 'long_TShirt', 'NULL')
# crud.queryData()
