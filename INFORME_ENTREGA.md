# Informe de entrega — Proyecto CarpuleNet corregido

**Versión:** preparación local para integrar a la rama de producción `main`.
**Origen:** ZIP original de la rama `integrar-articulos-002-003` aportado para auditoría.
**Acciones remotas:** ninguna. El ZIP no se ha subido a GitHub ni desplegado en Vercel.

## Cambios incluidos

1. Se mantiene la arquitectura de **un proyecto Vercel y cuatro subdominios** con mapeos por encabezado `Host`.
2. Se añadieron rutas de ficha de artículo tanto para `/` como para `/index.html`, evitando que la segunda dirección abra la portada común en los dominios individuales.
3. Se incorporó el archivo general de la revista en `/journal` y se actualizaron sus enlaces de navegación.
4. Se cambiaron los enlaces públicos de navegación, URL canónicas y metadatos generales que todavía señalaban al dominio antiguo de Vercel. Los botones PDF enlazan a cada CarpuleNet `/article.pdf`.
5. Se limpió el sitemap/robots genérico y se conservaron cuatro pares de sitemap/robots individuales: cada sitemap lista únicamente el PDF correspondiente.
6. Se eliminaron del PDF 001 la referencia visible al DOI ilustrativo no registrado, el enlace URI y los campos Info/XMP relacionados. Se corrigieron dos `mailto:` internos del mismo PDF.
7. Se conservaron sin cambios binarios los PDF 002, 003 y 004.
8. Se actualizaron el README, la guía de publicación y el inventario del proyecto. Se añadió `scripts/verify_project.py`.

## Validaciones locales

- El verificador automatizado completó **107 comprobaciones**, con **0 fallos**.
- `vercel.json` válido; rutas específicas de los cuatro hosts a 4 PDF distintos, sus fichas HTML, robots y sitemaps.
- Enlaces locales de archivos en HTML: sin destinos inexistentes detectados.
- Sitemaps individuales: cuatro archivos XML válidos, cada uno con una sola URL PDF de su propio dominio.
- Las cuatro páginas de artículo tienen `citation_pdf_url` coherente con su PDF de CarpuleNet.
- Los cuatro PDF son legibles y contienen título/autor; en el 001 no queda el DOI ilustrativo ni el mailto duplicado en contenido, enlaces o metadatos.
- Comparación visual del PDF 001 con la versión original: 7 páginas; diferencias gráficas **solo en página 1**, dentro de la zona del DOI retirado; páginas 2 a 7 idénticas a nivel de rasterizado con el mismo motor.
- PDF 002, 003 y 004: SHA-256 idéntico a los archivos originales.

## Estado de los PDF

| Artículo | Páginas | Binario idéntico al ZIP original | SHA-256 de la versión entregada |
|---|---:|---|---|
| 001 | 7 | No (corregido) | `5bc73555e4484ae55c5a309cd565cc8663ba6d73098b532b9bf3bbe1674f420a` |
| 002 | 10 | Sí | `875e7ced01225a99a5a2fac6704d87224bfdd49e713a42b5436337340cd4a95a` |
| 003 | 8 | Sí | `1e31b55c2866feda043b017383262594401e0161733adcd801b2bb776da58df6` |
| 004 | 5 | Sí | `25f88cd84c01dca84be8eb6262777ce97183fdd8a20e14d912e04f3606ccb41b` |

## Comprobaciones que requieren producción

- Vercel debe desplegar el commit de `main` que contenga estos archivos; un Preview temporal no tiene necesariamente los dominios personalizados adjuntos.
- Confirmar desde un navegador anónimo y con cabeceras HTTP que cada `https://DOMINIO.carpulenet.com/` muestra su propia ficha y cada `/article.pdf` devuelve HTTP 200, `application/pdf`, la cabecera `Link` canónica correcta y ausencia de `X-Robots-Tag: noindex`.
- Confirmar individualmente `sitemap.xml` y `robots.txt` en cada subdominio; solicitar después la indexación de las **URL PDF**, no la de las fichas HTML.
- Los DOI de los artículos 002–004 se preservaron del material aportado; su resolución y metadatos oficiales no quedan certificados por una prueba local de archivos.
- La edición del PDF 001 conservó el adjunto de procedencia `Content Credentials`. No se garantiza que las credenciales criptográficas originales sigan siendo válidas después de modificar el PDF; deben verificarse por el sistema emisor si se necesitan.
- No se garantiza la inclusión en Google o Google Scholar ni se afirma aceptación en una revista externa.

## Ruta de publicación sugerida

Trabaja desde una copia local del repositorio, integra estos archivos en `integrar-articulos-002-003`, ejecuta `python scripts/verify_project.py`, actualiza el pull request #1 y fusiona a `main` **solo después de comprobar el nuevo despliegue Preview**. Vercel desplegará a Production cuando la rama `main` reciba el cambio si la integración Git sigue habilitada. Comprueba el commit y el estado en Vercel y entonces empieza con Google Search Console.

## Segunda comprobación específica solicitada: DOI del PDF 001

Se confirmó que **el DOI de ejemplo no existe** en el texto de las siete páginas, PDF Info, XMP, anotaciones de enlace ni bytes sin comprimir del PDF final. La sección **«Cómo citar este artículo»** permanece, pero termina en el nombre de la revista y el volumen/número, sin DOI. La dirección de correo correcta es visible y extraíble como texto en la página 1. Se adjunta además una copia independiente del PDF limpio en la respuesta al usuario para evitar confundirla con una versión antigua.

La validación es **local**. Los cambios aún deben desplegarse a la rama de producción y probarse mediante solicitudes HTTP desde los dominios de CarpuleNet. No se garantiza la indexación en Google.
