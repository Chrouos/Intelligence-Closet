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
  $scope.upSet = false; // 上半身子選項
  $scope.downSet = false; // 下半身子選項
  $scope.otherSet = false; // 其他子選項

  $scope.queryAllList = async function () {
    // $scope.upperList = await eel.upper_clothes_to_js()(); // 上半身的所有衣服

    $scope.upperList = await eel.query_subCategory_byCategoryId(1)(); // 上半身的子類別
    $scope.lowerList = await eel.query_subCategory_byCategoryId(2)(); // 下半身的子類別
    $scope.otherList = await eel.query_subCategory_byCategoryId(3)(); // 下半身的子類別

    $scope.clothesNodeList = await eel.clothes_to_js()();
    console.log("clothesNodeList: ", clothesNodeList)

  }
  $scope.queryAllList();

  $scope.queryClothesBySubCategory = async function (subCategoryId) {
    $scope.clothesNodeList = await eel.query_clothes_nodes_bySubCategoryId(subCategoryId)();
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

  $scope.takeType = false;//拿單件or整套 false:單件 true:整套

  $scope.takeTypeClick = function () { // 拿單件or整套
    $scope.takeType = !$scope.takeType;
  }

  $scope.takeOnly = ""; // 拿取單件

  $scope.takeTwiceSt = "";//拿取整套-第一件
  $scope.takeTwiceNd = "";//拿取整套-第二件

  $scope.takeClick = function (takeN) {//選取衣服
    if ($scope.takeType == false) {
      $scope.takeOnly = "takeN";

    }
    else {

    }
  }


});