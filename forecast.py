import pyowm
owm = pyowm.OWM('bbc3649126d17d7bb4111c44c6a562d5',language='ru')
my_city = input('ВВедите, какой город интересует:')
observation = owm.weather_at_place(my_city)
w = observation.get_weather()
status = w.get_status()
det_status = w.get_detailed_status()
wind = w.get_wind()['speed']    # {'speed': 4.6, 'deg': 330}
temperature = w.get_temperature('celsius')['temp'] # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
print('Погода в городе : ' + my_city)         
print('Текущий ветер: ' + str(wind))         
print('Текущая температура: ' + str(temperature))
print('Статус: ' + status)
print('Статус подробнее: ' + det_status)