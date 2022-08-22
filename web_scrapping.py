import bs4
import requests


resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html')


navegable = bs4.BeautifulSoup(resultado.text,'lxml')

sidebar = navegable.select('.sidebar-container div')

for div in sidebar:
    print(div.getText())