# Ejercicios DTD

Bienvenido al boletín de ejercicios sobre DTD y validación XML. Los siguientes ejercicios están organizados por contenidos (declaración, elementos y cardinalidad, atributos, entidades y validación).

## Actividad 1

Explica cada línea de la sección `<!DOCTYPE ... [ ... ]>` del siguiente xml. Además, añade un elemento `fecha` (#PCDATA) después de `cuerpo`.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE nota [
    <!ELEMENT nota (para, de, cuerpo)>
    <!ELEMENT para (#PCDATA)>
    <!ELEMENT de (#PCDATA)>
    <!ELEMENT cuerpo (#PCDATA)>]
>
<nota>
        <para>José</para>
        <de>Marcos</de>
        <cuerpo>Buenos días</cuerpo>
</nota>
```

## Actividad 2
Convierte la definición de la [Actividad 1](#actividad-1) en `mi_nota.dtd` y actualiza el XML para usar `<!DOCTYPE nota SYSTEM "mi_nota.dtd">`. Documenta las ventajas de cada enfoque.


## Actividad 3
Escribe en 4-6 líneas qué hacen `+`, `*`, `?`, `EMPTY` y `ANY` en la declaración de un elemento.

## Actividad 4
Modifica el siguiente código para que el elemento `parque` cumpla los siguientes requisitos:
- El elemento `arbol` debe de aparecer mínimo una vez, pero puede aparecer varias veces
- El elemento `banco` puedo aparecer varias veces o no aparecer
- El elemento `fuente` debe existir.
- El elemento `mascota` puede aparecer o no.

```xml
<!ELEMENT parque (arbol, banco, fuente, mascota)>

<!ELEMENT arbol (#PCDATA)>
<!ELEMENT banco (#PCDATA)>
<!ELEMENT fuente (#PCDATA)>
<!ELEMENT mascota (#PCDATA)>
```

## Actividad 5
Define un elemento XML llamado `contacto` que pueda contener exactamente uno de los siguientes elementos hijos: `email` o `telefono`. Cada uno de estos elementos debe contener únicamente texto.

## Actividad 6
Utilizando el xml de la [Actividad 5](#actividad-5), crea un `contacto` inválido con ambos hijos y explica el mensaje de error que esperarías del validador.

## Actividad 7
Describe en una frase qué hace cada `ATTLIST` en el siguiente ejemplo:

```xml


```

## Actividad 8
Crea `productos_validos.xml` (mínimo 4 productos) y dos archivos inválidos: `productos_invalidos_1.xml` (falta `nombre`) y `productos_invalidos_2.xml` (`tienda` distinto de `Mercadona`).

DTD de referencia:

```xml
<!ELEMENT productos (producto+)>
<!ELEMENT producto EMPTY>
<!ATTLIST producto nombre CDATA #REQUIRED>
<!ATTLIST producto categoria CDATA #IMPLIED>
<!ATTLIST producto tienda CDATA #FIXED "Mercadona">
```

Ejemplo válido (fragmento):

```xml
<productos>
    <producto nombre="Leche" categoria="Lácteos" />
    <producto nombre="Pan" />
    <producto nombre="Huevos" tienda="Mercadona" />
</productos>
```

## Actividad 9
A partir de `ejemplos/dtd/05_entidades.xml`, añade `pais_editorial` y `anio_fundacion` y úsalo en `editorial`.

Ejemplo:

```xml
<!DOCTYPE libro [
    <!ENTITY editorial_principal "Editorial Universitaria">
    <!ENTITY pais_editorial "España">
    <!ENTITY anio_fundacion "1920">
]>
<libro>
    <titulo>Aprendiendo XML</titulo>
    <autor>Juan</autor>
    <editorial>&editorial_principal; — &pais_editorial; (&anio_fundacion;)</editorial>
</libro>
```

## Actividad 10
Crea `biblioteca.dtd` que cumpla:
- `biblioteca` con 1+ `libro` y 0+ `revista`.
- `libro` con `titulo`, `autor`, `isbn` y 0+ `categoria`.
- `revista` con `titulo` y `numero`.
- `contacto` opcional con `email` o `telefono` (no ambos).

Ejemplo mínimo de XML referenciando la DTD:

```xml
<?xml version="1.0"?>
<!DOCTYPE biblioteca SYSTEM "biblioteca.dtd">
<biblioteca>
    <libro>
        <titulo>Ejemplo</titulo>
        <autor>Autor</autor>
        <isbn>978-1234567890</isbn>
    </libro>
</biblioteca>
```

## Actividad 11
Elabora 5 errores reales (por ejemplo: atributo obligatorio ausente, valor distinto a `#FIXED`, elemento repetido, entidad no definida, DTD externa no encontrada). Para cada error incluye el XML inválido y la versión corregida.

---

Entrega y criterios
- Entrega: un ZIP con los XML y DTD creados y un documento con respuestas breves.
- Criterios: corrección de DTD/XML, evidencia de validación (indica la herramienta usada) y claridad en las explicaciones.



