
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 從 Python中 獲得天氣資訊(溫度、濕度、最高溫+時間、最低溫+時間)
    $scope.get_weather = async function (stationName) {
        $scope.weather = await eel.weather_to_js(stationName)()
    };

    // 從 Python中 角色資訊
    $scope.user_by_id_to_js = async function () {
        $scope.user = await eel.user_by_id_to_js()();
        $scope.get_weather($scope.user.StationName);

    }; $scope.user_by_id_to_js();



    // 從 Python中 獲得所有城鎮 顯示在 option 選項中
    $scope.get_combs = async function () {
        $scope.combs = await eel.comb_to_js()();

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

        $scope.subCategoryList = await eel.get_all_sc_name()();
        $scope.colorList = await eel.get_all_color()();
    }

    // 把資料存到資料庫
    $scope.identify_save_sql = async function () {
        $scope.isSuccess = await eel.identify_save_sql($scope.category, $scope.color, $scope.path)();
        $scope.isIdentifySuccess = false;
        $scope.isEditIdentify = false;
        $scope.get_combs();
    }

    // 修改 樣式名稱
    $scope.changeIdentifyName = function (weatherChName) {
        $scope.category = weatherChName;
    }

    // 修改 顏色
    $scope.changeColorName = function (color) {
        $scope.color = color;
    }



});


