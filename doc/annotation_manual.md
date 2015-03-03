# Manual para la anotación de atenuantes retóricos en español (v.1.0)

Aquí se presenta una descripción de la atenuación retórica, seguida por el
formato a seguir en su anotación textual. 

## 1 ¿Qué es un atenuante retórico?

Un atenuante retórico es “cualquier recurso lingüístico por medio del cual 
alguien evita ser comprometido por decir algo que resulte ser falso o por hacer 
una petición que pueda ser inaceptable, entre otras cosas. En vez de decir 
'Este argumento es convincente', uno podría usar un atenuante retórico y 
decir 'A mí me parece que este argumento es convincente'; en vez de 
simplemente dar la orden 'Llévelo a la cocina', uno podría usar una pregunta 
como atenuante retórico y decir '¿Podría tal vez llevarlo a la cocina?’". 
(Matthews, Peter. The Concise Oxford Dictionary of Linguistics. 2007)

Dicho de otra manera, es una palabra o frase que disminuye el compromiso que un 
autor tiene con la veracidad de sus afirmaciones. Se pueden usar para:
Mitigar o modular las afirmaciones de manera que la audiencia sienta que es 
capaz de juzgar por sí misma, que el autor queda pendiente de su aceptación.
Proteger al autor frente a las posibles reacciones que pueda provocar su 
proposición o reflejar su modestia y su deferencia hacia la audiencia que va 
dirigido el mensaje.
Expresar cautela, modestia o cortesía por parte del autor.

Como ejemplo, podemos considerar la siguiente oración:

	Yo creo que deberías de tomar esta ruta, pero bueno, es sólo una idea.

Las frases "yo creo" y "es sólo una idea" sugieren que el autor no quiere 
imponer su opinión sobre la persona a la que se dirige. Por lo tanto, se les 
considera como atenuantes retóricos.

### 1.1 Qué anotar

Sólo las oraciones con alguna instancia de lenguaje especulativo deberán ser 
anotadas. Si una oración no incluye algún elemento especulativo o cualquier 
elemento que sugiera incertidumbre (i.e., la oración expresa sólo un hecho), 
la oración puede ser ignorada.

Sin embargo, no todo el lenguaje especulativo se considera atenuación 
retórica. Oraciones hipotéticas como

	Si llueve, no iré al juego.

contienen instancias de lenguaje especulativo (‘si’ en este caso), pero no 
son instancias de atenuación retórica.

En general, cuando no es claro si una palabra o frase es un atenuante 
retórico, las siguientes preguntas pueden ser útiles:

Hay alguna falta de información o incertidumbre? 
Se está tratando de disminuir el impacto de la oración?

Si la respuesta a cualquiera de estas preguntas es sí, es posible que la
oración en cuestión contenga un atenuante retórico.

Nuestra labor es anotar las palabras o frases que indican la presencia de 
atenuación retórica.

#### 1.1.1 Indicadores de atenuación retórica

Un indicador de atenuación retórica (hedge cue en inglés) puede ser 
cualquier palabra o combinación de palabras que indican incertidumbre, una 
falta de precisión o un intento de amortiguar o reducir el impacto de un 
enunciado.

- [Supongo] que Carlos tiene la razón.
- María estaba [probablemente] en estado de ebriedad.
- Yo [creo] que es un tema de gran importancia.
- Esto [puede] ser un efecto del bioterrorismo en los Estados Unidos.
- Es [ampliamente] reconocido que esta universidad tiene una buena reputación e 
historial.

En cada uno de estos ejemplos, la palabra en corchetes es un indicador de 
atenuación retórica. A continuación se presenta una descripción más 
completa de estos indicadores.

#### 1.1.2 Tipos de atenuantes retóricos

De acuerdo a Prince (1980), los atenuantes retóricos se pueden clasificar como 
relacionales o proposicionales.

##### Relacionales

Relacionan al hablador con el contenido proposicional

Algunos ejemplos:

###### Adjetivos-adverbios

- [Quizá] sea mejor que hablemos con tu familia.
- [Quién sabe] si esto funcione.

###### Auxiliares

- [Deberías] considerar otra solución.
- Esta ruta [podría] ser peligrosa.

###### Verbos

- Yo [diría] que hay que esperar.
- [Siento] que podríamos trabajar más a fondo.

##### Proposicionales

Introducen incertidumbre en el contenido proposicional

Algunos ejemplos:

###### Grado

- [Casi] no hay librerías en el pueblo.
- Esto debería de ser [relativamente] sencillo.

###### Frecuencia

- [Generalmente] no salgo los jueves por la tarde.
- [Raramente ceno en ese restaurante.

###### Falta de especificidad

- Tuvo que haber escapado de [alguna] manera.
- [Hay quien] dice que murió ahogado.

###### Cuantificadores

- Me dijeron [más o menos] qué tengo que hacer.
- Sería [poco prudente] hablarle de esa manera.

### 1.2 Cómo anotar los atenuantes retóricos

La anotación sigue un formato en csv delimitado por tabuladores con las siguientes
columnas:

- segmento (oración anotada)
- proposición (posible atenuante retórico)
- clasificación (relacional, proposicional o ninguno)

Nota: En esta clasificación, se usan las abreviaciones HREL (relacional), HPROP
(proposicional) y NH (ninguno).

Consideremos este ejemplo:

1. Yo creo que ésta es una situación delicada.

Debido a que hay atenuación retórica en esta oración, la anotamos de la siguiente manera:

        Yo creo que ésta es una situación delicada.     creo    HREL

donde "creo" es un atenuante retórico de tipo relacional.
