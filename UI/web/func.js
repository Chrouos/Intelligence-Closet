async function get_weather(){ 
    
    var weather = await eel.weather_to_js()()  
    json = JSON.parse(weather);
  
    document.getElementById('weather_panel').textContent = json;
}
get_weather();