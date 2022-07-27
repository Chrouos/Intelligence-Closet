from Model.DAO.categoryDAO import CategoryDAO

class CategoryService:
    
    # 建構子: 呼叫SQL
    def __init__(self):	
        self.categoryDAO = CategoryDAO()
        
    # 搜尋全部資料: 轉換成字典
    def queryAll(self):
        
        category_dict = []
        datas = self.categoryDAO.queryAll()
        
        for data in datas:
            category_dict.append({'Id': data.Id, 'CategoryName': data.CategoryName, 'Level': data.Level})
        
        return category_dict
    
    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.categoryDAO.queryById(id)
        
        category_dict = {'Id': data.Id, 'CategoryName': data.CategoryName, 'Level': data.Level}
        return category_dict