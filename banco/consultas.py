
import re
import pymysql
from controle import *
import requests
from time import gmtime, strftime

class CommercePlus:
    def __init__(self):
        lista_pedidos = list()
        pedidos_preparo = CommercePlus.buscaPedidosEnpreparo()
        pedidos_aprovados = CommercePlus.buscaTodosPedidos()
        
        for pedido_preparo in pedidos_preparo:
            lista_pedidos.append(pedido_preparo)
            
        for pedido_aprovados in pedidos_aprovados:
            lista_pedidos.append(pedido_aprovados)
            
        self.Pedidos = lista_pedidos
            
    def buscaPedidosEnpreparo():
        url = 'https://commerceplus.com.br/api/v1/pedidos?situacao=preparando'
        headers = { 'accept': 'application/json', 'User': '73NN15240YGDAGA15310YGDAGA1531' , 'Password': 'a6f1f3380c3614dba4798a61b6c132bf'}

        lista_pedido = list()
        retorno= requests.get(url, headers=headers)
        ListaDePedidos = retorno.json()
        for Pedido in ListaDePedidos:  
            lista_pedido.append(Pedido['idpedido'])
        
        return lista_pedido

    def buscaTodosPedidos():
        url = 'https://commerceplus.com.br/api/v1/pedidos?status=aprovado&situacao=aguardando'
        headers = { 'accept': 'application/json', 'User': '73NN15240YGDAGA15310YGDAGA1531' , 'Password': 'a6f1f3380c3614dba4798a61b6c132bf'}

        lista_pedido = list()
        retorno= requests.get(url, headers=headers)
        ListaDePedidos = retorno.json()
        for Pedido in ListaDePedidos:  
            lista_pedido.append(Pedido['idpedido'])
        
        return lista_pedido

class Banco:
    def getInformacoes(str=str()):
        try:
            conexao = pymysql.connect(db='wwpneu_01', user='wwpneu_01', passwd='?5CgpDW4+lNf' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(str)
            resultado = cursor.fetchall()   

        except Exception as erro:
            pass
        
        finally:
            conexao.close()
        return resultado

    def getPedidoSite():
        try:
            conexao = pymysql.connect(db='wwpneu_01', user='wwpneu_01', passwd='?5CgpDW4+lNf' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute("SELECT order_id FROM oc_order where order_status_id > 0 order by order_id desc LIMIT 300")
            resultado = cursor.fetchall()   

        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        
        finally:
            conexao.close()
        return resultado

    def verifica_pedido_salvo(numeroPedido):
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            sql = str(f"SELECT * FROM dados_pedido WHERE PEDIDO='{numeroPedido}';")
            cursor.execute(sql)
            resultado = cursor.fetchall()  
            if resultado == ():
                retorno = True
            else:
                retorno = False
                
        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        finally:
            conexao.close()
        
        return retorno

    def salva_cotacao(TABELA ,COTACAO ):
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f"INSERT INTO {TABELA} (PEDIDO,N_COTACAO,VALOR,PRAZO,MEDIDAS) VALUES ( '{COTACAO['PEDIDO']}','{COTACAO['N_COTACAO']}','{COTACAO['VALOR']}','{COTACAO['PRAZO']}','{COTACAO['MEDIDAS']}')")
            conexao.commit()
            print('Pedido O.K')
            

        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        finally:
            conexao.close()
    
    def salva_dados_pedido(COTACAO):
        try:
            DATA_AUTAL = strftime("%Y-%m-%d")
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f"INSERT INTO dados_pedido   (PEDIDO ,NOME_CLIENTE, CPF, RUA ,BAIRRO ,CIDADE ,CEP ,UF ,MARCKETPLACE, TOTAL_PEDIDO ,VALOR_FRETE ,FORMA_PAGAMENTO ,PRAZO_ENTREGA ,  TABELA_FRETE ,PESO_TOTAL ,QUANTIDADE_TOTAL ,CUBAGEM,DATA_COTADO  ) VALUES ('{COTACAO['NUMERO_PEDIDO']}','{COTACAO['NOME_CLIENTE']}','{COTACAO['CPF']}','{COTACAO['RUA']}',  '{COTACAO['BAIRRO']}', '{COTACAO['CIDADE']}','{COTACAO['CEP']}','{COTACAO['UF']}','{COTACAO['MARCKETPLACE']}', '{COTACAO['TOTAL_PEDIDO']}', '{COTACAO['VALOR_FRETE']}','{COTACAO['FORMA_PAGAMENTO']}',  '{COTACAO['PRAZO_ENTREGA']}', '{COTACAO['TABELA_FRETE']}',   '{COTACAO['PESO_TOTAL']}', '{COTACAO['QUANTIDADE_TOTAL']}','{COTACAO['CUBAGEM']}','{DATA_AUTAL}')")
            conexao.commit()
            print('Pedido Cotado com Sucesso {}'.format(COTACAO['NUMERO_PEDIDO']))

            

        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        finally:
            conexao.close()
            