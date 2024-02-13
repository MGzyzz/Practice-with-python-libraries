import requests


# [1]=========================[1]
response = requests.get('https://www.google.com')
print(response.content)
# [1]=========================[1]

# [2]=========================[2]
# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://httpbin.org/post', data=payload)
# print(response.content)
# [2]=========================[2]

# [3]=========================[3]
# url = 'https://upload.wikimedia.org/wikipedia/commons/7/74/Python.png'
# response = requests.get(url)
#
# with open('python.png', 'wb') as f:
#     f.write(response.content)
# [3]=========================[3]

# [4]=========================[4]
# response = requests.get('https://jsonplaceholder.typicode.com/posts')
# data = response.json()
#
# for item in data:
#     print(item['title'])
# [4]=========================[4]

# [5]=========================[5]
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
# response = requests.get('https://www.example.com', headers=headers)
#
# print(response.content)
# [5]=========================[5]

# Библиотека Requests предоставляет простой интерфейс для отправки HTTP-запросов и получения ответов.
# Она облегчает выполнение многих типичных задач, связанных с веб-разработкой и анализом данных.
# Определение кода сверху
# Примечание: коды были закомментированый для того чтобы работал один из кодов.
# Все коды были разделены с помощью знака =
# [1] Получение содержимого веб-страницы
# [2] Отправка POST-запроса
# [3] Загрузка файла с сервера
# [4] Получение JSON-данных из API
# [5] Установка заголовков для запроса
