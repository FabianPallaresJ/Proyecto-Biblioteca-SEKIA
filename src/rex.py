import re
import json

S = "[1] Alaman A., Materiales metálicos de construcción Colegio de Ingenieros,de caminos, canales y puertos, 2000 [2] Arredondo  F., generalidades sobre materiales de construcción Revista Obras Públicas E.T.S. Ingenieros de Caminos, 1990 [3] Arredondo  F., Piedras, cerámica y vidrio Revista Obras Públicas E.T.S. Ingenieros de Caminos, 1990 [4] Beer y Johnston, Mecánica de materiales, Mc Graw Hill, 1995[5] Callister, Introducción a la ciencia e ingeniería de los materiales, Reverté, 1995.[6] Crissweel, Propierties of materiales, Colorado State University (Notas de clase)[7] Gordon, J.E. La nueva ciencia de los materiales, Celeste Ediciones 2002.[8] Sanchez de Guzmán. ¿Tecnología del concreto y del mortero, Bhandar,1996.[9] Shackelford J, Introducción a la ciencia de materials para ingenieros, Prentice Hall, 2006.[10] Mamlouk M, Zaniewski J. Materials for Civil and Construction Engineers. Pearson 2011.[11] Smith R.C. Materials of construction, Mc Graw Hill, 1973 [12] Yang H. Pavement analysis and Design Prentice Hall. 2004 [13] Young et al, The science and technology of civil engineering materials, Prentice Hall, 1998. [14] NORMAS TÉCNICAS COLOMBIANAS NTC 1998.[15] NORMAS TÉCNICAS INSTITUTO NACIONAL DE VIAS, 2013[16] NORMAS ASTM 2006[17] NSR 2010[18] Segui, W. Steel Design. 5th Ed. Cengage Learning, 2013.[19] Cao, G., Wang Y. Nanostructures and nanomaterials. Vol 2. World Scientific. 2011[20] Askeland, D. Ciencia e Ingeniería de los Materiales. International Thomson. 3  Edición o superior. 1998"


Ordinal_numeral = r'\[[1-9]\d{0,2}\]' ''
#Author_name = r'[A-Z]\w+'
Authors = r'[a-zA-Z .&]+\,' ''
title = r'[\w \-:\,]+'
year = r'\d{4}'


IEEE = re.compile(Ordinal_numeral +
                  Authors+title)

IEEE = re.compile(r'(?P<numeral>\[[1-9]\d{0,2}\]\s)'
                r'(?P<authors>[a-zA-Z .&]+\,\s)'
                r'(?P<title>[\w \-:\,\.\(\)]+)'
                r'(?P<year>\d{4})')


m = IEEE.match(S)

print(m)

m = IEEE.findall(S)

print(m)

with open('./src/resultado.json', 'w') as file:
    json.dump(m, file, indent=4)

print(len(m))