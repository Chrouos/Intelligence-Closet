
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

  $scope.StartType = true;//開始介面bool
  $scope.MainType = false;//主介面bool

  $scope.putIn = [//資料
    { 'FilePosition': './public/src/clothes_1.jpg', 'color': '白色', 'style': '連帽衫', 'like': 5, 'favorite': false }
  ]



  $scope.heartClicks = function () {
    $scope.putIn.favorite = !$scope.putIn.favorite;
  }

  $scope.Start = function () {//開始辨識
    $scope.StartType = false;
    //TODO bootbox:1.為偵測到衣服，請放入衣服  2.辨識中，請稍等
    $scope.MainType = true;
  }

  $scope.Back = function () {//退回衣服
    $scope.MainType = false;
    //TODO bootbox: 衣服退出中...
    $scope.StartType = true;
  }

  $scope.Send = function () {//送出
    $scope.MainType = false;
    //TODO bootbox: 衣服收入中...
    $scope.StartType = true;
    console.log($scope.putIn)
    //TODO 有個不知道是不是bug 我在DC問你
  }


});