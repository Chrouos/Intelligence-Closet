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
      angular.element(document.getElementById('hahaha')).scope().showInfo(a.substr(12));
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
    
    $scope.clothesNodeStatus = true;
    for(var i = 0; i < $scope.clothesNodeList.length; i++){
      if($scope.clothesNodeList[i].Position == null){
        $scope.clothesNodeStatus = false;
      }
    }
    console.log("$scope.clothesNodeStatus", $scope.clothesNodeStatus);
  }
  $scope.queryAllList();

  // 搜尋衣物 by.子類別ID
  $scope.nowSubCategory = "";
  $scope.queryClothesBySubCategory = async function (subCategoryId, subCategoryName) {
    $scope.clothesNodeList = await eel.query_clothes_nodes_bySubCategoryId(subCategoryId)();
    $scope.nowSubCategory = subCategoryName;
    console.log($scope.nowSubCategory)
  }

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

  $scope.pickUp_ClohtesNode = null; // 選擇的衣物
  $scope.checkThePickUpList = function (clothesNode) {
      // 如果為空 則選取
      if ($scope.pickUp_ClohtesNode == null) {
          document.getElementById("clothesNode_" + clothesNode.Id).style.border = "2px solid red";
          $scope.pickUp_ClohtesNode = clothesNode;
      }
      // 如果點選同樣資料 就取消
      else if ($scope.pickUp_ClohtesNode.Id == clothesNode.Id) {
          document.getElementById("clothesNode_" + clothesNode.Id).style.border = "";
          $scope.pickUp_ClohtesNode = null;
      }
      else{
      // 如果點選不同資料 就選取
          //console.log('pickUp_ClohtesNode.Id',pickUp_ClohtesNode.Id)
          document.getElementById("clothesNode_" + $scope.pickUp_ClohtesNode.Id).style.border = "";
          document.getElementById("clothesNode_" + clothesNode.Id).style.border = "2px solid red";
          $scope.pickUp_ClohtesNode = clothesNode;
      }
  }

  // clothes node 刪除(該衣物不在衣櫃中)
  $scope.deleteClothes = async function () {
    var isSuccess = await eel.delete_clothes_node($scope.pickUp_ClohtesNode.Id)();

    $scope.queryAllList();
  }

  // clothes 重新存放(該衣物不在衣櫃中)
  $scope.clothesRestore = async function () {
    //TODO:clothes 重新存放
  }


});