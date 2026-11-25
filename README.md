# Banco de Planeaciones

App para guardar planeaciones exitosas y llenar con un clic el formato de planeación del
Jardín de Niños “Barbarita Barrera de González” (ciclo 2026-2027).

- **Formato**: primero elige el **grado** (1°, 2° o 3°); luego toca el *Nombre del proyecto* y elige una
  planeación de ese grado; todo el formato se llena solo. El espacio *Programas externos (Actividades de la
  comunidad)* no viene del banco: la maestra lo escribe en el formato cada vez, porque cambia según las fechas.
  “Descargar Word” genera el .docx con el mismo encabezado, logos y colores del formato oficial.
  En el sitio también funciona “Imprimir”.
- **Editar**: captura o modifica una planeación (cada planeación lleva su grado). Los contenidos y PDA se eligen del Programa Sintético
  de la Fase 2 (1°, 2° y 3°) con las claves del cuadernillo; los momentos cambian según la modalidad.
- **Banco**: busca, filtra por campo formativo o eje, duplica, elimina, descarga o carga el banco.
- **Revisión de la planeación**: al subir un Word (o con el botón *Revisar planeación* del editor) la app revisa la
  estructura con el Cuadernillo de planeación (pp. 69 y 79-81) y el Programa Sintético de la Fase 2: datos del proyecto,
  que los PDA sean del grado y de su contenido, los 5 momentos en orden y lo que pide cada uno, inicio/desarrollo/cierre,
  organización, materiales, tiempo, evaluación ligada al PDA, vínculo con el programa analítico y fechas del calendario
  2026-2027. Cada tarjeta del banco dice “✓ Bien estructurada” o “⚠ N por revisar”. No revisa la redacción.
- **Revisar redacción con IA** (en la tarjeta de revisión): copia la planeación con instrucciones basadas en el
  cuadernillo y la Fase 2 para pegarla en Claude (claude.ai o la app; basta una cuenta gratis). La app no se conecta
  a ninguna IA ni tiene costo.
- **PMC**: las actividades del Programa de Mejora Continua 2026-2027 por mes. En el formato, “Actividades de PMC”
  se llena sola con las del mes del *Periodo de tiempo* (o de las fechas de las actividades). Se puede marcar
  qué actividades van en las planeaciones y, en una planeación específica, escribirlas a mano.
- **Analítico**: el Programa Analítico 2026-2027 del jardín, solo de consulta. *Por mes* muestra los contenidos y PDA
  jerarquizados de 2° o 3° en los cuatro campos formativos; *Todo el ciclo* los muestra de septiembre a junio en una
  tabla; *Programa analítico* tiene los tres planos (lectura de la realidad, territorialización y formulación).
- **Avance**: muestra qué PDA del grado ya tienen planeación en el banco y cuáles faltan.

## Para las maestras: cada una con su propio banco

Comparte este link: **https://jnbarbarita.github.io/planeaciones-/maestras.html**

- Es la misma app (formato, Word, PMC, Analítico, Avance), pero el banco empieza **vacío** y es de cada maestra:
  lo que ella sube o captura se guarda **solo en su dispositivo**. No cambia esta app ni el `banco.json` del jardín.
- Con **Copiar del banco del jardín** (pestaña Banco) puede empezar con las planeaciones del jardín y luego
  eliminar las que no use.
- **Descargar banco** guarda una copia de su banco (`mi-banco-de-planeaciones.json`); con **Cargar banco** la pasa
  a su otro dispositivo o la recupera si se borra.
- En el iPhone conviene agregarla primero a la pantalla de inicio (Safari → Compartir → *Agregar a pantalla de inicio*)
  y usarla siempre desde ese ícono: lo guardado en Safari y lo guardado en el ícono son bancos distintos, y Safari
  puede borrar los datos de un sitio que no se abre en varios días.

## Subir planeaciones que ya tienes en Word

En la pestaña **Banco** pulsa **Subir Word** y elige el archivo `.docx` (en el iPhone, desde *Archivos*).
La app lee el formato del jardín: nombre del proyecto, modalidad, problemática, finalidad, ejes,
contenidos y PDA (los acomoda en su campo con la clave del Programa Sintético), actividades por momento
y la tabla final. Con un solo archivo se abre el editor para revisarla antes de guardar; con varios,
se guardan todas de una vez. Los PDF y los .doc antiguos no se pueden leer: guárdalos como Word (.docx).

## Dónde se guardan las planeaciones

- **`banco.json`** es el banco compartido: lo que está ahí aparece en todos tus dispositivos.
- Lo que crees o cambies en la app se guarda primero **solo en ese dispositivo** (la app te avisa).
  Para pasarlo a todos: en la pestaña Banco pulsa **Descargar banco** y sube el archivo `banco.json`
  a este repositorio (*Add file → Upload files*), reemplazando el anterior. En 1 o 2 minutos el sitio
  se actualiza.

## Publicar el sitio (GitHub Pages)

1. *Settings → Pages → Build and deployment → Source: Deploy from a branch*.
2. Elige la rama `main` y la carpeta `/ (root)` → *Save*.
3. El sitio queda en `https://jnbarbarita.github.io/planeaciones-/`.
   (GitHub Pages gratis requiere que el repositorio sea público.)

En el iPhone: abre el sitio en Safari → Compartir → **Agregar a pantalla de inicio**.

## Archivos

| Archivo | Qué es |
|---|---|
| `index.html` | La app (página del sitio). Se genera a partir de `app.html` con `python3 build.py`. |
| `maestras.html`, `manifest-maestras.webmanifest` | “Mi banco de planeaciones”: la app para las maestras, cada una con su banco en su dispositivo. También la genera `build.py`. |
| `app.html` | La misma app en la versión que se publica dentro de Claude. |
| `banco.json` | El banco compartido de planeaciones y el PMC. |
| `catalogo.js` | Contenidos y PDA de los 4 campos formativos (Programa Sintético Fase 2, SEP 2024). |
| `analitico.js` | Programa Analítico 2026-2027 y jerarquización de contenidos de 2° y 3° por mes. |
| `plantilla.js` | Plantilla Word del formato (encabezado, logos, hoja horizontal). |
| `manifest.webmanifest`, `img/icono-*.png` | Nombre e ícono al agregarla a la pantalla de inicio. |
| `img/` | Logos del encabezado. |

Referencias: Programa Sintético de la Fase 2 (SEP, 2024) y el Cuadernillo de Planeación
(momentos por modalidad p. 69, elementos de la planeación pp. 79-81, claves de contenidos y PDA pp. 27 y 42-56).
