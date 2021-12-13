import requests

class API_CEP:
    def __init__(self,CEP):
        try:
            url = f'https://viacep.com.br/ws/{CEP}/json/'
            retorno= requests.get(url)
            CEP = retorno.json()
        
        except Exception as erro:
            CEP = {'cep': CEP, 'logradouro': '', 'complemento': '', 'bairro': '', 'localidade': '', 'uf': ''}
            
        self.CEP = CEP

