import xml.etree.ElementTree as ET

# Caminho do arquivo XML
caminho_arquivo = '/home/junior/Downloads/P2822/Patente_2822_04022025.xml'

# Lendo o arquivo XML
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

# Extraindo os valores dos atributos
numero_revista = root.attrib['numero']
dataPublicacao = root.attrib['dataPublicacao']

# Exibindo os valores
print(f'Revista: {numero_revista}')
print(f'Data de Publicação: {dataPublicacao}')

# Extraindo o valor do despacho
for despachos in root.findall('despacho'):
    despacho = despachos.find('codigo').text
    if despacho == '3.1' or despacho == '3.2':
        print(f'Despacho: {despacho}')
        for patentes in despachos.findall('processo-patente'):
            numero_patente = patentes.find('numero').text
            data_deposito = patentes.find('data-deposito').text
            titulo_patente = patentes.find('titulo').text
            print(f'Processo: {numero_patente} de {data_deposito}')
            print(f'Título: {titulo_patente}')
            for titulares in patentes.findall('titular-lista'):
                nome_titular = [titular.find('nome-completo').text for titular in titulares.findall('titular')]
                nomes_titular = '; '.join(nome_titular)
                quantidade_titular = [titular.get('sequencia') for titular in titulares.findall('titular')]
                if len(quantidade_titular) > 1:
                    print(f'Titulares: {nomes_titular}\n')
                else:
                    print(f'Titular: {nomes_titular}\n')
