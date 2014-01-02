# Periodismo de datos. Capítulo 03

En el 
[capítulo anterior](http://aniversarioperu.utero.pe/2013/12/18/periodismo-de-datos-capitulo-02/)
te mostré lo fácil que es 
ubircar al indultado EDWIN VALENZUELA entre las 2,184 normas jurídicas emitidas
por el Ministerio de Justicia durante el segundo gobierno aprista.

Esto se podía hacer fácilmente convirtiendo los PDF a archivos TXT (*plain
text*) ya que las normas jurídicas fueron publicadas
como archivos PDF conteniendo texto, no imágenes.

Mira tú:


![Imagen PDF del Ministerio de Justicia](pdf_minjus.png)


Pero qué pasa si quieres analizar los PDFs emitidos por el venerable Congreso
de la República? Sus PDFs son horribles, mira:

![Imagen PDF congreso](pdf_congreso.png)

El Congreso tiene una manera "creativa" de crear sus PDFs:

* Imprimen el texto en papel
* Escanean las hojas impresas
* Juntan las imágenes en un PDF y publican en la página web

Entonces estos PDFs están compuestos de imágenes. No se pueden convertir a
archivos TXT usando el método aplicado con los PDFs del Ministerio de Justicia.

Y ahora? cómo hacer el análisis de datos usando estos PDFs compuestos por imágenes? es el fin?
no somos nada?

# OCR al rescate
Nos puede servir una técnica llamada *Optical character recognition* que te convierte imágenes a texto.

Según Wikipedia el **[Reconocimiento óptico de caracteres](http://es.wikipedia.org/wiki/Reconocimiento_%C3%B3ptico_de_caracteres)**:

> ...es un proceso dirigido a la digitalización de textos, los cuales
identifican automáticamente a partir de una imagen símbolos o caracteres que
pertenecen a un determinado alfabeto, para luego almacenarlos en forma de datos

Existe un [software *open source* llamado
**tesseract**](http://en.wikipedia.org/wiki/Tesseract_(software)) que se
encarga de realizar OCR sobre archivos de imágenes. Tú le das imágenes y te
devuelve texto. **tesseract** es capaz de reconocer texto escrito en Español,
Inglés, Sueco, Swahili, Japonés, Hebreo, *Middle English*, etc, etc (66 idiomas en
total).

Algunos están pidiendo que también pueda reconocer Klingon y *Elvish* (#okno, #whynot).

Si tenemos descargados miles de PDFs compuestos por imágenes, podemos
convertirlos todos de un porrazo usando un par de comandos en una consola de
Linux. Primero se extraen las imágenes del PDF y en el segundo paso se usa
**tesseract** para hacer la conversión (es necesario especificar el lenguaje
en el que está escrito el texto).

# Prodecimiento para hacer OCR
**Paso 1.** Extraer las imágenes contenidas en miles de PDFs:

> ls *pdf | parallel -I {} pdfimages -j {} {.}

**Paso 2.** Convertir miles de imágenes a texto usando OCR:

> ls | grep -v pdf | parallel -I {} tesseract {} {.} -l spa

Luego de un rato tendremos nuestro folder lleno de archivos de texto. Y este es
el texto extraído de uno de los PDFs (imagen de más arriba).

<pre>
CONGRESO n: u nwuauca

Japón, seguido por los Estados Unidos, España y otros países“; estos se resumen en
la siguiente tabla:

PAIS Año/Legislación Lugares No. mínimo Financiamiento
DEA
Japón 2004 Según voluntad pública y/o privada, Público/privado
escuelas, instalaciones medicas,
deportivas. culturales y medios de
transporte público.
Estados Unidos 2005, Ley No.20 Edificios públicos, parques, guarderías, 1/250 Sin información
centros de tercera edad, escenarios
deportivos y clubes de salud.
Terminales de Ferry, 1 / 100o
España 2009, Real Decreto Voluntad de entidades públicas o privadas Sin información
365/2009 que deberán notiﬁcar a la autoridad
sanitaria quien dispone la instalación del
DEA.
Colombia 2008. Proyecto Ley Terminales de transportes. 1/500 Institución que posea
No. 149 DEA
Centros comerciales, 1/1000m?
Estadios, 1/1000
Centros de eventos. 1/100
Instituciones educativas. 1/500
Edificios > 100 personas 1/100
Tren, avión, barco 1/100
Uruguay 2008, Ley No. 18360 Todo lugar que disponga el Ministerio de Institución que posea
Salud Pública. DEA

46 Patricio Meller Bock Luis Javier Venegas Nuñez. Expansión del uso de desﬁbriladores externos automáticos en Chile,
mediante la creación de la empresa CARDlOVIDA S.A. Santiago de Chile Abril 2012.

Jr. Hua/Inga N“ 358 — 360/ Edificio Fernanda Be/aúnde Terry / Oficina 203
Teléfono 311-7480 f 3
</pre>

# Conclusión
Te darás cuenta que no se ha podido reconocer el 100% del texto. El porcentaje
de eficacia depende de la calidad de la imagen escaneada (alta calidad, que la
imagen no esté chueca, que la hoja no esté arrugada, etc.)

Ahora sí puedes hacer un análisis de datos buscando información interesante en
tus archivos y puedes hacerlo eficientemente usando el comando **grep**
reseñado en el [Capítulo 02 de este curso uterino](http://aniversarioperu.utero.pe/2013/12/18/periodismo-de-datos-capitulo-02/).
