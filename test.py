import sys, os
sys.path.append(os.getcwd())  # 抓取路徑

from Model.Domain.category import Category
from Model.DAO.categoryDAO import CategoryDAO
from Service.categoryService import CategoryService

categoryDAO = CategoryDAO()
categoryService = CategoryService()

categoryData = categoryService.queryById(3)

category = Category()
category.print()
category.updateByDict(categoryData)
category.print()

