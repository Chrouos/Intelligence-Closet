var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    // 使用者假資料
    // $scope.users = [
    //     { 'Id': 1, 'UserName': 'DiuDiu', 'WeatherLike': 5, 'StationName': '鯉魚潭', 'Clock': '08/00', 'ModifyTime': '08/01/2022', 'StationId': 0 },
    //     { 'Id': 2, 'UserName': 'Tester', 'WeatherLike': 9, 'StationName': '', 'Clock': '00/00', 'ModifyTime': '08/23/2022', 'StationId': 2 }
    // ]
    // console.log($scope.users)

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    /* ---------- 頁面切換 Start ---------- */
    $scope.isEdit = false; // 是否需要編輯

    $scope.openEdit = function () {
        $scope.isEdit = true;
    }

    $scope.closeEdit = function () {
        $scope.isEdit = false;
    }
    /* ---------- 頁面切換 End ---------- */

    // 從 Python中 角色資訊
    $scope.user_by_id_to_js = async function () {
        $scope.user = await eel.user_by_id_to_js()();
    }; $scope.user_by_id_to_js();

    // 更新資料
    $scope.update_user = async function () {
        //console.log($scope.user);
        var isSuccess = await eel.update_user_dashboard($scope.user)();
        if (isSuccess == true) {
            $scope.user_by_id_to_js();
        }
        $scope.closeEdit();
    }

    // 從 Python中 獲得所有縣市 顯示在 option 選項中
    $scope.get_city = async function () {
        $scope.allCitys = await eel.city_to_js()();
        // $scope.isCity_getStationByCity();
        $scope.isCity_getVillageByCity();
    }; $scope.get_city();

    // 從 Python中 獲得縣市氣象站別 顯示在 option 選項中
    // $scope.isCity_getStationByCity = async function () {
    //     var stationByCity = await eel.station_station_to_js($scope.user.CityId)();
    //     $scope.stationByCity = stationByCity;
    // }

     // 從 Python中 獲得所有鄉鎮 顯示在 option 選項中
     $scope.isCity_getVillageByCity = async function () {
        var villageByCity = await eel.village_to_js($scope.user.CityId)();
        $scope.villageByCity = villageByCity;
    }

});