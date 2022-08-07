
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */

  $scope.isLoading = false;
  $scope.isGetting = false;

  $scope.putInNow = function () {
    $scope.isLoading = true;

    setTimeout(function () {
      $scope.isLoading = false;
      $scope.isGetting = true;
    }, 4000)
  }


  $scope.goToPutInCheck = function () {
    $scope.isGetting = false;
    $scope.isLoading = false;
    window.location.replace("putInCheck.html");
  }






});


