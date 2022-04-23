
/* ---------------------- Angular Start ----------------------*/ 
var app = angular.module('myApp', []);
app.controller('myCtrl', function ($scope) {


    // 從 Python中 獲得所有城鎮 顯示在 option 選項中
    async function get_station_city(){
        var stationAllCity = await eel.station_city_to_js()(); 
        var lis = stationAllCity.split(",")
        $scope.allCitys = lis; // 字串轉陣列
    }; get_station_city();

    // 從 Python中 獲得縣市氣象站別 顯示在 option 選項中
    async function isCity_getStationByCity(){
        var stationByCity = await eel.station_station_to_js($scope.selectedCity)(); 
        var lis = stationByCity.split(",")
        // $scope.stationByCity = stationByCity.split(","); // 字串轉陣列
        $scope.stationByCity = lis;
    }

    // 從 Python中 獲得天氣資訊(溫度、濕度、最高溫+時間、最低溫+時間)
    async function get_weather(type){ 

        if (type == 1)
            var getWeatherPosition = document.getElementById("inputWeatherPosition").value;
        else if(type == 2)
            var getWeatherPosition = $scope.selectedStation;


        var weather = await eel.weather_to_js(getWeatherPosition)()  
        json = JSON.parse(weather);

        // document.getElementById("weather_temp").textContent = temp_temp; // 原始寫法

        if(json.temp != -1) {
            var tempStr = "現在溫度: " + json.temp;
            document.getElementById("weather_temp").textContent = tempStr;
        } else{
            document.getElementById("weather_temp").textContent = "該區目前未提供溫度"
        }

        if(json.humd != -1) {
        var humdStr = "濕度: " + json.humd;
            document.getElementById("weather_humd").textContent = humdStr;
        } else{
            document.getElementById("weather_humd").textContent = "該區目前未提供濕度"
        }

        if(json.d_tx != -1) {
        var dtxStr = "今日最高溫: " + json.d_tx;
        document.getElementById("weather_d_tx").textContent = dtxStr;
        } else{
            document.getElementById("weather_d_tx").textContent = "該區目前未提供最高溫"
        }
        
        if(json.d_tn != -1) {
        var dtnStr = "今日最高溫: " + json.d_tn;
        document.getElementById("weather_d_tn").textContent = dtnStr;
        } else{
            document.getElementById("weather_d_tn").textContent = "該區目前未提供最低溫"
        }

        if(json.d_txt != -1) {
        var dtxtStr = "今日最高溫時間: " + json.d_txt;
        document.getElementById("weather_d_txt").textContent = dtxtStr;
        } else{
            document.getElementById("weather_d_txt").textContent = "該區目前未提供最高溫時間"
        }

        if(json.d_tnt != -1) {
        var dtxtStr = "今日最高溫時間: " + json.d_tnt;
        document.getElementById("weather_d_tnt").textContent = dtxtStr;
        } else{
            document.getElementById("weather_d_tnt").textContent = "該區目前未提供最低溫時間"
        }

    }

    $scope.getStation = function(){
        isCity_getStationByCity();
    }

    $scope.getWeather = function(type){
        get_weather(type);
    }



});


