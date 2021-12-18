import requests


class API_Rodonaves:
    
    def __init__(self,Cep,pesoTotal,valorTotal,quantidadeTotal,cubagem,produtos):
        try:
            #token = API_Rodonaves.get_token()
            token = '_lgdFrzuNNFTXoW25BdYriNNyu-CRGebTKHaUjMCWWDkGg9Qy6aqY5o8tqicSDJYVOUKY_Sssfs60xB_CruOx4gSzGpJhG2SelWYU53Dk0i-KJEUUDf0rbOwhF7y2OUORO-mddac1xFNnEn3YkkxHiDzleKT0igRnxWu55_jmq1A_BaOMUxN7_NSMkBG0OKW3K1dsJu3G8OCDp3zsCIK5EMOixzTstCiYVxLfCl3YBmS4tep7DV5UnJ5kR6RDW7q9cuEj46sn_cZk-Eume_Yc3xKg19np8Hn3x2rQyFjDnhc9TyCLivgtRtfwOWUeXPIR7Kl1LisP-G_t-wagdXIbq1gQ2obyD7_mhDP2GVgvDAu4642UUllvJvvln2elNLBdjJzTMPfphRHTHEo9lUbS6jhxyQ5CpjA7sIaY-NZgkFdugYaIZH0M_6yUHVG3imaPdCIHKSDsrKKIoZPqaYGNw'
            produtos = API_Rodonaves.tratamento_produtos(produtos,cubagem ,pesoTotal ,quantidadeTotal)
            print('to aqui 1')
            cotacao_crua = API_Rodonaves.cotacao(token,Cep,pesoTotal,valorTotal,quantidadeTotal,produtos)
            print('to aqui 2')
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
        Cep = int(Cep)
        url = "https://01wapi.rte.com.br/api/v1/busca-por-cep?zipCode={}".format(Cep)


        headers = {
            "Accept": "application/json",
            "Authorization": "Bearer {}".format(token)
        }

        retorno_text = requests.get( url, headers=headers)
        retorno = retorno_text.json()
        
        try:
            id_cidade = retorno['CityId']
        except:
            id_cidade = 'NAO ANTENDE'
        
       
        print(id_cidade)
        return id_cidade
     
    def tratamento_produtos(produtos, cubagem ,pesoTotal ,quantidadeTotal):
        produto_lista = list()
        if (float(cubagem) > 0.68) or (float(pesoTotal) > 120):
            for produto in produtos:
                packs = dict()
                packs['AmountPackages'] = int(produto['QUANTIDADE'])
                packs['Weight'] = int(produto['PESO'])
                packs['Length'] = int(produto['COMPRIMENTO'])
                packs['Height'] = int(produto['ALTURA'])
                packs['Width'] = int(produto['LARGURA'])
                
                produto_lista.append(packs.copy())
        else:
            packs = dict()
            packs['AmountPackages'] = int(quantidadeTotal)
            packs['Weight'] = 0
            packs['Length'] = 0
            packs['Height'] = 0
            packs['Width'] = 0
            
            produto_lista.append(packs.copy())
                
        
        return produto_lista
     
    def cotacao(token,Cep,pesoTotal,valorTotal,quantidadeTotal,produtos):
        
        id_cidade_destino = API_Rodonaves.get_city_id(Cep,token)

        if  id_cidade_destino == 'NAO ANTENDE':
            retorno = {'Value': 0, 'DeliveryTime': 0, 'ProtocolNumber': "RTE não atende CEP ({}) informado".format(Cep), 'CustomerEmail': 'contato@pneustyres.com.br', 'Cubed': '', 'Message': '', 'ExpirationDay': '', 'ContactName': '', 'ContactPhoneNumber': '', 'AmountPacks': 0, 'UnitDestinyDescription': None, 'UnitOriginDescription': None, 'ReceiptForm': None, 'EmissionDate': '0001-01-01T00:00:00', 'ActiveDeliveryTime': True, 'DeliveryPhysicalPerson': 2, 'DeliveryLegalPerson': 0}
       
        else:
            url = "https://01wapi.rte.com.br/api/v1/gera-cotacao"
            payload = {
                "Packs": produtos,
                "OriginZipCode": "86804390",
                "OriginCityId": 5780,
                "DestinationZipCode": str(Cep),
                "DestinationCityId": int(id_cidade_destino),
                "TotalWeight": int(pesoTotal),
                "EletronicInvoiceValue": float(valorTotal),
                "CustomerTaxIdRegistration": 33403625000153,
                "ReceiverCpfcnp": 13033305989,
                "CustomerEmail": "contato@pneustyres.com.br",
                "ContactName": "Pneus Tyres",
                "ContactPhoneNumber": 4331621526,
                "TotalPackages": int(quantidadeTotal),
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "text/json",
                "Authorization": "Bearer {}".format(token)
            }

            retorno = requests.request("POST", url, json=payload, headers=headers)
            retorno = retorno.json()
        
        
        return retorno

    def tratamento_cotacao(cotacao_crua,pesoTotal,cubagem ):
        print(cotacao_crua)
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
    
    
    
