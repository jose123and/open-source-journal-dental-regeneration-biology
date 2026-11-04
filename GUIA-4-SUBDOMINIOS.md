# Actualización: 4 artículos, 1 subdominio existente y 3 nuevos para CarpuleNet

## Sitio y seguridad
No reemplazar ni borrar la carpeta original. Este paquete actualiza únicamente archivos web, PDFs y reglas de Vercel. El código se prepara en la rama `integrar-articulos-002-003` y **no** debe publicarse antes de configurar los dominios DNS.

## 001 conserva el subdominio existente; 002, 003 y 004 son propuestas (requieren alta real en Vercel y DNS)
- 001: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/ -> DOI del documento 10.68421/odrb.001
- 002: https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/ -> DOI del documento 10.66977/xsci.2611.000e
- 003: https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/ -> DOI del documento 10.66977/xsci.2611.000c
- 004: https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/ -> DOI del documento 10.5281/zenodo.21755496

En Vercel, dentro del proyecto de la revista, entrar en Settings > Domains y mantener el dominio 001 ya registrado y agregar los otros tres subdominios. En el proveedor DNS de carpulenet.com crear únicamente los tres registros CNAME nuevos que Vercel indique específicamente (NO modificar los registros A de carpulenet.com ni los subdominios existentes). Los `rewrites` de `vercel.json` hacen que la raíz de cada subdominio muestre la ficha única y `article.pdf` ofrezca el documento adecuado.

## Comprobación local antes de hacer commit
```bash
git status --short
git diff --check
python -m json.tool vercel.json > /dev/null
for n in 001 002 003 004; do test -f articles/2026/$n/index.html || exit 1; done
```

Después de publicar, verificar con un navegador que cada subdominio muestre el artículo correcto y que `/article.pdf`, `/robots.txt` y `/sitemap.xml` funcionen. En Google Search Console verificar la propiedad de dominio `carpulenet.com` mediante DNS (si no lo está) e inspeccionar los cuatro URLs únicos. La indexación no está garantizada. Google Scholar puede ser independiente de Google Search Console.

## Advertencias editoriales identificadas
- PDF 001 y PDF 004: el correo visible del autor contiene `jose.tlc.tlc.16@hotmail.com`, diferente del correo correcto indicado en HTML. Estos PDFs conservan su contenido visible; revisar el texto fuente antes de publicar si se desea corregirlo.
- PDF 003: el resumen presenta un texto incompleto en inglés (`through the review cutoff .`); se recomienda corregirlo en el documento fuente antes de dar por definitiva esa versión.
- Las cadenas DOI se copiaron de los PDFs y se incorporaron a los metadatos y a los enlaces; la resolución o registro externo de cada DOI no pudo certificarse.
- Los artículos 002–004 se presentan como obras disponibles en el archivo, sin adjudicarles arbitrariamente el volumen o la condición editorial del artículo 001.

## Sobre los metadatos PDF
Se añadieron metadatos PDF Info y XMP para título, autor, palabras clave, ORCID, DOI y un identificador local como `OSJDRB-2026-001`. Estos identificadores locales **no son DOI**. Las páginas visibles y el texto extraído de los PDFs se preservaron. Los PDF modificados en metadatos tienen nuevos hashes; no son idénticos byte a byte a los PDF recibidos.
