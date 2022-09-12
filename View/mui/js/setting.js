

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




    /* ---------- 切換頁面 end ---------- */


});