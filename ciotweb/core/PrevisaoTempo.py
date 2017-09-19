import urllib.request, json

def obter(latitude, longitude):
    url = "http://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&units=metric&lang=pt&APPID=d34d3ca4cb68fd45f6ff3d7a914d5943".format(latitude, longitude)

    with urllib.request.urlopen(url) as url:
        previsao = json.loads(url.read().decode())


    return previsao
