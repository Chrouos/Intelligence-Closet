

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

  $scope.upSet=false;//上半身子選項
  $scope.downSet=false;//下半身子選項
  $scope.otherSet=false;//其他子選項

  $scope.upClick = function () {
    $scope.upSet=!$scope.upSet;
    $scope.downSet=false;
    $scope.otherSet=false;
  }
  $scope.downClick = function () {
    $scope.upSet=false;
    $scope.downSet=!$scope.downSet;
    $scope.otherSet=false;
  }
  $scope.otherClick = function () {
    $scope.upSet=false;
    $scope.downSet=false;
    $scope.otherSet=!$scope.otherSet;
  }

});