# Open Source Journal of Dental Regeneration & Biology

Publicación académica y archivo de investigación independiente. Proyecto web estático para Vercel, con cuatro documentos PDF y cuatro dominios individuales de CarpuleNet.

## Organización

- Archivo general: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/journal
- Catálogo completo: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/articles.html

| ID | Artículo | Documento PDF canónico |
|---|---|---|
| 001 | Más allá de la revitalización: criterios biológicos para evaluar la regeneración del complejo dentino-pulpar en la endodoncia contemporánea | https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/article.pdf |
| 002 | The Clinical AI Safety Gap from Correct Answers to Safer Decisions | https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/article.pdf |
| 003 | Clinical–Laboratory Variability in Digitally Fabricated Complete Dentures: A Critical Evidence Synthesis and Traceability Framework | https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/article.pdf |
| 004 | De la hipótesis al manuscrito: ¿puede una inteligencia artificial conducir una investigación computacional completa? | https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/article.pdf |

## Política de indexación

- Cada subdominio publica su propia ficha en `/` y `/index.html`.
- Cada artículo tiene un único PDF principal en `https://HOST/article.pdf`.
- Cada subdominio publica `/sitemap.xml` con **solo el PDF individual**.
- Las fichas y páginas generales contienen `noindex, follow` por elección editorial: prioridad a los PDF en Google Search, no a las páginas HTML.
- Los PDF contienen `X-Robots-Tag: index, follow` y cabecera HTTP `Link` de canónica.
- La indexación no es automática ni garantizada. Los resultados de Google Scholar obedecen a criterios distintos.

## Identificadores

El artículo 001 carece de DOI registrado. Se ha eliminado del PDF el identificador ilustrativo anterior. Su identificador **local** `OSJDRB-2026-001` no es un DOI. Los artículos 002–004 contienen identificadores que ya figuraban en los manuscritos depositados en plataformas externas; comprueba los registros correspondientes antes de atribuirles una publicación editorial distinta.

## Comprobaciones antes de publicar

Requiere Python 3 y PyMuPDF (`pip install pymupdf`). Desde la raíz del proyecto:

```bash
python scripts/verify_project.py
python -m json.tool vercel.json > /dev/null
```

Para producción, la rama configurada en Vercel según la captura proporcionada es `main`. Este ZIP **no se ha desplegado**: para publicar, integra sus archivos a la rama de producción después de verificarlos, y confirma que el despliegue generado apunta al commit esperado. Las reglas por dominio no se pueden comprobar desde la raíz de una URL temporal de Preview porque dependen del encabezado `Host`.

Consulta `GUIA-4-SUBDOMINIOS.md` para la verificación HTTP real y las solicitudes individuales en Search Console.
