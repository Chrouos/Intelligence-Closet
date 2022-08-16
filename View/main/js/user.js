
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
    $scope.all_user_to_js = async function () {
        $scope.users = await eel.all_user_to_js()();

    }; $scope.all_user_to_js();


    $scope.change_user = async function () {
        $scope.change_user = await eel.change_user()();
    }

});


