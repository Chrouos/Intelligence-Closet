var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

	var getUpperIndex;//上衣的index
	var getUpperObject;//上個上衣被選取的Object
	var getLowerIndex;//褲子的index
	var getLowerObject;//上個褲子被選取的Object

	$scope.setUpper = "has-background-info";//將所有上衣邊框設定為藍色
	$scope.setLower = "has-background-info";//將所有褲子邊框設定為藍色

	$scope.upperCloth = function (upper) {
		var upperCloth = $scope.uppers.indexOf(upper);//拿取上衣的index
		console.log(upperCloth);
		if (getUpperIndex != undefined) {
			if (getUpperObject != undefined)//如果有挑選到一件上衣
				getUpperObject.setUpper = "has-background-info";//上一件上衣變回藍色
		}
		this.setUpper = "has-background-warning";//剛點選的上衣框框變為黃色
		getUpperObject = this;//指定當前上衣的物件
		getUpperIndex = upperCloth;//指定當前上衣的index
	}

	//上衣的圖片路徑
	$scope.uppers = [
		{
			url: "./public/src/clothes_1.jpg"
		},
		{
			url: "./public/src/clothes_2.jpg"
		},
		{
			url: "./public/src/clothes_5.jpg"
		}
	];

	$scope.lowerCloth = function (lower) {
		var lowerCloth = $scope.lowers.indexOf(lower);//拿取褲子的index
		console.log(lowerCloth);
		if (getLowerIndex != undefined) {
			if (getLowerObject != undefined)//如果有挑選到一件褲子
				getLowerObject.setLower = "has-background-info";//上一件褲子變回藍色
		}
		this.setLower = "has-background-warning";//剛點選的褲子邊框變為黃色
		getLowerObject = this;//指定當前褲子的物件
		getLowerIndex = lowerCloth;//指定當前褲子的index
	}

	//褲子的圖片路徑
	$scope.lowers = [
		{
			url: "./public/src/clothes_3.jpg"
		},
		{
			url: "./public/src/clothes_4.jpg"
		},
		{
			url: "./public/src/clothes_7.jpg"
		}
	];

	var button = document.querySelector('.is-success');
	button.addEventListener('click', function () {//點選儲存鍵觸發
		if (getUpperObject == undefined || getLowerObject == undefined)//若沒有挑選出上衣及褲子
			alert("請選擇喜歡的上衣及褲子!");
		else
			save();
	});
	function save(e) {
		if (confirm('確定要儲存?') == true) {//alert確認是否儲存
			window.location.href = 'lobby.html';//點選確定後回到主頁面
		}
	};
});