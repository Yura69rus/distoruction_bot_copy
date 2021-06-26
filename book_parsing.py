import requests
from bs4 import BeautifulSoup

files = {'uploadfile': open('logo.jpg', 'rb')}
data = {'ef-set': 7, 'jpeg-quality': 95}
r = requests.post('https://www.imgonline.com.ua/picture-distortion-result.php', files=files, data=data)

html = BeautifulSoup(r.content, 'html.parser')
get_img = html.find_all('a')

img = requests.get('https://www.imgonline.com.ua/' + get_img[8]['href'])
with open('result.jpg', 'wb') as img_file:
    img_file.write(img.content)

