import requests


class API_Rodonaves:
    
    def __init__(self,Cep,pesoTotal,valorTotal,quantidadeTotal,cubagem,produtos):
        try:
            token = API_Rodonaves.get_token()
            produtos = API_Rodonaves.tratamento_produtos(produtos,cubagem ,pesoTotal ,quantidadeTotal)
            cotacao_crua = API_Rodonaves.cotacao(token,Cep,pesoTotal,valorTotal,quantidadeTotal,produtos)
            cotacao = API_Rodonaves.tratamento_cotacao(cotacao_crua,pesoTotal,cubagem)
            

        except Exception as erro:
            print(erro)
            cotacao = {'PEDIDO': '', 'N_COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}
            
        self.COTACAO = cotacao
        
    def get_token():
        
        url = "https://01wapi.rte.com.br/token"
        
        autentificacao = "auth_type=DEV&grant_type=password&username=PNEUSTYRES&password=CZEIH9VM"
        
        headers = {"Content-Type": "application/x-www-form-urlencoded"}

        retorno_text = requests.request("POST", url, data=autentificacao, headers=headers)
        retorno = retorno_text.json()
        
        token = retorno['access_token']
        
        return token
        
    def get_city_id(Cep,token):
        url = "https://01wapi.rte.com.br/api/v1/busca-por-cep?zipCode={}".format(Cep)

        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(token)
        }

        retorno_text = requests.request("GET", url, headers=headers)
        retorno = retorno_text.json()

        id_cidade = retorno['CityId']
        
        return id_cidade
     
    def tratamento_produtos(produtos, cubagem ,pesoTotal ,quantidadeTotal):
        produto_lista = list()
        if (float(cubagem) > 0.68) or (float(pesoTotal) > 120):
            for produto in produtos:
                packs = dict()
                packs['AmountPackages'] = produto['quantidade']
                packs['Weight'] = produto['peso']
                packs['Length'] = produto['comprimento']
                packs['Height'] = produto['altura']
                packs['Width'] = produto['largura']
                
                produto_lista.append(packs.copy())
        else:
            packs = dict()
            packs['AmountPackages'] = quantidadeTotal
            packs['Weight'] = 0
            packs['Length'] = 0
            packs['Height'] = 0
            packs['Width'] = 0
            
            produto_lista.append(packs.copy())
                
        
        return produto_lista
     
    def cotacao(token,Cep,pesoTotal,valorTotal,quantidadeTotal,produtos):
        id_cidade_destino = API_Rodonaves.get_city_id(Cep,token)
        
        url = "https://01wapi.rte.com.br/api/v1/gera-cotacao"


        payload = {
            "Packs": [{'AmountPackages': 16, 'Weight': 0, 'Length': 0, 'Height': 0, 'Width': 0}],
            "OriginZipCode": "86804390",
            "OriginCityId": 5780,
            "DestinationZipCode": 86805300,
            "DestinationCityId": 5780,
            "TotalWeight": 20,
            "EletronicInvoiceValue": 1000,
            "CustomerTaxIdRegistration": 33403625000153,
            "ReceiverCpfcnp": 13033305989,
            "CustomerEmail": "contato@pneustyres.com.br",
            "ContactName": "Pneus Tyres",
            "ContactPhoneNumber": 4331621526,
            "TotalPackages": 16,
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "text/json",
            "Authorization": "Bearer {}".format(token)
        }

        retorno = requests.request("POST", url, json=payload, headers=headers)

        return retorno.json()

    def tratamento_cotacao(cotacao_crua,pesoTotal,cubagem ):
        if (float(cubagem) > 0.68) or (float(pesoTotal) > 120):
            medidas = 'UTILIZADAS'
        else:
            medidas = 'NAO UTILIZADAS'
        
        COTACAO_SSW = dict()
        COTACAO_SSW['N_COTACAO'] = cotacao_crua['ProtocolNumber']
        COTACAO_SSW['VALOR'] = cotacao_crua['Value']
        COTACAO_SSW['PRAZO'] = cotacao_crua['DeliveryTime']
        COTACAO_SSW['MEDIDAS'] = medidas
        
        return COTACAO_SSW
    
