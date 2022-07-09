
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */

  $scope.nowPosition = 0;

  $scope.clothesItems = [
    { "Id": 1, "category": "短袖", "color": "白", "createTime": "2022/05/04", "modifyTime": "2022/07/01", "count": 9, "FilePosition": "./public/src/clothes_1.jpg" },
    { "Id": 2, "category": "長袖", "color": "藍", "createTime": "2022/03/26", "modifyTime": "2022/04/07", "count": 2, "FilePosition": "./public/src/clothes_2.jpg" },
    { "Id": 3, "category": "長褲", "color": "咖啡", "createTime": "2022/04/07", "modifyTime": "2022/07/01", "count": 7, "FilePosition": "./public/src/clothes_3.jpg" },
    { "Id": 4, "category": "短褲", "color": "藍", "createTime": "2022/06/21", "modifyTime": "2022/07/04", "count": 3, "FilePosition": "./public/src/clothes_4.jpg" },
  ]

  $scope.item = $scope.clothesItems[0];
  $scope.changeClothes = function (direction) {

    // 0 代表向左 => -1
    if (direction == 0) {
      $scope.nowPosition = ($scope.nowPosition > 0) ? $scope.nowPosition - 1 : 3;
    }

    // 0 代表向右 => +1
    else if (direction == 1) {
      $scope.nowPosition = ($scope.nowPosition < 3) ? $scope.nowPosition + 1 : 0;
    }
    console.log("now position:", $scope.nowPosition)
    $scope.item = $scope.clothesItems[$scope.nowPosition];

  }



  $scope.returnLobby = function () {
    window.location.replace("main.html");
  }


  $scope.isLoading = false;
  $scope.isGetting = false;

  // 送出
  $scope.submitClothes = function () {
    // alert("你選擇" + $scope.chooseCombId)
    $scope.isLoading = true;

    setTimeout(function () {
      $scope.isLoading = false;
      $scope.isGetting = true;
    }, 3000);
  }

  $scope.returnLobby = function () {
    $scope.isGetting = false;
    $scope.isLoading = false;
    window.location.replace("lobby.html");
  }


});


