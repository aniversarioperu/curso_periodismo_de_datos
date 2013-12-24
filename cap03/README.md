# Periodismo de datos. Capítulo 03

En el 
[capítulo anterior](http://aniversarioperu.utero.pe/2013/12/18/periodismo-de-datos-capitulo-02/)
te mostré lo fácil que es 
ubircar al indultado EDWIN VALENZUELA entre los 2,184 normas jurídicas emitidas
por el Ministerio de Justicia durante el segundo gobierno aprista.

Esto se podía hacer fácilmente convirtiendo los PDF a archivos TXT (*plain
text*) ya que las normas jurídicas fueron publicadas
como archivos PDF conteniendo texto, no imágenes.

Mira tú:


>>>Imagen PDF


Pero qué pasa si quieres analizar los PDFs emitidos por el venerable Congreso
de la República? Sus PDFs son horribles, mira:

>>>Imagen PDF congreso

Estos PDFs son el resultado de:

* Imprimir el texto en papel
* Escanear las hojas impresas
* Armar el PDF y publicar en la página web

Entonces estos PDFs están compuestos de imágenes. No se pueden convertir a
archivos TXT usando el método aplicado con los PDFs del Ministerio de Justicia.

Y ahora? cómo hacer el análisis de datos usando estos PDFs compuestos por imágenes? es el fin?
no somos nada?

# OCR al rescate
Nos puede ayudar una técnica llamada *Optical character recognition* que te convierte imágenes a texto.

Según Wikipedia el **[Reconocimiento óptico de caracteres](http://es.wikipedia.org/wiki/Reconocimiento_%C3%B3ptico_de_caracteres)**:

> es un proceso dirigido a la digitalización de textos, los cuales identifican automáticamente a partir de una imagen símbolos o caracteres que pertenecen a un determinado alfabeto, para luego almacenarlos en forma de datos



