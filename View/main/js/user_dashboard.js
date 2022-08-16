
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
    $scope.user_by_id_to_js = async function () {
        $scope.user = await eel.user_by_id_to_js()();

    }; $scope.user_by_id_to_js();


    // 從 Python中 獲得所有城鎮 顯示在 option 選項中
    $scope.get_station_city = async function () {
        $scope.allCitys = await eel.station_city_to_js()();
    }; $scope.get_station_city();

    // 從 Python中 獲得縣市氣象站別 顯示在 option 選項中
    $scope.isCity_getStationByCity = async function () {
        var stationByCity = await eel.station_station_to_js($scope.selectedCityId)();
        $scope.stationByCity = stationByCity;
    }

    $scope.update_user = async function () {
        var isSuccess = await eel.update_user_dashboard($scope.user)();
        if (isSuccess == true) {
            $scope.user_by_id_to_js();
        }
    }


});


