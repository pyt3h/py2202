import requests

url = 'http://api.openweathermap.org/data/2.5/weather?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9'
data = requests.get(url).json()
print('Nhiệt độ:', data['main']['temp'], ' độ C')
print('Độ ẩm:', data['main']['humidity'], '%')