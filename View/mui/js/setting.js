

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    $scope.settingType_Main=true;
    $scope.settingType_Match=false;
    $scope.settingType_Single=false;
    $scope.settingType_Match_st=false;
    $scope.settingType_Match_nd=false;
    $scope.backToMain=function(){
        $scope.settingType_Main=true;
        $scope.settingType_Match=false;
        $scope.settingType_Single=false;
    }
    $scope.goToMatch=function(){
        $scope.settingType_Main=false;
        $scope.settingType_Match=true;
        $scope.settingType_Single=false;
        $scope.settingType_Match_st=true;
        $scope.settingType_Match_nd=false;
    }
    $scope.goToSingle=function(){
        $scope.settingType_Main=false;
        $scope.settingType_Match=false;
        $scope.settingType_Single=true;
    }
    $scope.goToMatchNd=function(){
        $scope.settingType_Match_nd=true;
        $scope.settingType_Match_st=false;
    }


});