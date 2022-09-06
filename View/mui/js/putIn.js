
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

    /* ----- step 1. 等待衣物放入階段 ----- */
    // var dialog = bootbox.dialog({
    //   message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 等待衣物放入中... </p>',
    //   closeButton: false
    // });

    // // do something in the background
    // dialog.modal('hide');

    /* ----- step2. 接收衣物放入 等待辨識階段 ----- */
    var dialog = bootbox.dialog({
      message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 辨識中，請稍等... </p>',
      closeButton: false
    });
    // 辨識
    $scope.get_camera_identify().then(function () {
      dialog.modal('hide'); // 等待時間到就將bootbox隱藏
    })

    // 切換畫面
    $scope.StartType = false;

    //TODO bootbox:1.為偵測到衣服，請放入衣服  2.辨識中，請稍等
    $scope.MainType = true;

    // 防呆
    bootbox.hideAll();
  }

  // 取消
  $scope.Back = function () {
    $scope.MainType = false;
    $scope.StartType = true;
  }

  /* ---------- 將資料儲存至料庫 Start ---------- */
  $scope.Send = function () { // 送出


    $scope.identify_save_sql();

    //TODO bootbox: 衣服收入中...
    $scope.MainType = false;
    $scope.StartType = true;
    console.log($scope.putIn)
  }
  /* ---------- 將資料儲存至料庫 Start ---------- */


  /* ---------- 拍照 + 辨識 Start ---------- */
  $scope.get_camera_identify = async function () {
    $scope.identify = await eel.get_camera_identify()();

    $scope.category = $scope.identify[0];
    $scope.color = $scope.identify[1];
    $scope.path = $scope.identify[2];
    $scope.isFavorite = 0;

    $scope.isIdentifySuccess = $scope.identify[3];

  };
  /* ---------- 拍照 + 辨識 Start ---------- */

  // 把資料存到資料庫
  $scope.identify_save_sql = async function () {
    return await eel.identify_save_sql($scope.category, $scope.color, $scope.path, $scope.isFavorite)();
  }

  $scope.heartClicks = function () {
    $scope.isFavorite = ($scope.isFavorite == 0) ? 1 : 0;
  }


});