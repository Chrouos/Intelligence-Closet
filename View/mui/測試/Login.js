var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () { });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 使用者假資料
    // $scope.users = [
    //     { 'Id': 1, 'UserName': 'DiuDiu', 'WeatherLike': 5, 'StationName': '鯉魚潭', 'Clock': '08/00', 'ModifyTime': '08/01/2022', 'StationId': 0 },
    //     { 'Id': 2, 'UserName': 'Tester', 'WeatherLike': 9, 'StationName': '', 'Clock': '00/00', 'ModifyTime': '08/23/2022', 'StationId': 2 }
    // ]
    // console.log($scope.users)

    // 從 Python中 獲得所有城鎮 顯示在 option 選項中
    $scope.all_user_to_js = async function () {
        $scope.users = await eel.all_user_to_js()();
    }; $scope.all_user_to_js();


    // 選擇角色ID 登入
    $scope.login = async function (id) {
        $scope.loginPage = false;
        $scope.change_user = await eel.change_user(id)();
        location.href = "./User.html";

    }


});