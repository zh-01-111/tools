import requests
import json
import datetime
# https://toy1.weather.com.cn/search?cityname=%E6%B8%A9%E5%B7%9E
# http://wthrcdn.etouch.cn/weather_mini?city=
def Weather(city):
    time = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime("%Y/%m/%d")
    url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city
    response = requests.get(url)
    text_data = response.content.decode("utf-8")
    json_data = json.loads(text_data)
    text_data = json.dumps(json_data,indent=4,ensure_ascii=False)
    day = json_data["data"]["forecast"][1]["date"][2:]
    low = json_data["data"]["forecast"][1]["low"][3:]
    high = json_data["data"]["forecast"][1]["high"][3:]
    wea = json_data["data"]["forecast"][1]["type"]
    message = city + ":" + time +day + "," + low + "~" + high + "," + wea
    return message

if __name__ == '__main__':
    data = Weather('南京')
