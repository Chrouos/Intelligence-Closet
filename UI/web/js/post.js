
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
  async function get_combs() {
    $scope.combs = await eel.comb_to_js()();

    console.log(combs)

  }; get_combs();



});


