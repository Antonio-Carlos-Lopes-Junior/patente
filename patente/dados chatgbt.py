import xml.etree.ElementTree as ET

# Caminho do arquivo XML
caminho_arquivo = '/home/junior/Downloads/P2822/Patente_2822_04022025.xml'

# Lendo o arquivo XML
tree = ET.parse(caminho_arquivo)
root = tree.getroot()

# Extraindo os valores dos atributos
numero_revista = root.attrib.get('numero')
data_publicacao = root.attrib.get('dataPublicacao')

# Exibindo os valores
print(f'Revista: {numero_revista}')
print(f'Data de Publicação: {data_publicacao}')

# Função para extrair e imprimir os dados da patente
def extrair_dados_patentes(despacho):
    for patentes in despacho.findall('processo-patente'):
        numero_patente = patentes.find('numero').text
        data_deposito = patentes.find('data-deposito').text
        titulo_patente = patentes.find('titulo').text
        print(f'Processo: {numero_patente} de {data_deposito}')
        print(f'Título: {titulo_patente}')

        # Extraindo os titulares
        for titulares in patentes.findall('titular-lista'):
            nomes_titular = '; '.join(titular.find('nome-completo').text for titular in titulares.findall('titular'))
            print(f'Titulares: {nomes_titular}\n' if ';' in nomes_titular else f'Titular: {nomes_titular}\n')

# Extraindo o valor do despacho e imprimindo informações relevantes
for despacho in root.findall('despacho'):
    codigo_despacho = despacho.find('codigo').text
    if codigo_despacho in ['3.1', '3.2']:  # Condição para despachos relevantes
        print(f'Despacho: {codigo_despacho}')
        extrair_dados_patentes(despacho)