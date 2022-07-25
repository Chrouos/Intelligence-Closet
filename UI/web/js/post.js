
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
  $scope.get_combs = async function () {
    $scope.combs = await eel.comb_to_js()();

    console.log(combs)

  }; $scope.get_combs();

//  // 拍照存取
  $scope.get_camera_identify = async function () {
      $scope.identify = await eel.get_camera_identify()();

      $scope.category = $scope.identify[0];
      $scope.color = $scope.identify[1];
      $scope.path = $scope.identify[2];

    };



});


