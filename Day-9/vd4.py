import requests,json,base64

img_url = 'https://i2-prod.liverpoolecho.co.uk/incoming/article17096840.ece/ALTERNATES/s1200d/0_whatsappweb1_censored.jpg'
img_data = requests.get(img_url).content
img_base64 = base64.b64encode(img_data).decode()

url = 'https://vision.googleapis.com/v1/images:annotate?key=AIzaSyBR8gU4Te36NCYlc2ZdynsOWQOS03lzWKc'

body = {
    "requests": [
    {
        "image": {"content" : img_base64},
        "features": [{"type": "DOCUMENT_TEXT_DETECTION"}]
        }
    ]
}
resp_data = requests.post(url, data=json.dumps(body)).json()
print(resp_data['responses'][0]['fullTextAnnotation']['text'])