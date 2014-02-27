# Periodismo de Datos. Capítulo 10

## Fiscalizando los viajes de los congresistas vía twitter
En el [capítulo anterior de este curso](http://aniversarioperu.utero.pe/2014/02/17/periodismo-de-datos-capitulo-09/)
habíamos explorado la posibilidad de fiscalizar los viajes al exterior de los
congresistas de la república.

La mayoría de congresistas usa fondos del estado para financiar sus viajes al
exterior cuando van en misión oficial. Por lo tanto es nuestro derecho y deber
enterarnos si el dinero de nuestros impuestos de gasta (o invierte) de la mejor
manera.

Para este fin había descargado los tuits georeferenciados más recientes de
nuestros congresistas y los había ploteado sobre un Google Map 
([ver el resultado aquí](http://aniversarioperu.me/utero/todos_congresistas.html)).
El objetivo era explorar las posibilidades de averiguar si los congresistas
habían viajado dentro del permiso otorgado en base a los tuits georeferenciados
que han podido emitir desde el extranjero.

![](img1.png)

# Solución a la tarea
Gracias a los amixers que enviaron sus respuestas. Todos estuvieron acertados.

## Estas fueron las preguntas:
**Pregunta 1:** Ubicar aquel acuerdo de mesa directiva donde la congresista (y
flamante ministra) Carmen Omonte haya recibido permiso para viajar a España.
Corroborar si ella se quedó en España durante el periodo autorizado. Averiguar
si los pasajes y viáticos usados por la congresista Carmen Omonte salieron de
su bolsillo propio o salió de tus impuestos.

**Rpta:** Tal como lo reportaron ustedes, la autorización para el viaje oficial a
España es el **acuerdo No 215-2012-2013/MESA-CR**.

> 1. Autorizar a la delegación conformada por los Congresistas José León Luna Gálvez,
    Tercer Vicepresidente del Congreso, quien la Presidirá, Luis Fernando Galarreta
    Velarde, Presidente de la Liga Parlamentaria Perú-España, Santiago Gastañadui
    Ramírez, Luz Filomena Salgado Rubianes, **María del Carmen Omonte Durand**, Martín
    Belaunde Moreyra, Luis Carlos Antonio Iberico Núñez y Elías Nicolás Rodríguez
    Zavaleta, para realizar una visita a **Madrid, España, del 15 al 19 de
    abril de 2013**, con la
    finalidad de cumplir una agenda coordinada con el Ministerio de Relaciones Exteriores.
> 2. Disponer que la Dirección General de Administración realice las acciones
    administrativas necesarias a fin de otorgar los pasajes y los viáticos correspondientes,
    debiendo considerar un día antes y un día después del evento, según itinerario y previo
    informe de disponibilidad presupuestal.

Esto coincide con los tuits que la congresista emitió desde Madrid. Todo bien:

[gist id=9177326]

El acuerdo de mesa también menciona que el congreso pagó los gastos de la
comitiva que integró la congresista Omonte. La única excepción fue el
congresista José Luna que pagó el viaje con su plata

> 3. Exceptuar de la adquisición de pasajes y otorgamiento de viáticos al Congresista José
Luna Gálvez, Tercer Vicepresidente del Congreso, según lo dispuesto en el
Memorándum 276-2012-2013/TVP-CR, quien asumirá los gastos que ocasione dicho
viaje.

**Pregunta 2:** Averiguar cuáles eran las fechas que comprendían la
autorización de viaje de la congresista Carmen Omonte a Santiago de Chile.

**Rpta:** Aquí también han acertado los amixers en que no se puede encontrar la
autorización para el viaje de la congresista Omonte al
4to Encuentro Peruano Chileno: Pensando en el Futuro. Organizado por Fundacion Chile 21 
([ver tuit](https://twitter.com/carmenomonte/status/323253641911865344)).
Tampoco es posible encontrar autorización para su viaje a Santiago de Chile (con viaje
a la Isla de Pascua) a fines de Marzo.
En este caso las posibilidades son varias:

* El viaje a la Isla de Pascua fue realizado durante sus vacaciones. Pero se
  supone que las vacaciones de los congresistas son durante Enero-Febrero. Y ya
  sabemos que en el 2013 la 
  [legislatura comenzó el 1ero de Marzo](http://bit.ly/1hl7nKK), y la ahora
  ministra estuvo en la Isla de Pascua el 29 de
  Marzo [(ver tuit)](https://twitter.com/carmenomonte/status/317731002325811201).
* Talvez tuvo licencia para ese viaje. Mi objetivo para este curso llega hasta
  aquí. Ya los periodistas profesionales juzgarán si esta situación merece
  tratamiento periodístico, merece mayor investigación, o es algo sin
  importancia. 

Tal como dije en el [primer
capítulo](http://aniversarioperu.utero.pe/2013/12/04/periodismo-de-datos-capitulo-01/)
de este curso:

> [Las] tareas repetitivas pueden ser automatizadas y ejecutadas por los hackers
y sus computadoras. La labor del periodista es otra, es analizar qué datos son
importantes de ser cosechados, qué otro tipo de datos deben ser asociados con
el fin de obtener una historia. La labor analítica y de pensamiento crítico
debe ser realizada por el periodista. Para esto es de vital importancia la
experiencia e intuición de periodista.

## Bonus track
El periodista Martín Hidalgo estuvo [alertando por tuiter](https://twitter.com/martinhidalgo/status/428598285171843072) de los jugosos
viáticos que reciben los congresistas cuando viajan al extranjero.
Por ejemplo para un viaje a Francia de 8 días llegan a recibir hasta 12,600
soles. Esta es la cantidad aproximada que recibe como **sueldo para un mes** un
profesional con posgrado en Europa.

![](viaticos.png)

Me da curiosidad saber en qué gastan tanto dinero durante sus viajes. Será
que los congresistas se hospedan en un hotel Sheraton? o en otro de 5
estrellas?

En el caso de la ministra Carmen Omonte podemos usar los tuits que envió
durante su estadía en Madrid, España para averiguar en qué hotel se hospedó.


## Tarea para la casa
Si usas una combinación del Google Map donde están los tuits de los congresistas
([aquí](http://aniversarioperu.me/utero/todos_congresistas.html)), con Google
Stree View y <http://www.tripadvisor.com/>, podrás averiguar la dirección del
hotel, ver la fachada, el nombre, y si el hotel es pitucazo, modesto,
o es hotel de mala muerte.


