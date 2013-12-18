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

## Aplicación práctica

Hace unos meses el tuitero [@jgodoym](https://twitter.com/jgodoym) alertó 
de una [noticia en Caretas](http://bit.ly/JBT349) donde un #narcoindultado fue capturado con varias
toneladas de droga.

https://twitter.com/jgodoym/status/390832218584543232

La [noticia de Caretas dice](http://bit.ly/JBT349):

> En 2009, sin embargo, Facundo Chinguel le redujo la pena a la mitad y el colombiano obtuvo su libertad en mayo del 2010.

Facundo Chinguel ya estaba preso, pero algunos sospechan que la
responsabilidad puede ser imputada a servidores públicos de mayor jerarquía.

Teniendo el nombre del indultado se puede buscar en cuál de las normas
jurídicas aparece mencionado.

https://twitter.com/AniversarioPeru/status/390832465826553856

https://twitter.com/jgodoym/status/390832556301901824

Usando el poderoso comando **``grep``** podemos buscar a **Edwin Valenzuela**
en las 2,184 normas jurídicas en cuestión de 35 segundos.

> grep -i Valenzuela *.txt  | grep -i Edwin

Estos son los resultados:

> 04-02-11.txt:22. VALENZUELA PINARES, EDWIN, conmutarle de 05 años a 04 años de pena privativa
> 09-08-09.txt:MELGAREJO VALENZUELA, EDWIN RICARDO
> 19-08-06.txt:1.- EDWIN TORRES VALENZUELA
> 24-11-09.txt:1. VALENZUELA MENESES, EDWIN JAVIER; conmutarle de 12 años a 06 años de pena
> real    0m35.020s


https://twitter.com/AniversarioPeru/status/390833099913035777

https://twitter.com/AniversarioPeru/status/390833292284821504

https://twitter.com/jgodoym/status/390833418155470848

Entonces, producto del análisis de datos, ya sabemos que el nombre completo del
narcoindultado es **VALENZUELA MENESES, EDWIN JAVIER**. El texto
**``24-11-09.txt``** nos indica que la resolución salió publicada el 24 de
Noviembre del 2009. Y teniendo la fecha podemos reconstruir la dirección
electrónica donde se encuentra la dichosa resolución:

> http://spij.minjus.gob.pe/Normas/textos/241109T.pdf

Si revisamos el documento vemos que el idulto fue firmado por el ex-minitro
Aurelio Pastor (páginas 32--33).

Este intercambio de tuits fue captado por
[@larryportera](https://twitter.com/larryportera):

https://twitter.com/larryportera/status/390838260211412993

Y al día siguiente salió [una noticia mucho más completa](http://www.larepublica.pe/18-10-2013/detienen-con-droga-a-otro-indultado-por-chinguel) 
en [@larepublica_pe](https://twitter.com/larepublica_pe), incluyendo datos que
no aparecieron en la nota de Caretas:

> Según resolución suprema 268-2009, del 23 de noviembre del 2009, el
  presidente Alan García y el ministro de Justicia, Aurelio Pastor, redujeron
  la condena de 12 años de prisión impuesta al colombiano, a solo seis años de
  cárcel.

La resolución se publicó el 24 de Noviembre pero se firmó un día antes.

Como ves, si tienes a un nerd a la mano tienes la posibilidad de enriquecer tus
nota periodísticas con datos adicionales. 

**Ojo, que no fue necesario meter toda la información a una base de datos**. Se
puede extraer información útil de una lista de archivos contenidos en una
carpeta. Las bases de datos pueden ser muy útiles para el periodismo de datos,
pero se pueden hacer cosas interesantes usando el simple comando **``grep``**. 

Dejaré la discusión sobre base de datos para un post futuro.
