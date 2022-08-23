var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {


    $scope.loginPage = true; // 是否在登入畫面
    $scope.nowUser = ""; // 目前的使用者

    // 使用者假資料
    $scope.users = [
        { 'Id': 1, 'UserName': 'DiuDiu', 'WeatherLike': 5, 'StationName': '鯉魚潭', 'Clock': '08/00', 'ModifyTime': '08/01/2022', 'StationId': 0 },
        { 'Id': 2, 'UserName': 'Tester', 'WeatherLike': 9, 'StationName': '', 'Clock': '00/00', 'ModifyTime': '08/23/2022', 'StationId': 2 }
    ]
    console.log($scope.users)

    // 點選使用者登入畫面
    $scope.login = function (id) {
        $scope.loginPage = false;
        $scope.nowUser = $scope.users[id - 1];
        console.log("登入", id)
    }

    // 登出
    $scope.logout = function () {
        $scope.loginPage = true;
    }

});