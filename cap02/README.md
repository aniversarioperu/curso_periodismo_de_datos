# Periodismo de datos. Capítulo 02

En el 
[capítulo anterior](http://aniversarioperu.utero.pe/2013/12/04/periodismo-de-datos-capitulo-01/)
demostré lo fácil que es descargar documentos públicos de los servidores del
Ministerio de Justicia. Solo se necesitan 5 líneas de código de programación
para descargar las 2,184 normas jurídicas (en formato PDF) emitidas durante el 2do gobierno
del APRA.

## En qué casos se puede descargar tantos documentos de manera tan fácil?

No toda la información que está en la Internet puede ser cosechada con 5 líneas
de código. Pero hay indicadores que te pueden dar una idea si esto es factible:

* Los documentos han sido colgados en el servidor de manera continua y
  constante.
* La cantidad de documentos es considerable (varios miles de archivos).

Si esas condiciones cumplen, es muy probable que los administradores del sitio
web estén usando algún software para asignar nombres a los archivos y mantener
los documentos de una forma ordenada.

Entonces ya tu sabes que **si se ha usado un software para colgar archivos, es
posible crear otro software para descargar esos archivos**.

## Cómo cosechar información

Cuando tienes todos los archivos descargados es necesario hacer la búsqueda de
información útil y relevante que sirvan para una historia o nota. Este proceso
es conocido como **análisis de datos** (["data analysis"](http://en.wikipedia.org/wiki/Data_analysis)).

Ya que leer 2,184 archivos PDF en búsqueda de información puede ser muy tediosa
para un humano, esto es muy fácil para una computadora. Pero es necesario que
toda la información esté como archivos de texto, en formato digital.

Un nerd puede convertir los 2,184 PDFs en texto usando una única línea de
de comandos en una consola Linux:

> ls | parallel -I {} pdftotext {}

Ahora ya la computadora puede leer todas las normas jurídicas en búsqueda de
datos de importancia. Si usas Linux o Mac ya tienes en tu computadora instalado
el comando **``grep``**. Este es un comando poderoso que puede leer miles 
de archivos de texto en cuestión de segundos.


http://www.twitter.com/jgodoym/status/390832218584543232

http://www.twitter.com/aniversarioperu/status/390832465826553856

http://www.twitter.com/jgodoym/status/390832556301901824
http://www.twitter.com/aniversarioperu/status/390833099913035777
http://www.twitter.com/aniversarioperu/status/390833292284821504
http://www.twitter.com/jgodoym/status/390833418155470848

https://twitter.com/larryportera/status/390838260211412993

http://www.larepublica.pe/18-10-2013/detienen-con-droga-a-otro-indultado-por-chinguel

