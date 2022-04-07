async function get_weather(){ 
    

    weather = await eel.weather_to_js()()  
  
    document.getElementById('weather_panel').textContent = weather
}
get_weather();