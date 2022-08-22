import bs4
import requests


resultado = requests.get('https://www.escueladirecta.com/courses')


navegable = bs4.BeautifulSoup(resultado.text,'lxml')

imgs = navegable.select('.course-box-image')[0]['src']

imagen_extraida = requests.get(imgs)


f = open("img_test.jpg", 'wb')
f.write(imagen_extraida.content)
f.close()
