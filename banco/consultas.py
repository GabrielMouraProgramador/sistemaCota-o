import pymysql
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

    def getInformacoesCotacao(pedido):
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f'''SELECT 
            dados.* , 
            alliex_td.N_COTACAO  as alliex_ncotacao ,
            alliex_td.VALOR  as alliex_valor,
            alliex_td.PRAZO  as alliex_prazo,
            alliex_td.MEDIDAS  as alliex_medidas,
            
            direcinal_td.N_COTACAO  as direcinal_ncotacao ,
            direcinal_td.VALOR  as direcinal_valor,
            direcinal_td.PRAZO  as direcinal_prazo,
            direcinal_td.MEDIDAS  as direcinal_medidas,
            
            mid_td.N_COTACAO  as mid_ncotacao ,
            mid_td.VALOR  as mid_valor,
            mid_td.PRAZO  as mid_prazo,
            mid_td.MEDIDAS  as mid_medidas,
            
            rodonaves_td.N_COTACAO  as rodonaves_ncotacao ,
            rodonaves_td.VALOR  as rodonaves_valor,
            rodonaves_td.PRAZO  as rodonaves_prazo,
            rodonaves_td.MEDIDAS  as rodonaves_medidas,
            
            transreis_td.N_COTACAO  as transreis_ncotacao ,
            transreis_td.VALOR  as transreis_valor,
            transreis_td.PRAZO  as transreis_prazo,
            transreis_td.MEDIDAS  as transreis_medidas,
            
            saomiguel_td.N_COTACAO  as saomiguel_ncotacao ,
            saomiguel_td.VALOR  as saomiguel_valor,
            saomiguel_td.PRAZO  as saomiguel_prazo,
            saomiguel_td.MEDIDAS  as saomiguel_medidas
            
        
        FROM 
            dados_pedido as dados, 
            alliex_transportadora as alliex_td,
            direcional_transportadora as direcinal_td,
            mid_transportadora as mid_td,
            rodonaves_transportadora as rodonaves_td,
            transreis_transportadora as transreis_td,
            sao_miguel_transportadora as saomiguel_td

        WHERE 
            dados.PEDIDO = alliex_td.PEDIDO and
            dados.PEDIDO = direcinal_td.PEDIDO and
            dados.PEDIDO = mid_td.PEDIDO and
            dados.PEDIDO = rodonaves_td.PEDIDO  and
            dados.PEDIDO = transreis_td.PEDIDO and
            dados.PEDIDO = saomiguel_td.PEDIDO and
            dados.PEDIDO = {pedido} ''')
            
            resultado = cursor.fetchall()   
            pedido_info = dict()
            pedido_info['PEDIDO'] = resultado[0][0]
            pedido_info['NOME'] = resultado[0][1]
            pedido_info['CPF'] = resultado[0][2]
            pedido_info['RUA'] = resultado[0][3]
            pedido_info['BAIRRO'] = resultado[0][4]
            pedido_info['CIDADE'] = resultado[0][5]
            pedido_info['CEP'] = resultado[0][6]
            pedido_info['UF'] = resultado[0][7]
            pedido_info['MARCKETPLACE'] = resultado[0][8]
            pedido_info['TOTALPEDIDO'] = resultado[0][9]
            pedido_info['VALORFRETE'] = resultado[0][10]
            pedido_info['FORMAPAGAMENTO'] = resultado[0][11]
            pedido_info['PRAZOENTREGA'] = resultado[0][12]
            pedido_info['TABELAFRETE'] = resultado[0][13]
            pedido_info['PESOTOTAL'] = resultado[0][14]
            pedido_info['QUANTIDADETOTAL'] = resultado[0][15]
            pedido_info['CUBAGEM'] = resultado[0][16]
            pedido_info['DATA'] = resultado[0][18]
            pedido_info['ALLIEX'] = {'COTACAO':resultado[0][19],
                                     'VALOR':resultado[0][20],
                                     'PRAZO':resultado[0][21],
                                     'MEDIDAS':resultado[0][22]}
            
            pedido_info['DIRECIONAL'] = {'COTACAO':resultado[0][23],
                                     'VALOR':resultado[0][24],
                                     'PRAZO':resultado[0][25],
                                     'MEDIDAS':resultado[0][26]}
            
            pedido_info['MID'] = {'COTACAO':resultado[0][27],
                                     'VALOR':resultado[0][28],
                                     'PRAZO':resultado[0][29],
                                     'MEDIDAS':resultado[0][30]}
            
            pedido_info['RODONAVES'] = {'COTACAO':resultado[0][31],
                                     'VALOR':resultado[0][32],
                                     'PRAZO':resultado[0][33],
                                     'MEDIDAS':resultado[0][34]}
            
            pedido_info['TRANSREIS'] = {'COTACAO':resultado[0][35],
                                     'VALOR':resultado[0][36],
                                     'PRAZO':resultado[0][37],
                                     'MEDIDAS':resultado[0][38]}
            
            pedido_info['SAOMIGUEL'] = {'COTACAO':resultado[0][39],
                                     'VALOR':resultado[0][40],
                                     'PRAZO':resultado[0][41],
                                     'MEDIDAS':resultado[0][42]}
          
            

        except Exception as erro:
            print(erro)
            pedido_info = {'PEDIDO': '', 'NOME': '', 'CPF': '', 'RUA': '', 'BAIRRO': '', 'CIDADE': '', 'CEP': '', 'UF': '', 'MARCKETPLACE': '', 'TOTALPEDIDO': '', 'VALORFRETE': '', 'FORMAPAGAMENTO': '', 'PRAZOENTREGA': '', 'TABELAFRETE': '', 'PESOTOTAL': '', 'QUANTIDADETOTAL': '', 'CUBAGEM': '', 'DATA': '', 'ALLIEX': {'COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}, 'DIRECIONAL': {'COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}, 'MID': {'COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}, 'RODONAVES': {'COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}, 'TRANSREIS': {'COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''},'SAOMIGUEL': {'COTACAO': '', 'VALOR': '', 'PRAZO': '', 'MEDIDAS': ''}}
        
        finally:
            conexao.close()
            
        return pedido_info
    
    def veridicaPedidoSalvo(PEDIDO):
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f"select * from COTACAO_UTILIZADAS where PEDIDO='{PEDIDO}';")
            resultado = cursor.fetchall()

            
            return resultado
            

        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        finally:
            conexao.close()
            
    def salvaCotacaoNoPedido(TRANSPORTADORA=dict()):
        
        try:
            DATA_AUTAL = strftime("%Y-%m-%d")
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            
            cursor.execute(f"INSERT INTO COTACAO_UTILIZADAS (PEDIDO ,TRANSPORTADORA,VALORFRETE,VALORFRETETRANSPORTADORA,CIDADE,ESTADO,DATA_COTACAO)  VALUES ( '{TRANSPORTADORA['PEDIDO']}','{TRANSPORTADORA['TRANSPOTADORA']}','{TRANSPORTADORA['FRETECLIENTE']}','{TRANSPORTADORA['FRETETRANSPORTADORA']}','{TRANSPORTADORA['CIDADE']}','{TRANSPORTADORA['ESTADO']}','{DATA_AUTAL}')")
            conexao.commit()
            

        except Exception as erro:
            print(f"ERRO BANCO salvaCotacaoNoPedido {erro}")
            pass
        
        finally:
            conexao.close()
            
            
    def alteraTransportdoraNoBanco(TRANSPORTADORA=dict()):
        try:
            DATA_AUTAL = strftime("%Y-%m-%d")
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            
            cursor.execute(f"INSERT INTO COTACAO_UTILIZADAS (PEDIDO ,TRANSPORTADORA,VALORFRETE,VALORFRETETRANSPORTADORA,CIDADE,ESTADO,DATA_COTACAO)  VALUES ( '{TRANSPORTADORA['PEDIDO']}','{TRANSPORTADORA['TRANSPOTADORA']}','{TRANSPORTADORA['FRETECLIENTE']}','{TRANSPORTADORA['FRETETRANSPORTADORA']}','{TRANSPORTADORA['CIDADE']}','{TRANSPORTADORA['ESTADO']}','{DATA_AUTAL}')")
            conexao.commit()
            

        except :
            pass
        
        try:
            DATA_AUTAL = strftime("%Y-%m-%d")
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f"UPDATE COTACAO_UTILIZADAS SET PEDIDO = '{TRANSPORTADORA['PEDIDO']}', TRANSPORTADORA = '{TRANSPORTADORA['TRANSPOTADORA']}',VALORFRETE = '{TRANSPORTADORA['FRETECLIENTE']}',VALORFRETETRANSPORTADORA = '{TRANSPORTADORA['FRETETRANSPORTADORA']}' ,CIDADE ='{TRANSPORTADORA['CIDADE']}' ,ESTADO = '{TRANSPORTADORA['ESTADO']}' , DATA_COTACAO = '{DATA_AUTAL}'   WHERE (PEDIDO = '{TRANSPORTADORA['PEDIDO']}');")
            conexao.commit()

        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        finally:
            conexao.close()
    
    def getInformacoesCotacaoSalva(str):
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(str)
            resultado = cursor.fetchall()   

        except Exception as erro:
            pass
        
        finally:
            conexao.close()
        return resultado
    
    
    def getDataCotacaoSalvas(dataInicial,dataFinal,TRANSPORTADORA,cidade,estado):

        ano = dataInicial[6]+dataInicial[7]+dataInicial[8]+dataInicial[9]
        mes = dataInicial[3]+dataInicial[4]
        dia = dataInicial[0]+dataInicial[1]
        dataInicial = str(f"{ano}-{mes}-{dia}")

        ano = dataFinal[6]+dataFinal[7]+dataFinal[8]+dataFinal[9]
        mes = dataFinal[3]+dataFinal[4]
        dia = dataFinal[0]+dataFinal[1]
        dataFinal = str(f"{ano}-{mes}-{dia}")

        if(cidade):
            cidade = "AND CIDADE = '{}'".format(cidade)
        else:
            cidade = ''
        
        if(estado) :
            estado = "AND ESTADO = '{}'".format(estado)
        else:
            estado = ''
            
            
            
        
        if TRANSPORTADORA == '*':
            sql = str(f"SELECT * FROM COTACAO_UTILIZADAS WHERE DATA_COTACAO BETWEEN '{dataInicial}' AND '{dataFinal}' {cidade} {estado}")
        else:
            sql = str(f"SELECT * FROM COTACAO_UTILIZADAS WHERE DATA_COTACAO BETWEEN '{dataInicial}' AND '{dataFinal}' AND TRANSPORTADORA = '{TRANSPORTADORA}' {cidade} {estado} ")
        
    
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu_02', passwd='xSA]FB+PH7Wl' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(sql)
            resultado = cursor.fetchall()   

        except Exception as erro:
            pass
        
        finally:
            conexao.close()
        return resultado
    
    
    def getValorDoFrete(numero_Pedido):
        try:
            conexao = pymysql.connect(db='wwpneu_01', user='wwpneu_01', passwd='?5CgpDW4+lNf' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f"select * from oc_order_total  where order_id='{numero_Pedido}' ;")
            informacoes = cursor.fetchall()   

        except Exception as erro:
            pass
        
        finally:
            conexao.close()
        
        for opcoes in informacoes:
            if opcoes[2] == 'shipping':
                frete = opcoes[5]
                frete = "%.2f" % frete
        if frete == '':
            frete = 00.00
    
        return frete
    
