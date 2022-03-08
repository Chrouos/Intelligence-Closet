import pyodbc
import pandas as pd

from nodeCRUD import nodeCRUD

crud = nodeCRUD()
crud.createtData('upper', 'blue', 11, 'long_Tshirt', 'NONE')

print(crud.queryData())
