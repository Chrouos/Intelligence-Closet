var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 從 Python中 獲得天氣資訊
    $scope.weather_to_js = async function () {
        $scope.weather = await eel.weather_to_js()();
    }; $scope.weather_to_js();

    // 從 Python中 獲得存放最多種類的衣服
    $scope.most_subCategory_to_js = async function () {
        $scope.mostSubCategory = await eel.most_subCategory_to_js()();
    }; $scope.most_subCategory_to_js();

    // 從 Python中 獲得存放最多顏色的衣服
    $scope.most_color_to_js = async function () {
        $scope.mostColor = await eel.most_color_to_js()();
    }; $scope.most_color_to_js();

    // 從 Python中 獲得最常拿出來的衣服
    $scope.most_counter_to_js = async function () {
        $scope.mostCounter = await eel.most_counter_to_js()();
    }; $scope.most_counter_to_js();

    /* ---------- 切換頁面 start ---------- */

    $scope.settingType_Main = true; // 主頁面

    /* ---------- 切換頁面 end ---------- */

});

