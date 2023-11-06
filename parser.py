from bs4 import BeautifulSoup # ипортируем библиотеку для разбора html-страницы на отдельные блоки
import requests # импортируем библиотеку для совершения запросов в интернет

url = 'https://www.cbr.ru/currency_base/daily/' # адрес, на который будем совершать запрос


page = requests.get(url) # совершаем запрос на адрес, а полученнный ответ сохраняем в переменную page
print(f'Статус ответа: {page.status_code}') # проверяем статус ответа, 200 - успешно, 4** - ошибки клиента, 5** - ошибки на сервере

soup = BeautifulSoup(page.text, "html.parser") # создаём объект BeautifulSoup, передав полученную из запроса html-страницу

data = soup.findAll('td') # ищем на html-странице все элементы "td", получаем список элементов, сохраняем в переменную data 


# осуществляем поиск элементов, содержимым которых является текст "Доллар США" и "Евро" 
for d in data:
    if d.text == 'Доллар США':
        print(f'{d.text}: {data[data.index(d) + 1].text} руб.') # выводим текущий курс доллара
        usd = float(data[data.index(d) + 1].text.replace(',', '.'))
    if d.text == 'Евро':
        print(f'{d.text}: {data[data.index(d) + 1].text} руб.') # выводим текущий курс евро
        eur = float(data[data.index(d) + 1].text.replace(',', '.'))

# полученные данные можно использовать в конвертере валют
print('') # пустая строка
print(round(int(input('Введите кол-во долларов необходимое перевсти в рубли: ')) * usd, 2))


print('') # пустая строка
print(round(int(input('Введите кол-во евро необходимое перевсти в рубли: ')) * eur, 2))


