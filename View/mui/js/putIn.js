
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
  $scope.isClothesExis = false; // 是否衣物在上面了

  // 從 Python中 獲得天氣資訊
  $scope.weather_to_js = async function () {
    $scope.weather = await eel.weather_to_js()();
  }; $scope.weather_to_js();

  // ----- 取得 子類別 和 顏色的資料 start ----- //
  $scope.getColorAndSubCategoryList = async function () {
    $scope.subCategoryList = await eel.get_all_sc_name()();
    $scope.colorList = await eel.get_all_color()();
  }
  $scope.getColorAndSubCategoryList();
  // ----- 取得 子類別 和 顏色的資料 end ----- //

  // ----- 取得 衣櫃位置是否放滿 start ----- //
  $scope.getVacancyPosition = async function () {
    $scope.vacancyStatus = false;
    $scope.vacancy = await eel.vacancyPosition()();
    
    if($scope.vacancy == -1){
      $scope.vacancyStatus = true;
    }
    console.log("$scope.vacancyStatus", $scope.vacancyStatus);
  };$scope.getVacancyPosition();
  // ----- 取得 衣櫃位置是否放滿 end ----- //


  // 等待衣物模塊送至入口
  $scope.wait_zero_nullPosition_entrance = function (){
    
    var dialog = bootbox.dialog({
      message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 等待空模塊提出 ... </p>',
      closeButton: false
    });

    // 等待空模塊拿出
    $scope.getNullPositionModel_toEntrance().then(function () {
      dialog.modal('hide'); // 等待時間到就將bootbox隱藏

      dialog = bootbox.dialog({
        message: '<p class="text-center mb-0">是否確認以放入衣物 ... </p>',
        closeButton: false,
        buttons: {
        cancel: {
          label: '取消',
          className: 'btn-danger',
          callback: function() {
                $scope.put_cancel().then(function () {
                dialog.modal('hide'); // 等待時間到就將bootbox隱藏
                }); // 触发put_cancel函数
          }
        },
        ok: {
          label: '確認',
          className: 'btn-success',
          callback: function() {
                $scope.start_identify().then(function () {
                dialog.modal('hide'); // 等待時間到就將bootbox隱藏
                });
          }
        },
        }
      });
    })

    


    $scope.isClothesExis = !$scope.isClothesExis;

    // 防呆
    bootbox.hideAll();

  }

  $scope.start_identify = function () { // 開始辨識

    var dialog = bootbox.dialog({
      message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 存放與辨識中，請稍等... </p>',
      closeButton: false
    });

    // 辨識
    $scope.get_camera_identify().then(function () {
      dialog.modal('hide'); // 等待時間到就將bootbox隱藏
    })

    // 切換畫面
    $scope.StartType = false;
    $scope.MainType = true;

    // 防呆
    bootbox.hideAll();
  }

  // 取消
  $scope.Back = async function () {
    $scope.MainType = false;
    $scope.StartType = true;

    $scope.subCategory = "";
    $scope.color = "";
    $scope.path = "";
    $scope.isFavorite = 0;

    await eel.arduino_car_back_now()();
  }

  /* ---------- 將資料儲存至料庫 Start ---------- */
  $scope.Send = function (subCategory, color) { // 送出
    
    var dialog = bootbox.dialog({
      message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 存放中... </p>',
      closeButton: false
    });

    // 辨識
    $scope.identify_save_sql(subCategory, color).then(function () {
      dialog.modal('hide'); // 等待時間到就將bootbox隱藏
    })


    $scope.MainType = false;
    $scope.StartType = true;
  }
  /* ---------- 將資料儲存至料庫 Start ---------- */

  // 把資料存到資料庫
  $scope.identify_save_sql = async function (subCategory, color) {
    // console.log("[js] identify_save_sql: ", subCategory, color, $scope.path, $scope.isFavorite)

    return await eel.identify_save_sql(subCategory, color, $scope.path, $scope.isFavorite)();
  }

  /* ---------- 拍照 + 辨識 Start ---------- */
  $scope.get_camera_identify = async function () {
    console.log("get_camera_identify");
    var identify = await eel.get_camera_identify()();

    $scope.subCategory = identify[0];
    $scope.color = identify[1];
    $scope.path = identify[2];
    $scope.isFavorite = 0;

    $scope.isIdentifySuccess = identify[3];

  };
  /* ---------- 拍照 + 辨識 Start ---------- */

  $scope.getNullPositionModel_toEntrance = async function () {
    console.log("getNullPositionModel_toEntrance");
    await eel.getNullPositionModel_toEntrance()();
  };

  $scope.put_cancel = async function () {
    console.log("put_cancel");
    await eel.put_cancel()();
  };

  $scope.heartClicks = function () {
    $scope.isFavorite = ($scope.isFavorite == 0) ? 1 : 0;
  }

});