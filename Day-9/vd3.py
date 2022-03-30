import json
import requests
url = 'https://translation.googleapis.com/language/translate/v2?key=AIzaSyBR8gU4Te36NCYlc2ZdynsOWQOS03lzWKc'

text = input('Nhập đoạn tiếng Việt cần dịch:')
body = {
    "q": text,
    "source": "vi",
    "target": "en",
    "format": "text"
}
resp_data = requests.post(url, data=json.dumps(body)).json()
print(resp_data['data']['translations'][0]['translatedText'])
