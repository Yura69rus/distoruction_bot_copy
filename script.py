from bs4 import BeautifulSoup
import requests


def distortImage(img_before, img_after):
    files = {'uploadfile': open(f'{img_before}.jpg', 'rb')}
    data = {'ef-set': 7, 'jpeg-quality': 95}
    r = requests.post('https://www.imgonline.com.ua/picture-distortion-result.php', files=files, data=data)

    html = BeautifulSoup(r.content, 'html.parser')
    get_img = html.find_all('a')

    img = requests.get('https://www.imgonline.com.ua/' + get_img[8]['href'])
    with open(f'{img_after}.jpg', 'wb') as img_file:
        img_file.write(img.content)


def downloadImage(url_img, path_to_image):
    img = requests.get(url_img)
    with open(f'{path_to_image}.jpg', 'wb') as img_file:
        img_file.write(img.content)


