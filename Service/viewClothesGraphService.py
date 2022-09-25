from Model.DAO.viewClothesGraphDAO import ViewClothesGraphDAO


class ViewClothesGraphService:

    # 建構子: 呼叫SQL
    def __init__(self):
        self.viewClothesGraphDAO = ViewClothesGraphDAO()

    # 搜尋全部資料: 轉換成字典
    def queryAll(self):

        viewClothesGraph_dict = []
        datas = self.viewClothesGraphDAO.queryAll()

        for data in datas:
            viewClothesGraph_dict.append({
                'Id': data.Id,
                'UpperClothesId': data.UpperClothesId,
                'UpperPosition': data.UpperPosition,
                'UpperSubCategory': data.UpperSubCategory,
                'UpperColorId': data.UpperColorId,
                'UpperUserPreferences': data.UpperUserPreferences,
                'UpperFilePosition': data.UpperFilePosition,
                'LowerClothesId': data.LowerClothesId,
                'LowerPosition': data.LowerPosition,
                'LowerSubCategory': data.LowerSubCategory,
                'LowerColorId': data.LowerColorId,
                'LowerUserPreferences': data.LowerUserPreferences,
                'LowerFilePosition': data.LowerFilePosition,
                'OtherClothesId': data.OtherClothesId,
                'OtherPosition': data.OtherPosition,
                'OtherSubCategory': data.OtherSubCategory,
                'OtherColorId': data.OtherColorId,
                'OtherUserPreferences': data.OtherUserPreferences,
                'OtherFilePosition': data.OtherFilePosition,
                'TotalPreferences': data.TotalPreferences,
                'UserLike': data.UserLike,
                'ColorScore': data.ColorScore
            })

        return viewClothesGraph_dict

    # 透過Id查找一筆資料: 轉換成字典
    def queryById(self, id):
        data = self.viewClothesGraphDAO.queryById(id)

        viewClothesGraph_dict = {
            'Id': data.Id,
            'UpperClothesId': data.UpperClothesId,
            'UpperPosition': data.UpperPosition,
            'UpperSubCategory': data.UpperSubCategory,
            'UpperColorId': data.UpperColorId,
            'UpperUserPreferences': data.UpperUserPreferences,
            'UpperFilePosition': data.UpperFilePosition,
            'LowerClothesId': data.LowerClothesId,
            'LowerPosition': data.LowerPosition,
            'LowerSubCategory': data.LowerSubCategory,
            'LowerColorId': data.LowerColorId,
            'LowerUserPreferences': data.LowerUserPreferences,
            'LowerFilePosition': data.LowerFilePosition,
            'OtherClothesId': data.OtherClothesId,
            'OtherPosition': data.OtherPosition,
            'OtherSubCategory': data.OtherSubCategory,
            'OtherColorId': data.OtherColorId,
            'OtherUserPreferences': data.OtherUserPreferences,
            'OtherFilePosition': data.OtherFilePosition,
            'TotalPreferences': data.TotalPreferences,
            'UserLike': data.UserLike,
            'ColorScore': data.ColorScore
        }
        return viewClothesGraph_dict