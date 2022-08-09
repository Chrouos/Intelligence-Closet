
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
    $scope.get_station_city = async function () {
        $scope.allCitys = await eel.station_city_to_js()();
    }; $scope.get_station_city();

    // 從 Python中 獲得縣市氣象站別 顯示在 option 選項中
    $scope.isCity_getStationByCity = async function () {
        var stationByCity = await eel.station_station_to_js($scope.selectedCityId)();
        $scope.stationByCity = stationByCity;
    }

    // 從 Python中 獲得天氣資訊(溫度、濕度、最高溫+時間、最低溫+時間)
    $scope.get_weather = async function () {

        var getWeatherPosition = $scope.selectedStation;
        $scope.weather = await eel.weather_to_js(getWeatherPosition)()

    }

    $scope.getStation = function () {
        $scope.isCity_getStationByCity();
    }

    $scope.getWeather = function (type) {
        $scope.get_weather(type);
    }


});


