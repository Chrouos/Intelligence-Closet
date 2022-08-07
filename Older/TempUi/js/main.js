
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


  $scope.chooseCombIndex = ['clothes-comb', 'clothes-comb', 'clothes-comb', 'clothes-comb']; // 改變前端組合選擇後的樣貌
  $scope.chooseCombId = -1; // 選擇的組合Id 0~3

  // 選擇衣物
  $scope.chooseComb = function (index) {
    for (var i = 0; i < 4; i++) {
      (index != i) ? $scope.chooseCombIndex[i] = 'clothes-comb' : $scope.chooseCombIndex[i] = 'clothes-choosed';
    }
    $scope.chooseCombId = index;
  }

  // 送出
  $scope.submitComb = function () {
    // alert("你選擇" + $scope.chooseCombId)
    $scope.isLoading = true;

    setTimeout(function () {
      $scope.isLoading = false;
      $scope.isGetting = true;
    }, 6000);
  }

  $scope.returnLobby = function () {
    $scope.isGetting = false;
    $scope.isLoading = false;
    window.location.replace("lobby.html");
  }



});


