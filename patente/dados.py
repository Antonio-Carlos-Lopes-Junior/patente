import xml.etree.ElementTree as ET


class Patente:
    def __init__(self, numero, data_deposito, titulo, titulares):
        self.numero = numero
        self.data_deposito = data_deposito
        self.titulo = titulo
        self.titulares = titulares

    def __str__(self):
        titulares_str = "; ".join(self.titulares) if len(self.titulares) > 1 else self.titulares[0]
        titulares_prt = f"Titulares: {titulares_str}" if ";" in titulares_str else f"Titular: {titulares_str}"
        return f"Processo: {self.numero} de {self.data_deposito}\nTítulo: {self.titulo}\n{titulares_prt}"


class Despacho:
    def __init__(self, codigo):
        self.codigo = codigo
        self.patentes = []

    def adicionar_patente(self, patente):
        self.patentes.append(patente)

    def exibir_patentes(self):
        for patente in self.patentes:
            print(patente)
            print()


class Revista:
    def __init__(self, numero, data_publicacao):
        self.numero = numero
        self.data_publicacao = data_publicacao
        self.despachos = []

    def adicionar_despacho(self, despacho):
        self.despachos.append(despacho)

    def exibir_despachos(self):
        for despacho in self.despachos:
            print(f"Despacho: {despacho.codigo}")
            despacho.exibir_patentes()


class ProcessadorXML:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo
        self.revista = None

    def processar(self):
        tree = ET.parse(self.caminho_arquivo)
        root = tree.getroot()

        numero_revista = root.attrib.get('numero')
        data_publicacao = root.attrib.get('dataPublicacao')
        self.revista = Revista(numero_revista, data_publicacao)

        for despacho_elem in root.findall('despacho'):
            codigo_despacho = despacho_elem.find('codigo').text
            if codigo_despacho in ['3.1', '3.2']:  # Condição para despachos relevantes
                despacho = Despacho(codigo_despacho)
                for patente_elem in despacho_elem.findall('processo-patente'):
                    numero_patente = patente_elem.find('numero').text
                    data_deposito = patente_elem.find('data-deposito').text
                    titulo_patente = patente_elem.find('titulo').text

                    titulares = [
                        titular.find('nome-completo').text for titular in patente_elem.findall('titular-lista/titular')
                    ]

                    patente = Patente(numero_patente, data_deposito, titulo_patente, titulares)
                    despacho.adicionar_patente(patente)
                self.revista.adicionar_despacho(despacho)

    def exibir_dados(self):
        print(f'Revista: {self.revista.numero}')
        print(f'Data de Publicação: {self.revista.data_publicacao}')
        self.revista.exibir_despachos()


# Exemplo de uso
caminho_arquivo = '/home/junior/Downloads/P2822/Patente_2822_04022025.xml'
processador = ProcessadorXML(caminho_arquivo)
processador.processar()
processador.exibir_dados()