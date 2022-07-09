
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {


  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */


  $scope.isSaving = false;
  $scope.saveOk = false;

  $scope.save = function () {
    $scope.isSaving = true;

    setTimeout(function () {
      $scope.isSaving = false;
      $scope.saveOk = true;
    }, 3000);
  }


  $scope.returnLobby = function () {
    $scope.isSaving = false;
    $scope.saveOk = false;
    window.location.replace("main.html");
  }
});


