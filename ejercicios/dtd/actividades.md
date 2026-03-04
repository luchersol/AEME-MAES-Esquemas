<style>
pre {
  border: 2px solid #333; /* borde */
  padding: 10px;           /* espacio interno */
  border-radius: 5px;      /* esquinas redondeadas */
  background-color: #f5f5f5; /* fondo gris claro */
  overflow-x: auto;        /* scroll horizontal si es necesario */
}
code {
  font-family: Consolas, monospace; /* tipografía monoespaciada */
}
h2::before {
  counter-increment: actividad;
  content: "Actividad " counter(actividad);
}
body {
  counter-reset: actividad;
}
</style>

# Ejercicios DTD

Bienvenido al boletín de ejercicios sobre DTD y validación XML. Los siguientes ejercicios están organizados por contenidos (declaración, elementos y cardinalidad, atributos, entidades y validación).

##

Crea un DTD como declaración interna para el siguiente XML. Considera que todos los elementos hijos solo aparecen una vez y son obligatorios:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<nota>
    <para>José</para>
    <de>Marcos</de>
    <cuerpo>Buenos días</cuerpo>
</nota>
```

##
Convierte la definición de la actividad anterior en un DTD externo y actualiza el XML para usar `<!DOCTYPE nota SYSTEM ...>`. Documenta las ventajas de cada enfoque.

##
Corrige el siguiente DTD:

```xml
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE persona [     
    <!ELEMENT nombre (#PCDATA)> 
]> 
<persona>     
    <nombre>25</nombre> 
</persona> 
```

##
Corrige el siguiente DTD:

Nota: Debe existir mínimo un telefono en el listado.

```xml
<?xml version="1.0" encoding="UTF-8"?> 
<!DOCTYPE telefonos [     
    <!ELEMENT telefonos (telefonos)>
    <!ELEMENT telefono (#PCDATA)> 
]> 
<telefonos>     
    <telefono>678-124-612</telefono> 
    <telefono>678-124-613</telefono> 
</telefonos> 
```

##
Escriba el DTD que defina el siguiente XML:

```xml
<?xml version="1.0" encoding="UTF-8"?> 
<casa>
</casa> 
```

##
Modifica el siguiente código para que el elemento `parque` cumpla los siguientes requisitos: <br>

- El elemento `arbol` debe de aparecer mínimo una vez, pero puede aparecer varias veces <br>
- El elemento `banco` puedo aparecer varias veces o no aparecer<br>
- El elemento `fuente` debe existir.<br>
- El elemento `mascota` puede aparecer o no.<br>

```xml
<!ELEMENT parque (arbol+, banco*, fuente, mascota?)>

<!ELEMENT arbol (#PCDATA)>
<!ELEMENT banco (#PCDATA)>
<!ELEMENT fuente (#PCDATA)>
<!ELEMENT mascota (#PCDATA)>
```

##
Crea un elemento `contacto` que pueda contener exactamente uno de los siguientes elementos hijos: `email` o `telefono`. Cada uno de estos elementos debe contener únicamente texto.

##
Utilizando el XML de la actividad anterior, crea un `contacto` con los elementos `email` y `telefono` a la vez. Explica el mensaje de error que se muestra.

##
Crea un DTD con varios elementos en el que se utilicen los caracteres `+`, `*`, `?`, `EMPTY` y `ANY`. Luego, explica cómo afecta cada uno de estos elementos.

##
Describe qué hace cada `ATTLIST` en el siguiente dtd:

```xml
<!ELEMENT cuadrado EMPTY>

<!ATTLIST cuadrado color #IMPLIED >
<!ATTLIST cuadrado longitudLado #REQUIRED >
<!ATTLIST cuadrado numLados #FIXED 4>
```

A continuación, dame un XML de ejemplo válido y dos XML de ejemplo inválidos, explicando en estos últimos por qué son inválidos.

##
Escribe el DTD que defina el siguiente XML

```xml
<?xml version="1.0" encoding="UTF-8"?> 
<persona dni="12345678M" /> 
```

##
Crea un elemento `productos` (mínimo 4 productos). En el mismo archivo de forma comentada, ponme también dos `producto` invalidos.

DTD de referencia:

```xml
<!ELEMENT productos (producto+)>
<!ELEMENT producto EMPTY>
<!ATTLIST producto nombre CDATA #REQUIRED>
<!ATTLIST producto categoria CDATA #IMPLIED>
<!ATTLIST producto tienda CDATA #FIXED "Mercadona">
```

##
Sustituye el contenido del elemento `libro` para que en su lugar utilice la entidad `nombre`.

```xml
<!DOCTYPE libro [
    <!ELEMENT autor (#PCDATA)>
    
    <!ENTITY nombre "Miguel de Cervantes">
]>
<libro>Miguel de Cervantes</libro>
```

##
En el siguiente DTD, incluye en la declaración las entidades correspondientes de forma de que:
- El título sea "Aprendiendo Entidades".
- El autor sea "Antonio Galán".
- La editorial sea "Santillana".

```xml
<!DOCTYPE libro [
    <!ELEMENT libro (titulo, autor, editorial)>
    <!ELEMENT titulo (#PCDATA)>
    <!ELEMENT autor (#PCDATA)>
    <!ELEMENT editorial (#PCDATA)
]>
<libro>
    <titulo>&titulo;</titulo>
    <autor>&autor;</autor>
    <editorial>&editorial;</editorial>
</libro>
```

##
Crea el DTD del elemento `biblioteca` que cumpla:
- `biblioteca` con 1+ `libro` y 0+ `revista`.
- `libro` con `titulo`, `autor`, `isbn` y 0+ `categoria`. Además, contiene el atributo obligatorio `id`.
- `revista` con `titulo` y `numero`.
- `contacto` opcional con 1+ `email` o 1+ `telefono` (no ambos).

##
Elabora 5 errores diferentes reales (por ejemplo: atributo obligatorio ausente, valor distinto a `#FIXED`, elemento repetido, entidad no definida, DTD externa no encontrada). Para cada error incluye el XML inválido y la versión corregida.

---

Entrega y criterios
- Entrega: un ZIP con las respuestas de cada ejercicio.
- Nombrado: cada archivo debe comenzar con el número del ejercicio en dos dígitos, seguido de un guion bajo y un nombre si se quiere ser más descriptivo.
    Ej: ejercicio 1 -> "01_Nombre.dtd", ejercicio 12 -> "12_Nombre.dtd"



