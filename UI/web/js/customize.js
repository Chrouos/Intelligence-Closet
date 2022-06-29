var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

	var getUpperIndex;//上衣的index
	var getLowerIndex;//褲子的index

	upperCloth();
	lowerCloth();

	$scope.setUpper="has-background-info";
	$scope.setUpper1="has-background-info";
	$scope.setUpper2="has-background-info";

	function upperCloth(){
		$scope.changeUpper=function(){
			$scope.setUpper="has-background-warning";
			$scope.setUpper1="has-background-info";
			$scope.setUpper2="has-background-info";
			getUpperIndex=0;
		};
		$scope.changeUpper1=function(){
			$scope.setUpper="has-background-info";
			$scope.setUpper1="has-background-warning";
			$scope.setUpper2="has-background-info";
			getUpperIndex=0;
		};
		$scope.changeUpper2=function(){
			$scope.setUpper="has-background-info";
			$scope.setUpper1="has-background-info";
			$scope.setUpper2="has-background-warning";
			getUpperIndex=0;
		};
	}
	$scope.setLower="has-background-info";
	$scope.setLower1="has-background-info";
	$scope.setLower2="has-background-info";

	function lowerCloth(){
		$scope.changeLower=function(){
			$scope.setLower="has-background-warning";
			$scope.setLower1="has-background-info";
			$scope.setLower2="has-background-info";
			getLowerIndex=0;
		};
		$scope.changeLower1=function(){
			$scope.setLower="has-background-info";
			$scope.setLower1="has-background-warning";
			$scope.setLower2="has-background-info";
			getLowerIndex=0;
		};
		$scope.changeLower2=function(){
			$scope.setLower="has-background-info";
			$scope.setLower1="has-background-info";
			$scope.setLower2="has-background-warning";
			getLowerIndex=0;
		};
	}

	var button = document.querySelector('.is-success');
   	button.addEventListener('click', function(){//點選儲存鍵觸發
   		if(getUpperIndex == undefined || getLowerIndex == undefined)//若沒有挑選出上衣及褲子
    		alert("請選擇喜歡的上衣及褲子!");
    	else
    		save();
   	});
    function save(e) {
        if (confirm('確定要儲存?') == true) {//alert確認是否儲存
            window.location.href='lobby.html';//點選確定後回到主頁面
        }
    };
});