import json

# Nhan du lieu tu file text

text = '''
[{"time": "20220318T19:00:00", "temp": 26, "humidity": 90}, {"time": "20220318T21:00:00", "temp": 25, "humidity": 92}, {"time": "20220318T23:00:00", "temp": 24, "humidity": 95}]
'''

weather_data = json.loads(text)

print('Thoi gian | Nhiet do | Do Am')
for item in weather_data:
    print(item['time'], item['temp'], item['humidity'])