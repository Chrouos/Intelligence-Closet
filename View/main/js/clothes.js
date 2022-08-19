
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 獲得 衣物
    $scope.clothes_to_js = async function () {
        $scope.clothes = await eel.clothes_to_js()()
    };
    $scope.clothes_to_js();

    // 獲得 衣物
    $scope.upper_clothes_to_js = async function () {
        $scope.clothes_filter = await eel.upper_clothes_to_js()()
    };

    // 獲得 衣物
    $scope.lower_clothes_to_js = async function () {
        $scope.clothes_filter = await eel.lower_clothes_to_js()()
    };

    // 獲得 衣物
    $scope.other_clothes_to_js = async function () {
        $scope.clothes_filter = await eel.other_clothes_to_js()()
    };

});


