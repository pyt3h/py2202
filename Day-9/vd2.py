import requests
url = 'http://api.openweathermap.org/data/2.5/forecast?id=1581129&units=metric&appid=d6477696b63c2e661af64eead58c11d9&cnt=8'
data = requests.get(url).json()

for item in data['list']:
    time = item['dt_txt']
    temp = item['main']['temp']
    humidity = item['main']['humidity']
    print(f'Thời tiết lúc {time} (UTC): nhiệt độ: {temp} độ C, độ ẩm {humidity} %')