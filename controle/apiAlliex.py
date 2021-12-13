from zeep import Client
import xml.etree.ElementTree as ET

class API_Alliex:
    def __init__(self, Cep=str()  ,valorTotal=float() ,quantidade_total=int() ,peso_total=float()  ,cubagem=float()):
        try:
            if (float(cubagem) > 0.68) or (float(peso_total) > 120):
                cubagem = cubagem
                medidas = 'UTILIZADAS'
            else:
                cubagem = 0.02 * quantidade_total
                medidas = 'NAO UTILIZADAS'
                
            

            cliente = Client(wsdl='https://ssw.inf.br/ws/sswCotacaoColeta/index.php?wsdl')
            retorno_api_ssw =  cliente.service.cotar('ALC','gab33403','33403','33403625000153',86804390, Cep, valorTotal , quantidade_total, peso_total, cubagem,1,'C','33403625000153','','','','','','')

            Conteudo_retorno = ET.fromstring(retorno_api_ssw)

            for node in Conteudo_retorno.iter('cotacao'):
                numeroCotacao = node.text

            for node in Conteudo_retorno.iter('frete'):
                valor_cotacao = node.text
                valor_cotacao = valor_cotacao.replace(',','.')
    
            for node in Conteudo_retorno.iter('prazo'):
                prazo_estimado = node.text

            for node in Conteudo_retorno.iter('erro'):
                erro = node.text


            COTACAO_SSW = dict()
            COTACAO_SSW['N_COTACAO'] = numeroCotacao
            COTACAO_SSW['VALOR'] = valor_cotacao
            COTACAO_SSW['PRAZO'] = prazo_estimado
            COTACAO_SSW['MEDIDAS'] = medidas
          
        

        except Exception as erro:
            print(erro)
            COTACAO_SSW = {'N_COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}
        
        self.COTACAO = COTACAO_SSW
        