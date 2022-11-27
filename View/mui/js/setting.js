
function heartClick(a) {
    if (a.style.color == "gray")
        a.style.color = "red";
    else
        a.style.color = "gray";
}

var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

    /* ---------- 刷新頁面 Start ---------- */
    setInterval(function () {
        $scope.$apply(function () {

        });
    }, 15);
    /* ---------- 刷新頁面 End ---------- */

    // 從 Python中 獲得天氣資訊
    $scope.weather_to_js = async function () {
        $scope.weather = await eel.weather_to_js()();
    }; $scope.weather_to_js();

    // 抓取全部資料
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
    $scope.nowSubCategory = "";
    $scope.queryClothesBySubCategory = async function (subCategoryId, subCategoryName) {
        $scope.clothesNodeList = await eel.query_clothes_nodes_bySubCategoryId(subCategoryId)();
        $scope.nowSubCategory = subCategoryName;
        console.log($scope.nowSubCategory)
    }

    $scope.pickUp_FirstClohtesNode = null; // 選擇的第一件衣物
    $scope.checkTheFirstPickUpList = function (clothesNode) {
        // 如果為空 則選取
        if ($scope.pickUp_FirstClohtesNode == null) {
            document.getElementById("clothesNode_" + clothesNode.Id).style.border = "2px solid red";
            $scope.pickUp_FirstClohtesNode = clothesNode;
        }
        // 如果點選同樣資料 就取消
        else if ($scope.pickUp_FirstClohtesNode.Id == clothesNode.Id) {
            document.getElementById("clothesNode_" + clothesNode.Id).style.border = "";
            $scope.pickUp_FirstClohtesNode = null;
        }
        else{
            //console.log('pickUp_FirstClohtesNode.Id',pickUp_FirstClohtesNode.Id)
            document.getElementById("clothesNode_" + $scope.pickUp_FirstClohtesNode.Id).style.border = "";
            document.getElementById("clothesNode_" + clothesNode.Id).style.border = "2px solid red";
            $scope.pickUp_FirstClohtesNode = clothesNode;
        }
    }

    $scope.pickUp_SecondClohtesNode = null; // 選擇的第二件衣物
    $scope.checkTheSecondPickUpList = function (clothesNode) {
        // 如果為空 則選取
        if ($scope.pickUp_SecondClohtesNode == null) {
            document.getElementById("clothesSecondNode_" + clothesNode.Id).style.border = "2px solid red";
            $scope.pickUp_SecondClohtesNode = clothesNode;
        }
        // 如果點選同樣資料 就取消
        else if ($scope.pickUp_SecondClohtesNode.Id == clothesNode.Id) {
            document.getElementById("clothesSecondNode_" + clothesNode.Id).style.border = "";
            $scope.pickUp_SecondClohtesNode = null;
        }
        else{
            //console.log('pickUp_SecondClohtesNode.Id',pickUp_SecondClohtesNode.Id)
            document.getElementById("clothesSecondNode_" + $scope.pickUp_SecondClohtesNode.Id).style.border = "";
            document.getElementById("clothesSecondNode_" + clothesNode.Id).style.border = "2px solid red";
            $scope.pickUp_SecondClohtesNode = clothesNode;
        }
    }

    /* ---------- 將資料儲存至料庫 Start ---------- */
    $scope.creatNodeGraph = async function () { // 送出
        // console.log("$scope.pickUp_FirstClohtesNode",$scope.pickUp_FirstClohtesNode);
        // console.log("$scope.pickUp_SecondClohtesNode",$scope.pickUp_SecondClohtesNode);
        // console.log("$scope.clothesMath_like",$scope.clothesMath_like);
        var isSuccess = await eel.creat_node_graph($scope.pickUp_FirstClohtesNode, $scope.pickUp_SecondClohtesNode, $scope.clothesMath_like);
        
        $scope.backToMain();
        
    }

    /* ---------- 切換頁面 start ---------- */
    $scope.settingType_Main = true; // 主頁面

    $scope.settingType_Single = false;
    $scope.settingType_Match_st = false;
    $scope.settingType_Match_nd = false;

    $scope.backToMain = function () {
        $scope.settingType_Main = true;
        $scope.settingType_Single = false;
        $scope.settingType_Match_st = false;
        $scope.settingType_Match_nd = false;
    }

    $scope.goToMatch = function () {
        $scope.settingType_Main = false;
        $scope.settingType_Match_st = true;
        $scope.settingType_Match_nd = false;
        $scope.settingType_Single = false;

        if($scope.pickUp_SecondClohtesNode != null){
            document.getElementById("clothesSecondNode_" + $scope.pickUp_SecondClohtesNode.Id).style.border = "";
            $scope.pickUp_SecondClohtesNode = null;
        }
    }

    $scope.goToSingle = function () {
        $scope.settingType_Main = false;
        $scope.settingType_Match_st = false;
        $scope.settingType_Match_nd = false;
        $scope.settingType_Single = true;
    }

    $scope.goToMatchNd = function () {
        $scope.settingType_Main = false;
        $scope.settingType_Match_st = false;
        $scope.settingType_Match_nd = true;
        $scope.settingType_Single = false;
    }

    //衣物設定介面
    $scope.clothesSetType = false;
    $scope.clothes_Set = function () {
        $scope.clothesSetType = !$scope.clothesSetType;
    }
    /* ---------- 切換頁面 end ---------- */



});

