#!/usr/bin/env python3
"""Comprobación local sin conexiones externas ni cambios en archivos.

Valida las rutas por dominio, PDF, sitemaps, robots, HTML, DOI ficticio retirado,
metadatos y vínculos. Para lectura PDF profunda instalar PyMuPDF (pip install pymupdf).
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path
from html.parser import HTMLParser
from xml.etree import ElementTree as ET
from urllib.parse import urlparse

ROOT=Path(__file__).resolve().parents[1]
SITES={
 '001':('open-source-journal-of-dental-regeneration-biology.carpulenet.com','mas-alla-de-la-revitalizacion.pdf','Más allá de la revitalización'),
 '002':('clinical-ai-safety-gap-from-correct-answers-to-safer-decisions.carpulenet.com','clinical-ai-safety-gap.pdf','The Clinical AI Safety Gap'),
 '003':('clinical-laboratory-variability-in-digital-complete-dentures.carpulenet.com','clinical-laboratory-complete-dentures.pdf','Clinical–Laboratory Variability'),
 '004':('de-la-hipotesis-al-manuscrito-agentes-cientificos.carpulenet.com','de-la-hipotesis-al-manuscrito.pdf','DE LA HIPÓTESIS AL MANUSCRITO'),
}
OLD_INVALID='10.' + '68421' + '/odrb.' + '001'
ISSUES=[]
PASSED=[]
def check(condition,message):
 (PASSED if condition else ISSUES).append(message)

class Links(HTMLParser):
 def __init__(self): super().__init__();self.links=[];self.metas=[];self.jsonlds=[];self._injson=False;self._json=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag in ('a','link','script','img'):
   val=a.get('href') or a.get('src')
   if val:self.links.append(val)
  if tag=='meta':self.metas.append(a)
  if tag=='script' and a.get('type')=='application/ld+json':self._injson=True;self._json=[]
 def handle_data(self,data):
  if self._injson:self._json.append(data)
 def handle_endtag(self,tag):
  if tag=='script' and self._injson:
   self.jsonlds.append(''.join(self._json));self._injson=False

vfile=ROOT/'vercel.json'
config=json.loads(vfile.read_text(encoding='utf-8'))
check(isinstance(config.get('routes'),list),'Configuración JSON con tabla de rutas')
check(config['routes'][-1].get('handle')=='filesystem','Fallback filesystem al final')

def resolve(host,path):
 for entry in config['routes']:
  if 'handle' in entry: break
  if not re.fullmatch(entry['src'],path):continue
  hs=entry.get('has',[])
  if any(h.get('type')=='host' and h.get('value')!=host for h in hs):continue
  return entry['dest']
 return path

for n,(host,pdf,title) in SITES.items():
 base=ROOT/'articles/2026'/n
 expected={'/':f'/articles/2026/{n}/index.html',
   '/index.html':f'/articles/2026/{n}/index.html',
   '/article.pdf':f'/articles/2026/{n}/{pdf}',
   '/sitemap.xml':f'/sitemaps/{n}.xml',
   '/robots.txt':f'/robots/{n}.txt'}
 for route,loc in expected.items():
  got=resolve(host,route)
  check(got==loc and (ROOT/got.lstrip('/')).is_file(),f'{n}: {route} -> {loc}')
 check(resolve(host,'/journal')=='/index.html',f'{n}: archivo general /journal')
 doc=base/pdf
 b=doc.read_bytes()
 check(b[:5]==b'%PDF-',f'{n}: PDF binario válido')
 doc_html=(base/'index.html').read_text(encoding='utf-8')
 check(title.casefold()[:16] in doc_html.casefold(),f'{n}: HTML muestra título correcto')
 check(f'https://{host}/article.pdf' in doc_html,f'{n}: URL PDF CarpuleNet en HTML')
 check('noindex, follow' in doc_html,f'{n}: Ficha noindex; PDF indexable')
 page=Links();page.feed(doc_html)
 for item in page.jsonlds:
  try:json.loads(item)
  except Exception as e:ISSUES.append(f'{n}: JSON-LD inválido {e}')
 check(any(m.get('name')=='citation_pdf_url' and m.get('content')==f'https://{host}/article.pdf' for m in page.metas),f'{n}: cita PDF correcta')
 sitemap=ROOT/f'sitemaps/{n}.xml'
 xml=ET.parse(sitemap)
 urls=[x.text for x in xml.findall('.//{*}loc')]
 check(urls==[f'https://{host}/article.pdf'],f'{n}: sitemap contiene solo PDF propio')
 robots=(ROOT/f'robots/{n}.txt').read_text()
 check('Allow: /' in robots and f'Sitemap: https://{host}/sitemap.xml' in robots,f'{n}: robots individual correcto')
 # Headers for publicly served PDFs; one matching canonical per host.
 hdrs=[h for h in config['headers'] if h.get('source')=='/article.pdf' and h.get('has',[{}])[0].get('value')==host]
 check(len(hdrs)==1 and any(kv['key'].lower()=='link' and kv['value']==f'<https://{host}/article.pdf>; rel="canonical"' for kv in hdrs[0]['headers']),f'{n}: cabecera canónica PDF por dominio')

for name in ['index.html','articles.html','about.html','editorial.html']:
 p=ROOT/name;html=p.read_text(encoding='utf-8'); parser=Links();parser.feed(html)
 check('noindex, follow' in html,f'{name}: política HTML noindex')
 check('vercel.app' not in html,f'{name}: sin URLs temporales de Vercel')
 check(any(x.startswith('https://open-source-journal-of-dental-regeneration-biology.carpulenet.com/') for x in parser.links),f'{name}: navegación CarpuleNet')

check(resolve('other.example.org','/sitemap.xml')=='/sitemap.xml','Fallback a sitemap.xml genérico')
check(ET.parse(ROOT/'sitemap.xml') is not None,'Sitemap fallback XML bien formado')
check(len(ET.parse(ROOT/'sitemap.xml').findall('.//{*}loc'))==1,'Sitemap fallback solo PDF')
check('vercel.app' not in (ROOT/'robots.txt').read_text(),'Robots fallback sin dominio antiguo')

# No string of the falsely proposed DOI remains in the delivered project's files (incl. documentation).
for p in ROOT.rglob('*'):
 if not p.is_file():continue
 content=p.read_bytes()
 if OLD_INVALID.encode() in content:ISSUES.append(f'Identificador no registrado encontrado en {p.relative_to(ROOT)}')
 if (b'jose.tlc.' + b'tlc.16@hotmail.com') in content:ISSUES.append(f'Correo equivocado encontrado en {p.relative_to(ROOT)}')
 if p.suffix.lower() in ('.html','.xml','.txt','.md','.json') and b'open-source-journal-dental-regenera.vercel.app' in content:
  ISSUES.append(f'Dominio antiguo encontrado en {p.relative_to(ROOT)}')

try:
 import fitz
 for n,(host,pdf,title) in SITES.items():
  d=fitz.open(ROOT/f'articles/2026/{n}/{pdf}')
  check(not d.is_encrypted and len(d)>0,f'{n}: PDF sin cifrado y con páginas')
  check(title.casefold()[:15] in d[0].get_text().casefold(),f'{n}: contenido de título concordante')
  check(bool(d.metadata.get('author') and d.metadata.get('title')),f'{n}: PDF con título y autor')
  for page in d:
   for link in page.get_links():
    if n=='001':
     check('jose.tlc.tlc' not in link.get('uri',''), '001: sin enlace mailto incorrecto' )
     check(OLD_INVALID not in link.get('uri',''), '001: sin enlace DOI ilustrativo' )
  if n=='001':
   check(OLD_INVALID not in ''.join(pg.get_text() for pg in d),'001: sin DOI ficticio en texto PDF')
   check(OLD_INVALID not in (d.get_xml_metadata() or ''),'001: sin DOI ficticio en XMP')
   check('jose.tlc.16@hotmail.com' in d[0].get_text(sort=True),'001: correo visible extraíble por el buscador')
   check(OLD_INVALID not in str(d.metadata),'001: sin DOI ficticio en PDF Info')
except ImportError:
 print('NOTA: PyMuPDF no instalado; verificación profunda del contenido de PDF omitida.')

print(f'PROYECTO: {ROOT}\nCOMPROBACIONES SUPERADAS: {len(PASSED)}\nFALLOS: {len(ISSUES)}')
for s in ISSUES:print('ERROR:',s)
print('RESULTADO:', 'APROBADO LOCALMENTE' if not ISSUES else 'FALLIDO')
sys.exit(1 if ISSUES else 0)
