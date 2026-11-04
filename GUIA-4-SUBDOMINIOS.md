# Guía de publicación y comprobación de los cuatro subdominios CarpuleNet

## Estado de la entrega
- El proyecto se entrega como ZIP corregido; **no se ha publicado en Production**.
- Los cuatro subdominios estaban asociados a Production en las capturas aportadas. No cambiar DNS sin una razón concreta.
- La rama Production de Vercel se configuró como `main`. En el momento de la auditoría anterior, esa rama todavía no contenía los artículos 002–004.

## Rutas definitivas (después del despliegue a main)

### 001 · Más allá de la revitalización: criterios biológicos para evaluar la regeneración del complejo dentino-pulpar en la endodoncia contemporánea
- Ficha: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/
- PDF: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/article.pdf
- Sitemap: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/sitemap.xml
- Robots: https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/robots.txt

### 002 · The Clinical AI Safety Gap from Correct Answers to Safer Decisions
- Ficha: https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/
- PDF: https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/article.pdf
- Sitemap: https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/sitemap.xml
- Robots: https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/robots.txt

### 003 · Clinical–Laboratory Variability in Digitally Fabricated Complete Dentures: A Critical Evidence Synthesis and Traceability Framework
- Ficha: https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/
- PDF: https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/article.pdf
- Sitemap: https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/sitemap.xml
- Robots: https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/robots.txt

### 004 · De la hipótesis al manuscrito: ¿puede una inteligencia artificial conducir una investigación computacional completa?
- Ficha: https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/
- PDF: https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/article.pdf
- Sitemap: https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/sitemap.xml
- Robots: https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/robots.txt

## Procedimiento seguro
1. Descomprimir este ZIP en una copia de trabajo del repositorio.
2. Ejecutar `python scripts/verify_project.py` y corregir cualquier fallo.
3. Integrar a `main` con el procedimiento Git habitual, sin borrar la configuración de dominios.
4. En Vercel, confirmar que el despliegue de **Production** procede del nuevo commit de `main` y está **Ready**.
5. Abrir cada subdominio en ventana privada y confirmar el título de su artículo.
6. Comprobar cada `/article.pdf`, `/sitemap.xml` y `/robots.txt`.
7. Verificar cabeceras HTTP y ausencia de autenticación o `noindex` en el PDF.
8. Solo entonces solicitar indexación en Search Console para cada PDF de CarpuleNet.

## Prueba HTTP externa recomendada (Git Bash)
```bash
curl -IL "https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/article.pdf"
curl -L "https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/sitemap.xml"
curl -L "https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/robots.txt"
curl -IL "https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/article.pdf"
curl -L "https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/sitemap.xml"
curl -L "https://clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com/robots.txt"
curl -IL "https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/article.pdf"
curl -L "https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/sitemap.xml"
curl -L "https://clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com/robots.txt"
curl -IL "https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/article.pdf"
curl -L "https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/sitemap.xml"
curl -L "https://de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com/robots.txt"
```

En cada PDF confirmar `200`, `application/pdf`, `Link: <https://DOMINIO/article.pdf>; rel="canonical"` y que no exista `X-Robots-Tag: noindex`. En cada sitemap comprobar una sola URL, correspondiente a su artículo. Una URL de Vercel Preview no sustituye al dominio CarpuleNet en Search Console.

## Ajustes editoriales
- PDF 001: se eliminó el DOI ilustrativo que no estaba registrado de la referencia visible, sus enlaces y metadatos; se corrigieron dos anotaciones mailto. No se cambió la paginación.
- PDF 002, 003 y 004: copias binarias idénticas a las del ZIP original.
- El PDF 001 llevaba un adjunto de procedencia `Content Credentials`. Se ha preservado, aunque cualquier edición PDF puede invalidar acreditaciones criptográficas asociadas al archivo antiguo; no se garantiza una firma o credencial válida después de editarlo.
- Un encabezado editorial dentro de un PDF no implica aceptación por una revista externa.
- La publicación en CarpuleNet no crea un DOI ni garantiza indexación o evaluación por pares.
