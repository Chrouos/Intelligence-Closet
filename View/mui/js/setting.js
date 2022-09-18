
function heartClick(a) {
    if (a.style.color == "gray")
        a.style.color = "red";
    else
        a.style.color = "gray";
}

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 抓取全部資料
    $scope.queryAllList = async function () {
        // $scope.upperList = await eel.upper_clothes_to_js()(); // 上半身的所有衣服

        $scope.upperList = await eel.query_subCategory_byCategoryId(1)(); // 上半身的子類別
        $scope.lowerList = await eel.query_subCategory_byCategoryId(2)(); // 下半身的子類別
        $scope.otherList = await eel.query_subCategory_byCategoryId(3)(); // 下半身的子類別

        $scope.clothesNodeList = await eel.clothes_to_js()();
        console.log("clothesNodeList: ", $scope.clothesNodeList)

    }
    $scope.queryAllList();

    // 搜尋衣物 by.子類別ID
    $scope.nowSubCategory = "";
    $scope.queryClothesBySubCategory = async function (subCategoryId, subCategoryName) {
        $scope.clothesNodeList = await eel.query_clothes_nodes_bySubCategoryId(subCategoryId)();
        $scope.nowSubCategory = subCategoryName;
        console.log($scope.nowSubCategory)
    }

    $scope.pickUp_ClohtesNode = null; // 選擇的衣物
    $scope.checkThePickUpList = function (clothesNode) {
        // 如果為空 則選取
        if ($scope.pickUp_ClohtesNode == null) {
            document.getElementById("clothesNode_" + clothesNode.Id).style.border = "2px solid red";
            $scope.pickUp_ClohtesNode = clothesNode;
        }
        // 如果點選同樣資料 就取消
        else if ($scope.pickUp_ClohtesNode.Id == clothesNode.Id) {
            document.getElementById("clothesNode_" + clothesNode.Id).style.border = "";
            $scope.pickUp_ClohtesNode = null;
        }
    }

    /* ---------- 切換頁面 start ---------- */
    $scope.settingType_Main = true; // 主頁面

    $scope.settingType_Single = false;
    $scope.settingType_Match_st = false;
    $scope.settingType_Match_nd = false;

    $scope.backToMain = function () {
        $scope.settingType_Main = true;
        $scope.settingType_Single = false;
        $scope.settingType_Match_st = false;
        $scope.settingType_Match_nd = false;

        $scope.pickUp_ClohtesNode = null;
    }

    $scope.goToMatch = function () {
        $scope.settingType_Main = false;
        $scope.settingType_Match_st = true;
        $scope.settingType_Match_nd = false;
        $scope.settingType_Single = false;
    }

    $scope.goToSingle = function () {
        $scope.settingType_Main = false;
        $scope.settingType_Match_st = false;
        $scope.settingType_Match_nd = false;
        $scope.settingType_Single = true;
    }

    $scope.goToMatchNd = function () {
        $scope.settingType_Main = false;
        $scope.settingType_Match_st = false;
        $scope.settingType_Match_nd = true;
        $scope.settingType_Single = false;
    }

    //衣物設定介面
    $scope.clothesSetType = false;
    $scope.clothes_Set = function () {
        $scope.clothesSetType = !$scope.clothesSetType;
    }
    /* ---------- 切換頁面 end ---------- */





});

