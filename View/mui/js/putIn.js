
function heartClick(a) {
  if (a.style.color == "white")
    a.style.color = "red";
  else
    a.style.color = "white";
}

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {


  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */

  $scope.StartType = true; // 開始介面 bool
  $scope.MainType = false; // 主介面 bool

  // ----- 取得 子類別 和 顏色的資料 start ----- //
  $scope.getColorAndSubCategoryList = async function () {
    $scope.subCategoryList = await eel.get_all_sc_name()();
    $scope.colorList = await eel.get_all_color()();
  }
  $scope.getColorAndSubCategoryList();
  // ----- 取得 子類別 和 顏色的資料 end ----- //


  $scope.start_identify = function () { // 開始辨識

    bootbox.alert({
      message: "This is an alert with a callback!",
      callback: function () {
        console.log('This was logged in the callback!');
      }
    })

    $scope.get_camera_identify(); // 辨識 + 存入資料庫
    $scope.StartType = false;

    //TODO bootbox:1.為偵測到衣服，請放入衣服  2.辨識中，請稍等
    $scope.MainType = true;

    bootbox.hideAll();
  }

  $scope.Back = function () { // 退回衣服
    $scope.MainType = false;

    //TODO bootbox: 衣服退出中...
    $scope.StartType = true;
  }

  $scope.Send = function () { // 送出
    $scope.MainType = false;

    $scope.identify_save_sql();
    //TODO bootbox: 衣服收入中...
    $scope.StartType = true;
    console.log($scope.putIn)
  }

  // 拍照存取
  $scope.get_camera_identify = async function () {
    $scope.identify = await eel.get_camera_identify()();

    $scope.category = $scope.identify[0];
    $scope.color = $scope.identify[1];
    $scope.path = $scope.identify[2];
    $scope.isFavorite = 0;

    $scope.isIdentifySuccess = $scope.identify[3];

  };

  // 把資料存到資料庫
  $scope.identify_save_sql = async function () {
    return await eel.identify_save_sql($scope.category, $scope.color, $scope.path, $scope.isFavorite)();
  }


  $scope.heartClicks = function () {
    $scope.isFavorite = ($scope.isFavorite == 0) ? 1 : 0;
  }


});