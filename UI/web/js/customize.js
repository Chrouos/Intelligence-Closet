var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {

	var getUpperIndex;//上衣的index
	var getLowerIndex;//褲子的index

	upperCloth();
	lowerCloth();

	function upperCloth(){
		$('.columns #upper').each( function(eq) {
			$(this).off().click( function() {//當點擊上衣的任一件
				//console.log(getUpperIndex);
				$('.upHide').eq(getUpperIndex).hide();//上一件點選的衣服會從黃框變藍框
				$('.upShow').eq(getUpperIndex).show();
				window.setTimeout( function() {
					$('.upShow').eq(eq).hide();//這次點選的的衣服會從藍框變黃框
					$('.upHide').eq(eq).show();
				});
				getUpperIndex=eq;//抓取當前衣服的index
			});
		});
	}

	function lowerCloth(){
		$('.columns #lower').each( function(eq) {
			$(this).off().click( function() {
				//console.log(getLowerIndex);
				$('.loHide').eq(getLowerIndex).hide();//上一件點選的褲子會從黃框變藍框
				$('.loShow').eq(getLowerIndex).show();
				window.setTimeout( function() {
					$('.loShow').eq(eq).hide();//這次點選的的褲子會從藍框變黃框
					$('.loHide').eq(eq).show();
				});
				getLowerIndex=eq;//抓取當前褲子的index
			});
		});
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