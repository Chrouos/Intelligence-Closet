import eel

@eel.expose #用decorator的方式，將JS要呼叫的PY function暴露給eel, 讓eel當作一個library  去給JS使用
def weather_to_js():      

    return 30.8

eel.init('web') # eel.init(網頁的資料夾)
eel.start('main.html',size = (600,400)) #eel.start(html名稱, size=(起始大小))