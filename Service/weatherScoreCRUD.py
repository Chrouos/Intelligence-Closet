import pyodbc
import pandas as pd


class weatherScoreCRUD:

    def __init__(self):

        try:
            server = 'MSI\SQLEXPRESS'
            database = 'intelligence_closet'
            username = 'sa'
            password = 'a25232523'
            cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server
                                  + ';DATABASE=' + database
                                  + ';UID=' + username
                                  + ';PWD=' + password)
            self.cursor = cnxn.cursor()
            print('操作成功')

        except:
            print('操作錯誤')

        self.cnxn = cnxn
        self.cursor = cnxn.cursor()

    def reconnect(self):
        self.cursor = self.cnxn.cursor()
    
    def queryByClothesTypeCategoryId(self, clothesType):
        execute_str = "SELECT CategoryId FROM weather_score WHERE ClothesType = '" + clothesType + "'"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchone()[0]
        return datas
    
    def queryByClothesTypeWSId(self, clothesType):
        execute_str = "SELECT Id FROM weather_score WHERE ClothesType = '" + clothesType + "'"
        self.cursor.execute(execute_str)
        datas = self.cursor.fetchone()[0]
        return datas
    