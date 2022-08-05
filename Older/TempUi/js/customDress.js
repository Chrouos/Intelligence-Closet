
/* ---------------------- Angular Start ----------------------*/
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

  /* ---------- 刷新頁面 Start ---------- */
  setInterval(function () {
    $scope.$apply(function () {

    });
  }, 15);
  /* ---------- 刷新頁面 End ---------- */


  $scope.clothesItems = [
    { "Id": 1, "category": "短袖", "color": "白", "createTime": "2022/05/04", "modifyTime": "2022/07/01", "count": 9, "FilePosition": "./public/src/clothes_1.jpg", "like": 5 },
    { "Id": 2, "category": "長袖", "color": "藍", "createTime": "2022/03/26", "modifyTime": "2022/04/07", "count": 2, "FilePosition": "./public/src/clothes_2.jpg", "like": 7 },
    { "Id": 3, "category": "長褲", "color": "咖啡", "createTime": "2022/04/07", "modifyTime": "2022/07/01", "count": 7, "FilePosition": "./public/src/clothes_3.jpg", "like": 3 },
    { "Id": 4, "category": "短褲", "color": "藍", "createTime": "2022/06/21", "modifyTime": "2022/07/04", "count": 3, "FilePosition": "./public/src/clothes_4.jpg", "like": 8 },
  ]

  $scope.nowPosition = 0;
  $scope.min = 0;
  $scope.max = 10;
  $scope.changeClothes = function (direction) {

    // 0 代表向左 => -1
    if (direction == 0) {
      $scope.nowPosition = ($scope.nowPosition > 0) ? $scope.nowPosition - 1 : 3;
    }

    // 0 代表向右 => +1
    else if (direction == 1) {
      $scope.nowPosition = ($scope.nowPosition < 3) ? $scope.nowPosition + 1 : 0;
    }
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
    window.location.replace("main.html");
  }

  $scope.isSaving = false;
  $scope.saveOk = false;

  $scope.save = function () {
    $scope.isSaving = true;

    setTimeout(function () {
      $scope.isLoading = false;
      $scope.saveOk = true;
    }, 3000);
  }


});


