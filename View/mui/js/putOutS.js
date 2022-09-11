function takeClick(a) {
  if (a.style.background - color == "white")
    a.style.background.color = "red";
  else
    a.style.background.color = "white";
}

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */

  /* ********************** 選單 *********************** */

  $scope.queryAllList = async function () {
    // $scope.upperList = await eel.upper_clothes_to_js()(); // 上半身的所有衣服

    $scope.upperList = await eel.query_subCategory_byCategoryId(1)(); // 上半身的子類別
    $scope.lowerList = await eel.query_subCategory_byCategoryId(2)(); // 下半身的子類別
    $scope.otherList = await eel.query_subCategory_byCategoryId(3)(); // 下半身的子類別

    $scope.clothesNodeList = await eel.clothes_to_js()();
    console.log("clothesNodeList: ", $scope.clothesNodeList)

  }
  $scope.queryAllList();

  // 搜尋衣物 by.子類別ID
  $scope.queryClothesBySubCategory = async function (subCategoryId) {
    $scope.clothesNodeList = await eel.query_clothes_nodes_bySubCategoryId(subCategoryId)();
  }

  $scope.siglePickUpList = null; // 只拿取一件衣物: JSON
  $scope.pairPickUpList = [null, null]

  $scope.checkThePickUpList = function (clothesNode) {
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

      console.log("sigle: ", $scope.siglePickUpList);
    }
    // 整套
    else {


      var isInsert = true;
      for (var i = 0; i < 2; i++) {
        // 如果有Id一樣的就拿掉
        if ($scope.checkThePickUpList[i] != null) {
          if ($scope.checkThePickUpList[i].Id == clothesNode.Id) {
            $scope.checkThePickUpList[i] = null;
            document.getElementById("clothesNode_" + $scope.checkThePickUpList[i].Id).style.border = "";
          }
        }
        // 
        else if ($scope.checkThePickUpList == null && isInsert) {
          $scope.pairPickUpList[i] = clothesNode;
          isInsert = false;
        }

      }
      console.log("pair: ", $scope.pairPickUpList);



    }

    $scope.pickUpTheStyle();

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
  $scope.takeType = false; //拿單件or整套 false: 單件, true: 整套
  $scope.changePickUpType = function () { // 拿單件or整套
    $scope.takeType = !$scope.takeType;

    $scope.siglePickUpList = null;
    $scope.pairPickUpList = [null, null];
  }

  // 拿取 衣物
  $scope.getThePickUpList = function () {
    // sigle
    if ($scope.takeType == false) {
      console.log("pick up the sigle clothes: ", $scope.siglePickUpList);
    }
    else {
      console.log("pick up the pair clothes List: ", $scope.pairPickUpList);
    }
  }

  /* ********************** 選擇 *********************** */

  // $scope.Data = [//假資料
  //   { 'Picture': './public/src/clothes_1.jpg' },
  //   { 'Picture': './public/src/clothes_2.jpg' },
  //   { 'Picture': './public/src/clothes_3.jpg' },
  //   { 'Picture': './public/src/clothes_4.jpg' },
  //   { 'Picture': './public/src/clothes_5.jpg' },
  //   { 'Picture': './public/src/clothes_6.jpg' },
  //   { 'Picture': './public/src/clothes_7.jpg' },
  //   { 'Picture': './public/src/clothes_8.jpg' },
  //   { 'Picture': '' },
  //   { 'Picture': '' },
  //   { 'Picture': '' },
  //   { 'Picture': '' }
  // ]



  $scope.takeOnly = ""; // 拿取單件

  $scope.takeTwiceSt = "";//拿取整套-第一件
  $scope.takeTwiceNd = "";//拿取整套-第二件




});