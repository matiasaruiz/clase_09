import bs4
import requests


# Goal: obtener todos los tittulos de los libros que tiene 4 o mas estrllas

# cada libro tiene una class=star-rating Three y necesito class=star-rating Four and class=star-rating Five
 

 # Url independiente del numero de pagina

url_root = 'http://books.toscrape.com/catalogue/page-{}.html'

# Lista en la cual se van a guardar los aciertos de 4 o 5 estrllas
aciertos = []

# Recorro todas las paginas
for pagina in range(0,51):

    # Creo los navegales por pagina
    url_pagina = url_root.format(pagina)
    resultado = requests.get(url_pagina)
    navegable = bs4.BeautifulSoup(resultado.text,'lxml')

    # Extraigo los datos de los libros
    libros = navegable.select('.product_pod')

    # Busco aciertos de libros y los guaro en la lista
    for libro in libros:

        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
        
            titulo_acierto = libro.select('a')[1]['title']
            aciertos.append(titulo_acierto)

# Muestro los aciertos
for libro in aciertos:
    print(libro)
