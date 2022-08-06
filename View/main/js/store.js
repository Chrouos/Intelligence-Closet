
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 從 Python中 獲得所有城鎮 顯示在 option 選項中
    $scope.get_combs = async function () {
        $scope.combs = await eel.comb_to_js()();

        console.log($scope.combs)

    }; $scope.get_combs();

    // 拍照存取
    $scope.get_camera_identify = async function () {
        $scope.identify = await eel.get_camera_identify()();

        $scope.category = $scope.identify[0];
        $scope.color = $scope.identify[1];
        $scope.path = $scope.identify[2];

        $scope.isIdentifySuccess = $scope.identify[3];

    };

    // 資料辨識失敗: 顯示選項
    $scope.identify_failed = async function () {
        $scope.isEditIdentify = true;

        $scope.watherScoreList = await eel.get_all_ws_name()();
        $scope.colorList = await eel.get_all_color()();
    }

    // 把資料存到資料庫
    $scope.identify_save_sql = async function () {
        $scope.isSuccess = await eel.identify_save_sql($scope.category, $scope.color, $scope.path)();
        $scope.isIdentifySuccess = false;
        $scope.isEditIdentify = false;
    };

    // 修改category
    $scope.changeIdentifyName = function (weatherChName) {
        $scope.category = weatherChName;
    }

    // 修改category
    $scope.changeColorName = function (color) {
        $scope.color = color;
    }

});


