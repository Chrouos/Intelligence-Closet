var timeStart, timeEnd, time;
//獲取此刻時間
function getTimeNow() {
        var now = new Date();
        return now.getTime();
    }
function holdDown(SBC) {
    //獲取滑鼠按下時的時間
    timeStart = getTimeNow();

    //setInterval會每100毫秒執行一次，也就是每100毫秒獲取一次時間
    time = setInterval(function () {
        timeEnd = getTimeNow();

        //如果此時檢測到的時間與第一次獲取的時間差有1000毫秒
        if (timeEnd - timeStart > 1000) {
            //便不再繼續重復此函數 （clearInterval取消周期性執行）
            clearInterval(time);
            //字體變紅
            console.log(SBC.id)
            angular.element(document.getElementById('YourElementId')).scope().myfunction(SBC);
        }
    }, 100);
}
function holdUp() {
    //如果按下時間不到1000毫秒便彈起，
    clearInterval(time);
}
function ppp(AAA){
    console.log(AAA)
}



var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    //滑鼠按下時觸發

    $scope.hahaha=false;
    $scope.lalala = function () {
        $scope.hahaha=!$scope.hahaha;
        console.log("456")
    }

    $scope.myfunction = function (SBC) {
        //console.log(SBC)
    };

});