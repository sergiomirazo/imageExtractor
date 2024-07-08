# imageExtractor
A python script for web scrapping. This script extracts all the figures in a web page

**Description:**
Un cliente me pidió remodelar el sitio web de su empresa. La empresa se dedica a vender material de plomería y tienen en su sitio un amplio inventario, de más de 100 objetos.
El cliente no me facilitó la información en formato JSON para desplegarlo en el nuevo sitio debido a que el cliente no posee conocimientos de programación.
Así que hice este pequeño script para extraer todas las imágenes de cada figure, junto con los figcaptions y h3 de cada artículo.
Luego, toda esta información se guarda en un JSON para implementarlo en el FrontEnd para el nuevo sitio web

- Por respeto a la privacidad de mi cliente quité la URL ,la cual debes cambiar con la que deseas extraer
- Es importante que el sitio que deseas extraer tenga etiquetas 'figure'
- La variable 'headers' es necesaria para evitar que nuestro bot sea detectado por algunos sitios, en especial si son de wordpress

Espero que este script sea de gran ayuda a la comunidad
