function takeClick(a) {
  if (a.style.background - color == "white")
    a.style.background.color = "red";
  else
    a.style.background.color = "white";
}
var timeStart, timeEnd, time;


//獲取此刻時間
function getTimeNow() {
  var now = new Date();
  return now.getTime();
}
function holdDown(CID) {
  timeStart = getTimeNow();
  //每100毫秒執行一次
  time = setInterval(function () {
    timeEnd = getTimeNow();
    //如果按超過2s
    if (timeEnd - timeStart > 1000) {
      clearInterval(time);
      //呼叫衣物資訊
      var a = CID.id;
      // console.log(a)
      angular.element(document.getElementById('putOS-Info')).scope().showInfo(a.substr(12));
      showMask();
    }
  }, 100);
}
function holdUp() {
  clearInterval(time);
}

/* ----------------------------------------------------------------------------------------------------- */
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */

  $scope.takeType = false; //拿單件 or 整套, false: 單件, true: 整套

  // 從 Python中 獲得天氣資訊
  $scope.weather_to_js = async function () {
    $scope.weather = await eel.weather_to_js()();
  }; $scope.weather_to_js();

  /* ********************** 選單 *********************** */

  $scope.queryAllList = async function () {
    // $scope.upperList = await eel.upper_clothes_to_js()(); // 上半身的所有衣服

    $scope.upperList = await eel.query_subCategory_byCategoryId(1)(); // 上半身的子類別
    $scope.lowerList = await eel.query_subCategory_byCategoryId(2)(); // 下半身的子類別
    $scope.otherList = await eel.query_subCategory_byCategoryId(3)(); // 下半身的子類別

    $scope.clothesNodeList = await eel.clothes_to_js()();

  }
  $scope.queryAllList();

  // 搜尋衣物 by.子類別ID
  $scope.nowSubCategory = "";
  $scope.queryClothesBySubCategory = async function (subCategoryId, subCategoryName) {
    $scope.clothesNodeList = await eel.query_clothes_nodes_bySubCategoryId(subCategoryId)();
    $scope.nowSubCategory = subCategoryName;
    console.log($scope.nowSubCategory)
  }

  // 搜尋衣物 by.類別
  $scope.queryClothesByCategory = async function (categoryId) {
    if (categoryId == 1)
      $scope.clothesNodeList = await eel.upper_clothes_to_js()();
    else if (categoryId == 2)
      $scope.clothesNodeList = await eel.lower_clothes_to_js()();
    else if (categoryId == 3)
      $scope.clothesNodeList = await eel.other_clothes_to_js()();
    else if (categoryId == 0)
      $scope.clothesNodeList = await eel.clothes_to_js()();

    $scope.nowSubCategory = null;
  }

  // 搜尋衣物 by.最愛&類別
  $scope.queryClothesByIsFavorite = async function (isFavorite) {
    $scope.clothesNodeList = await eel.isFavorite_clothes_to_js(isFavorite)();

    $scope.nowSubCategory = null;
  }

  // 拿取衣物: 
  $scope.takeOut = async function () {

    // TODO: step1: 把衣物位置position = null
    // TODO: step2: 硬體啟動

    // 單件 // 
    if ($scope.takeType == false) {
      console.log("updateThePickUpListToNull ", $scope.siglePickUpList.Position)

      var dialog = bootbox.dialog({
        message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 等待衣物拿取中... </p>',
        closeButton: false
      });
      $scope.info_clothesNode = await eel.updatePositionToNull($scope.siglePickUpList.Position)().then(function () {
        dialog.modal('hide'); // 等待時間到就將bootbox隱藏
      });
      $scope.clothesNodeList = await eel.clothes_to_js()();
      $scope.siglePickUpList = null;
    }
    // 一套
    else if ($scope.takeType == true) {

    }
  }

  $scope.siglePickUpList = null; // 只拿取一件衣物: JSON
  $scope.pairPickUpList = [null, null]
  $scope.chosen = false;
  $scope.checkThePickUpList = function (clothesNode) {

    /*
    if (clothesNode.Position == null) {

      var dialog = bootbox.alert({
        message: "衣櫃內不存在此衣物",
        locale: 'ar'
      });

    }*/
    //else {
      // step 1. Judging how to take it
      // 單件
      if ($scope.takeType == false) {

        // 代表重複: 取消
        if ($scope.siglePickUpList != null) {
          if ($scope.siglePickUpList.Id == clothesNode.Id) {
            document.getElementById("clothesNode_" + clothesNode.Id).style.border = "";
            $scope.siglePickUpList = null;
          }
        }
        // 代表無資料: 存入
        else $scope.siglePickUpList = clothesNode;
        //console.log("sigle: ", $scope.siglePickUpList);
      }
      // 整套
      else {
        var isInsert = true;
        for (var i = 0; i < 2; i++) {
          // 如果有Id一樣的就拿掉
          if ($scope.pairPickUpList[i] != null) {
            if ($scope.pairPickUpList[i].Id == clothesNode.Id) {
              document.getElementById("clothesNode_" + $scope.pairPickUpList[i].Id).style.border = "";
              $scope.pairPickUpList[i] = null;
              isInsert = false;
            }
          }
          // 放入
          else if ($scope.pairPickUpList[i] == null && isInsert) {
            $scope.pairPickUpList[i] = clothesNode;
            isInsert = false;
          }
        }
      }

      $scope.pickUpTheStyle();
    //}
  }

  $scope.pickUpTheStyle = function () {
    // // 單件
    if ($scope.takeType == false && $scope.siglePickUpList != null) {
      document.getElementById("clothesNode_" + $scope.siglePickUpList.Id).style.border = "2px solid red"
    }
    else {
      for (var i = 0; i < 2; i++) {
        if ($scope.pairPickUpList[i] != null) {
          document.getElementById("clothesNode_" + $scope.pairPickUpList[i].Id).style.border = "2px solid red"
        }
      }
    }

  };


  //切換拿取衣物的選擇
  $scope.changePickUpType = function () { // 拿單件or整套
    $scope.takeType = !$scope.takeType;

    if ($scope.siglePickUpList != null) {
      document.getElementById("clothesNode_" + $scope.siglePickUpList.Id).style.border = ""
    }
    $scope.siglePickUpList = null;

    for (var i = 0; i < 2; i++) {
      if ($scope.pairPickUpList[i] != null) {
        document.getElementById("clothesNode_" + $scope.pairPickUpList[i].Id).style.border = ""
      }
    }
    $scope.pairPickUpList = [null, null];
  }

  // 拿取衣物
  $scope.queryThePickUpList = async function (clothesID) {
    $scope.info_clothesNode = await eel.query_clothesNode_byId(clothesID)();
  }


  $scope.putOStype = false
  //衣物資料
  $scope.showInfo = function (clothesID) {
    //TODO:用clothesID呼叫衣物資料
    console.log(clothesID)
    $scope.queryThePickUpList(clothesID);
    $scope.putOStype = !$scope.putOStype;
  }
  $scope.backToMain = function () {
    $scope.putOStype = !$scope.putOStype;
  }




  // color 
  $scope.isPositionNull = function (position) {

    if (position === null) {
      return { opacity: "25%" }
    }
    else
      return { opacity: "100%" }
  }
});