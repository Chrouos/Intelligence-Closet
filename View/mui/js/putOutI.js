

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    $scope.putOItype = false

    // 從 Python中 獲得天氣資訊
    $scope.weather_to_js = async function () {
        $scope.weather = await eel.weather_to_js()();
    }; $scope.weather_to_js();

    //衣物資料
    $scope.showInfo = function (clothesID) {
        //TODO:用clothesID呼叫衣物資料
        console.log("clothesID",clothesID)

        //$scope.clothesNode = $scope.pageList[arr[1]];
        //$scope.weather = await eel.query_clothesNode_byId()();

        $scope.putOItype = !$scope.putOItype;
    }

    $scope.backToMain = function () {
        $scope.putOItype = !$scope.putOItype;
    }

    // 抓取全部資料
    $scope.queryAllList = async function () {
        $scope.clothesGraphList = await eel.comb_to_js()();
        console.log("$scope.clothesGraphList", $scope.clothesGraphList);
        $scope.maxPage = Math.ceil($scope.clothesGraphList.length/'5');
        console.log("$scope.maxPage", $scope.maxPage )
        $scope.setData();
    }
    $scope.queryAllList();

    $scope.page = 1;
    $scope.pageList = {};
    $scope.setData = function () {
        var count = 0;
        for (var i = ($scope.page - 1) * 5; i < ($scope.page - 1) * 5 + 5; i++) {
            $scope.pageList[count] = $scope.clothesGraphList[i];
            count++;
        }
    }
        
    //上一頁
    $scope.Previous = function () {
        $scope.page = $scope.page - 1;
        $scope.setData();
    }
    //下一頁
    $scope.Next = function () {
        $scope.page = $scope.page + 1;
        $scope.setData();
    };


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
            showMask();
        }
    }, 100);
}
function holdUp() {
    clearInterval(time);
}