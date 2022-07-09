
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

  $scope.checkOk = function () {
    $scope.isLoading = true;

    setTimeout(function () {
      $scope.isLoading = false;
      $scope.isGetting = true;
    }, 3000)
  }


  $scope.returnLobby = function () {
    $scope.isGetting = false;
    $scope.isLoading = false;
    window.location.replace("lobby.html");
  }






});


