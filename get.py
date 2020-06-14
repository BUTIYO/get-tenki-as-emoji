# -*- coding: utf-8 -*-
import requests
import json

city_name = "Tokyo"
API_KEY = "xxx"
api = "http://api.openweathermap.org/data/2.5/weather?units=metric&q={city}&APPID={key}"

def main():
    res = getData()
    weather_id = res["weather"][0]["id"]
    print(weather_id)
    emo = weahter_to_emoji(str(weather_id))
    print(emo)

def getData():
    url = api.format(city = city_name, key = API_KEY)
    print(url)
    response = requests.get(url)
    data = response.json()
    data = json.loads(response.text)
    # jsonText = json.dumps(data, indent=4)
    # print(jsonText)
    return data


def weahter_to_emoji(id):
    thunderstorm = "⚡️"    # Code: 200's, 900, 901, 902, 905
    drizzle = "☂️"         # Code: 300's
    rain = "☔️"            # Code: 500's
    snowflake = "❄️"       # Code: 600's snowflake
    snowman = "☃️"         # Code: 600's snowman, 903, 906
    atmosphere = "🌫"      # Code: 700's foogy
    clearSky = "☀️"        # Code: 800 clear sky
    fewClouds = "🌤"       # Code: 801 sun behind clouds
    clouds = "☁️"          # Code: 802-803-804 clouds general
    hot = "🔥"             # Code: 904
    defaultEmoji = "🌎"    # default emojis

    if id[0] == '2' or id == '900' or id == '901' or id == '902' or id == '905':
        return thunderstorm
    elif id[0] == '3':
        return drizzle
    elif id[0] == '5':
        return rain
    elif id[0] == '6' or id == '903' or id == '906':
        return snowflake + ' ' + snowman
    elif id == '7':
        return atmosphere
    elif id == '800':
        return clearSky
    elif id == '801':
        return fewClouds
    elif id == '802' or id == '803' or id == '803':
        return clouds
    elif id == '904':
        return hot
    else:
        return defaultEmoji

if __name__ == "__main__":
    main()
