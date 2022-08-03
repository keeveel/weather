import requests
from django.shortcuts import render


# 12b81732ac2c1769723ed335b035c02e - key weatherapp

def index(request):
    appid = '12b81732ac2c1769723ed335b035c02e'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid
    city = 'Moscow'
    response = requests.get(url.format(city)).json()
    city_info = {
        'city': city,
        'temp': response['main']['temp'],
        'icon': response['weather'][0]['icon']
    }

    context = {'info': city_info}

    return render(request, 'weather/index.html', context)
