# -*- coding: utf-8 -*-
"""Копия блокнота "Практика 0.7.0.ipynb"

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10IG5oyVK6a2lkVAW18Uxo8CdYpd5gmMF
"""

https://drive.google.com/file/d/16Cm2tgrpuDH8eIdxdSYyOsfDPqnJ3byd/view?usp=sharing

"""ФИО:"""



"""## Задание 1. HTTP-запросы, ответы и погода

Описание:

Напишите HTTP-запрос для получения информации о погоде в введенном городе из API.

Можно использовать API: https://open-meteo.com/. Используйте метод GET.


Ввод
```
56.50, 60.35
```

Вывод
```
Сегодня (1.11) погода 20 ◦С, нет осадков, туман
```
"""

pip install requests

import requests

data = input('Введите данные(долготу и широту)').split(', ')
url = f'https://api.open-meteo.com/v1/forecast?latitude='+str(data[0])+'&longitude='+str(data[1])+'&current=temperature_2m,rain,showers,snowfall,weather_code'
response = requests.get(url)

status_code = response.status_code
json = response.json()

for k, v in json:
    dict1['time'] = json[]

print(response.status_code)
print(response.json())

import requests

data = input('Введите данные(долготу и широту)').split(', ')
url = f'https://api.open-meteo.com/v1/forecast?latitude='+str(data[0])+'&longitude='+str(data[0])+'&current_weather=true'
response = requests.get(url)

current_weather = weather_data['current_weather']
temperature = current_weather['temperature']
weather_description = current_weather['weathercode']

weather_descriptions = {0: "ясно", 1: "малооблачно", 2: "облачно", 3: "пасмурно", 45: "туман", 48: "морозный туман", 61: "небольшой дождь", 63: "умеренный дождь", 80: "небольшой дождь", 81: "дождь", 90: "небольшой снег", 95: "гроза"}

description = weather_descriptions.get(weather_description, "неизвестно")

from datetime import datetime
today = datetime.now()

print(f"Сегодня ({today.day}.{today.month}) погода {temperature} °C, {description}")

"""## Задание 2. HTTP-запросы, ответы и покемоны

**Описание:**


Создайте код программы, которая будет взаимодействовать с API, со следующим функионалом:

1. Используя метод GET, отправьте запрос на endpoint /pokemon, чтобы получить список первых 20 покемонов

2. Извлеките имена покемонов из ответа и выведите их списком

3. Введите с помощью input() название одного из покемонов


```
Имя покемона: clefairy
```



4. Отправьте GET-запрос, чтобы получить полную информацию о выбранном покемоне

5. Извлеките и выведите следующие данные о введенном покемоне:

     • Имя

     • Тип

     • Вес

     • Рост

     • Способности

Используйте PokéAPI (https://pokeapi.co/), который предоставляет информацию о покемонах, их характеристиках, типах и другую информацию.
"""



"""## Задание 3. HTTP-запросы, ответы и посты

**Описание:**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API, реализуя следующие функции:

1. Реализуйте функцию, которая выполняет GET-запрос к https://jsonplaceholder.typicode.com/posts и возвращает список постов в формате JSON

2. Реализуйте функцию, котороая получает вводимое ID поста, выполняет GET-запрос по ID и возвращает данные поста в формате JSON

3. Реализуйте функцию, которая выполняет обработку JSON из пункта 2 и выводит всю важную информацию в консоль
"""



"""## Задание 4. HTTP-запросы, ответы и работа с постами

**Описание**

Создайте программу, которая будет взаимодействовать с JSONPlaceholder API (из предыдущего задания), реализуя новые функции:

1. Реализуйте функцию, которая принимает заголовок, содержимое и ID пользователя (информация вводится с помощью input()), выполняет POST-запрос для создания нового поста и возвращает информацию о созданном посте в формате JSON


```
Заголовок: Новый пост
Содержимое поста: Тут должно находиться содержимое нового поста...
ID пользователя: 10
```



2. Реализуйте функцию, которая принимает ID поста, новый заголовок и новое содержимое, выполняет PUT-запрос и возвращает обновлённый пост в формате JSON

3. Реализуйте функцию, которая принимает ID поста, выполняет DELETE-запрос и возвращает статус-код ответа
"""



"""## Задание 5. HTTP-запросы, ответы и пёсики

**Описание**

Создайте программу, которая будет взаимодействовать с Dog API, которая позволит получать список пород собак, вводить несколько пород и получать их фотогрфии.

Этапы:

1. Создайте функцию, которая использует метод GET и возвращает список всех пород собак в формате нумерованного списка

2. Реализуйте возможность ввода нескольких пород собак через запятую


```
african, chow, dingo
```



3. Создание функции, которая реализует запрос, возвращает и выводит изображениия собак, породы которых были введены до этого


Используйте Dog API (https://dog.ceo/dog-api/), который предоставляет информацию о породах собак и их изображения.

*Подсказка*



```
import requests
from PIL import Image
from IPython.display import display
import io

url =
response =
        
if response.status_code == 200:
      image_url = response.json()['message']

res = requests.get(image_url)
img = Image.open(io.BytesIO(res.content))
display(img)
```
"""

