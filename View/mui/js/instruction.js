

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {


    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */



});