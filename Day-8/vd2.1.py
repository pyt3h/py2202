import json

weather_data = [
    {'time': '20220318T19:00:00', 'temp':26, 'humidity':90},
    {'time': '20220318T21:00:00', 'temp':25, 'humidity':92},
    {'time': '20220318T23:00:00', 'temp':24, 'humidity':95},
]

text = json.dumps(weather_data)
print(text)
