

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    $scope.putOItype = false

    //衣物資料
    $scope.showInfo = function (clothesID) {
        //TODO:用clothesID呼叫衣物資料
        console.log(clothesID)
        $scope.putOItype = !$scope.putOItype;
    }
    $scope.backToMain = function () {
        $scope.putOItype = !$scope.putOItype;
    }

});

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
            angular.element(document.getElementById('putOutI_main')).scope().showInfo(a.substr(12));
        }
    }, 100);
}
function holdUp() {
    clearInterval(time);
}