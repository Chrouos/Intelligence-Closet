

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    $scope.putOItype = false
    $scope.checkShow = false
    $scope.proposalStatus=false;
    // 從 Python中 獲得天氣資訊
    $scope.weather_to_js = async function () {
        $scope.weather = await eel.weather_to_js()();
        
        if($scope.weather['UVI'] >=5 || $scope.weather['PoP12h'] >= 30 || $scope.weather['T'] <= 15){
            $scope.proposalStatus=true;
            showMask();
        }
    }; $scope.weather_to_js();

    //衣物資料
    $scope.showInfo = async function (clothesID) {
        // 用clothesID呼叫衣物資料
        //console.log("clothesID",clothesID);

        $scope.clothesInfo = await eel.query_clothesNode_byId(clothesID)();
        //console.log("$scope.clothesInfo",$scope.clothesInfo);

        $scope.set_isFavorite_color();
        $scope.putOItype = !$scope.putOItype;
    }

    $scope.set_isFavorite_color = function (){
        if($scope.clothesInfo != null){
            if($scope.clothesInfo.IsFavorite == 1)
                return { color: "red" };     
            else
                return { color: "gray" };
        }
    }

    $scope.backToMain = function () {
        $scope.putOItype = false;
        $scope.checkShow = false;
        $scope.proposalStatus=false;
        nowClothe = null;
    }

    $scope.pageStatus = true;
    // 抓取全部資料
    $scope.queryAllList = async function () {
        $scope.clothesGraphList = await eel.comb_to_js()();
        $scope.maxPage = Math.ceil($scope.clothesGraphList.length/'5');
        if($scope.clothesGraphList.length == 0){
            $scope.pageStatus = false;
        }
        $scope.setData();

        console.log("comb:", $scope.clothesGraphList);
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

        // 換頁取消選取
        if($scope.pickUp_index != null){
            document.getElementById("clothesGraph_" + $scope.pickUp_index).style.border = "";
            $scope.pickUp_index = null;
            $scope.pickUp_clothesGraph = null;
        }
        $scope.setData();
    }
    //下一頁
    $scope.Next = function () {
        $scope.page = $scope.page + 1;

        // 換頁取消選取
        if($scope.pickUp_index != null){
            document.getElementById("clothesGraph_" + $scope.pickUp_index).style.border = "";
            $scope.pickUp_index= null;
            $scope.pickUp_clothesGraph = null;
        }
        $scope.setData();
    }

    $scope.pickUp_index = null; // 選擇的衣物id
    $scope.pickUp_clothesGraph = null; // 選擇的衣物
    $scope.checkPickUpList = function (index) {
        if((($scope.page-1)*5+index) < $scope.clothesGraphList.length){
            // 如果還未選取 就選取
            if ($scope.pickUp_index == null) {
                document.getElementById("clothesGraph_" + index).style.border = "2px solid red";
                $scope.pickUp_index = index;
                $scope.pickUp_clothesGraph = $scope.clothesGraphList[($scope.page-1)*5+index];
            }
            // 如果點選同樣資料 就取消
            else if ($scope.pickUp_index == index) {
                document.getElementById("clothesGraph_" + index).style.border = "";
                $scope.pickUp_index = null;
                $scope.pickUp_clothesGraph = null;
            }
            else{
            // 如果點選不同資料 就選取
                //console.log('pickUp_ClohtesGraph.Id',pickUp_ClohtesGraph.Id)
                document.getElementById("clothesGraph_" + $scope.pickUp_index).style.border = "";
                document.getElementById("clothesGraph_" + index).style.border = "2px solid red";
                $scope.pickUp_index = index;
                $scope.pickUp_clothesGraph = $scope.clothesGraphList[($scope.page-1)*5+index];
            }
        }
        // console.log("$scope.pickUp_clothesGraph", $scope.pickUp_clothesGraph);
    }

    // 拿取衣物(一套)
    $scope.checkTake = function () {
        console.log("確認拿取:", $scope.pickUp_clothesGraph)
        $scope.checkShow = !$scope.checkShow;
        showMask();
    }

    // 確認拿取(一套)
    $scope.ConfirmTake = async function (){
        
        console.log("拿取衣物1:", $scope.pickUp_clothesGraph.Clothes1Position, ", 拿取衣物2: ",$scope.pickUp_clothesGraph.Clothes2Position)
        $scope.checkShow = !$scope.checkShow;

        var dialog = bootbox.dialog({
            message: '<p class="text-center mb-0"><i class="fa fa-spin fa-cog"></i> 拿取衣物中... </p>',
            closeButton: false
        });
    
        // 放入衣物
        console.log("clothes restore");
        var isSuccess =  await eel.updatePositionToNull_TwoClothes(
            $scope.pickUp_clothesGraph.Clothes1Position, $scope.pickUp_clothesGraph.Clothes2Position,
            $scope.pickUp_clothesGraph)().then(function () {
            dialog.modal('hide'); // 等待時間到就將bootbox隱藏
        });

        $scope.queryAllList();
        showMask();
    }

});

/*
var nowClothe = null;

//獲取此刻時間
function getTimeNow() {
    var now = new Date();
    return now.getTime();
}
function holdDown(CID) {
    
    if(nowClothe == null || CID == nowClothe){
        timeStart = getTimeNow();
        //每100毫秒執行一次
        time = setInterval(function () {
            timeEnd = getTimeNow();
            //如果按超過2s
            if (timeEnd - timeStart > 1000) {
                clearInterval(time);
                //呼叫衣物資訊
                var a = CID.id;
                angular.element(document.getElementById('putOutI_main')).scope().showInfo(a.substr(14));
                showMask();
            }
        }, 0);
    }

    if(CID != nowClothe){
        nowClothe = CID;
    }
}

function holdUp() {
    clearInterval(time);
    nowClothe = null
}
*/

function dclick(CID) {
    //呼叫衣物資訊
    var a = CID.id;
    angular.element(document.getElementById('putOutI_main')).scope().showInfo(a.substr(14));
    showMask();
}

