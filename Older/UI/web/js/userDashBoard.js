var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

	$scope.addWeatherLike = 50;

	var SliderValue = [];//索取各個衣服的喜好程度

	//時時更新每個slider的值
	function findOutputForSlider(el) {
		var idVal = el.id;
		outputs = document.getElementsByTagName('output');
		for (var i = 0; i < outputs.length; i++) {
			if (outputs[i].htmlFor == idVal) {
				SliderValue[i] = outputs[i];
				return outputs[i];
			}
		}
	}
	var sliders = document.querySelectorAll('input[type="range"].slider');
	[].forEach.call(sliders, function (slider) {
		var output = findOutputForSlider(slider);
		if (output) {
			slider.addEventListener('input', function (event) {
				output.value = event.target.value;
			});
		}
	});


	var button = document.querySelector('.is-success');
	button.addEventListener('click', function () { //點選儲存鍵觸發
		//var name = $("#name").val();
		var name = document.getElementById("name").value;//get name Tag
		//console.log(name);
		if (name.replace(/(^\s)|(\s*$)/g, "") == "")//若沒輸入名字或輸入空白鍵
			alert('請輸入你的名字!');
		else
			save();//執行此函式
	});
	function save(e) {
		//console.log(SliderChoose[0].value);
		//console.log(SliderChoose[1].value);
		//console.log(SliderChoose[2].value);
		if (confirm('確定要儲存?') == true) { //alert確認是否儲存
			window.location.href = 'lobby.html';//點選確定後回到主頁面
		}
	};

});