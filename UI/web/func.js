async function get_weather(){ 
    
    var weather = await eel.weather_to_js()()  
    json = JSON.parse(weather);

    // document.getElementById("weather_temp").textContent = temp_temp; // 原始寫法

    if(json.temp != -1) {
        var tempStr = "現在溫度: " + json.temp;
        document.getElementById("weather_temp").textContent = tempStr;
    }

    if(json.humd != -1) {
       var humdStr = "濕度: " + json.humd;
        document.getElementById("weather_humd").textContent = humdStr;
    }

    if(json.d_tx != -1) {
    var dtxStr = "今日最高溫: " + json.d_tx;
    document.getElementById("weather_d_tx").textContent = dtxStr;
    }
    
    if(json.d_tn != -1) {
    var dtnStr = "今日最高溫: " + json.d_tn;
    document.getElementById("weather_d_tn").textContent = dtnStr;
    }

    if(json.d_txt != -1) {
    var dtxtStr = "今日最高溫時間: " + json.d_txt;
    document.getElementById("weather_d_txt").textContent = dtxtStr;
    }

    if(json.d_tnt != -1) {
    var dtxtStr = "今日最高溫時間: " + json.d_tnt;
    document.getElementById("weather_d_tnt").textContent = dtxtStr;
    }

}
get_weather();