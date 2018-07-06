import xml.etree.cElementTree as ET

tree = ET.parse('ficha.xml')

root = tree.getroot()

obrigatorias = {}
limitadas_dict = {}

with open('obrigatorias.txt', 'r') as obrig_file:
    for line in obrig_file:
        cod, mat = line.split(';')
        obrigatorias[cod] = mat.strip()

with open('limitadas.txt', 'r') as limitadas:
    for line in limitadas:
        cod, mat = line.split(';')
        limitadas_dict[cod] = mat.strip()

discp_feitas = {}

for child in root.findall('Disciplina'):
    cod_discp_feita = child.find('codigo').text
    nome_discp_feita = child.find('disciplina').text
    if (cod_discp_feita in obrigatorias.keys() or nome_discp_feita in obrigatorias.values()) and child.find('situacao').text != "Reprovado":
        #print(child.find('disciplina').text)
        discp_feitas[cod_discp_feita] = nome_discp_feita
    if (cod_discp_feita in limitadas_dict.keys() or nome_discp_feita in limitadas_dict.values()) and child.find('situacao').text != "Reprovado":
        #print(child.find('disciplina').text)
        discp_feitas[cod_discp_feita] = nome_discp_feita

values = discp_feitas.values()
if "Cálculo Numérico" in values:
    print("aaa")
for x, y in obrigatorias.items():
    print(y)
    if x not in discp_feitas.keys() or y.strip() not in values:
        print(x, y)

## teste