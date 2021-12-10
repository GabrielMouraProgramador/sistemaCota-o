# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

import sys
import os
import platform
import time
from typing import Dict

from PySide6 import QtWidgets
from Banco import *
import re
# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////

from modules import ui_popUP
from modules import ui_popUP_Duplicado
from modules import *
from widgets import *

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None

    
class CARREGA_INFORMACOES_BANCO:
    def __init__(self,Pedido) :

        RODONAVES = BUSCATUDO(Pedido,'RODONAVES')
        SAO_MIGUEL = BUSCATUDO(Pedido,'SAO_MIGUEL')
        ALLIEX = BUSCATUDO(Pedido,'ALLIEX')
        TRANSREIS = BUSCATUDO(Pedido,'TRANSREIS')
        MID = BUSCATUDO(Pedido,'MID')
        DIRECIONAL = BUSCATUDO(Pedido,'DIRECIONAL')
        Cliente = BUSCA_INFORMACOES_PEDIDO(Pedido)

        print(RODONAVES)
        self.RODONAVES = RODONAVES
        
        self.SAO_MIGUEL = SAO_MIGUEL
        self.ALLIEX = ALLIEX
        self.TRANSREIS = TRANSREIS
        self.MID = MID
        self.DIRECIONAL = DIRECIONAL
        self.CLIENTE = Cliente
    
    def BucaTransportadora(PEDIDO,DB):
        try:
            conexao = pymysql.connect(db='wwpneu_Cotacao', user='wwpneu', passwd='Goncales@2019' ,host='162.214.74.29' , port=3306)
            cursor = conexao.cursor()
            cursor.execute(f"select * from {DB} where PEDIDO='{PEDIDO}';")
            resultado = cursor.fetchall()
   
            
            if resultado ==():
                resultado = False
            else:
                resultado = True
            return resultado
            

        except Exception as erro:
            print(f"ERRO BANCO {erro}")
            pass
        finally:
            conexao.close()

class popUp_Duplicado(QMainWindow):
    def __init__(self,TRANSPORTADORA):
        QMainWindow.__init__(self)
        self.ui = ui_popUP_Duplicado.Ui_MainWindow_Pop_Up_Duplicado()
        self.ui.setupUi(self)
        global widgets_PopUP_Duplicado
        widgets_PopUP_Duplicado = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        UIFunctions.uiDefinitions(self)
        
        self.transportadora = TRANSPORTADORA
        widgets_PopUP_Duplicado.label_2.setText(QCoreApplication.translate("MainWindow", u"   Pedido salvo em outra Transportadora  ", None))
        widgets_PopUP_Duplicado.label.setText(QCoreApplication.translate("MainWindow", u"   Deseja Altera para para {} ??".format(self.transportadora['TRANSPOTADORA']), None))   
        widgets_PopUP_Duplicado.pushButton.clicked.connect(self.buttonClick)
        widgets_PopUP_Duplicado.pushButton_3.clicked.connect(self.buttonClick)


    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        TRANSPORTADORA = self.transportadora 

        if btnName == "pushButton":
            alteraTransportdoraNoBanco(TRANSPORTADORA)
            self.hide()
            Sucesso = Pop_Up()
            Sucesso.show()
            MainWindow.limpatelacotacoes()
        
        elif btnName == "pushButton_3":
            print('entrou')
            MainWindow.limpatelacotacoes()
            self.hide()
        
        print(f'Button "{btnName}" pressed!')
            

class Pop_Up(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_popUP.Ui_MainWindow_Pop_Up()
        self.ui.setupUi(self)
        widgets_PopUp = self.ui
        UIFunctions.uiDefinitions(self)
        MainWindow.limpatelacotacoes()

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "Pneus Tyres"
        description = "Pneus Tyres"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # CHAMA POPUP
        # ///////////////////////////////////////////////////////////////
        self.PopUp = Pop_Up()
        
        
        # BUTTONS CICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.pushButton.clicked.connect(self.BuscaPedido)
        widgets.pushButton_30.clicked.connect(self.salvaRodonaves)#Rodonaves
        widgets.pushButton_31.clicked.connect(self.salvaSaoMiguel)#Sao Miguel 
        widgets.pushButton_32.clicked.connect(self.salvaAlliex)#Alliex
        widgets.pushButton_33.clicked.connect(self.salvaTransreis)#Transreis
        widgets.pushButton_34.clicked.connect(self.salvaMID)#Mid
        widgets.pushButton_35.clicked.connect(self.salvaDirecional)#Mid



        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        #widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        #widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

        # DESABILITA WIDGETS
        # ///////////////////////////////////////////////////////////////
        MainWindow.DesabilitaWidgets()
        
    
        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.home)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
    
    def melhorValor(Pedido,INFORMACOES):
        RODONAVES = INFORMACOES.RODONAVES
        SAO_MIGUEL = INFORMACOES.SAO_MIGUEL
        ALLIEX = INFORMACOES.ALLIEX
        TRANSREIS = INFORMACOES.TRANSREIS
        DIRECIONAL = INFORMACOES.DIRECIONAL
        MID = INFORMACOES.MID
        
 

        valorMid = str(MID[3]).replace(',','.')
        valorDirecional = str(DIRECIONAL[3]).replace(',','.')
        valorRte = str(RODONAVES[3]).replace(',','.')
        valorSaoMiguel = str(SAO_MIGUEL[3]).replace(',','.')
        valorAlliex = str(ALLIEX[3]).replace(',','.')
        valorTransreis = str(TRANSREIS[3]).replace(',','.')

        lista_valores = list()

        try:
            valorMid = float(valorMid)
            lista_valores.append(valorMid)
        except:
            pass
        
        try:
            valorDirecional = float(valorDirecional)
            lista_valores.append(valorDirecional)
        except:
            pass
        
        try:
            valorRte = float(valorRte)
            lista_valores.append(valorRte)
        except:
            pass

        try:
            valorSaoMiguel = float(valorSaoMiguel)
            lista_valores.append(valorSaoMiguel)
        except:
            pass
        try:
            valorAlliex = float(valorAlliex)
            lista_valores.append(valorAlliex)
        except:
            pass
        
        try:
            valorTransreis = float(valorTransreis)
            lista_valores.append(valorTransreis)
        except:
            pass
        listaOrdenada = list()
        for valores in lista_valores:
            if valores > 0:
                listaOrdenada.append(valores)
                



        
        listaOrdenada = sorted(listaOrdenada)
        print(listaOrdenada)

        if str(listaOrdenada[0]) == str(valorTransreis):
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(valorTransreis), None)) #cotacao

        
        if str(listaOrdenada[0]) == str(valorAlliex):
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(valorAlliex), None)) #cotacao

        if str(listaOrdenada[0]) == str(valorSaoMiguel):
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Expresso S\u00e3o Miguel", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(82, 153, 0);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(valorSaoMiguel), None)) #cotacao

        if str(listaOrdenada[0]) == str(valorRte):
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(valorRte), None)) #cotacao

        if str(listaOrdenada[0]) == str(valorDirecional):
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Direcional", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(valorDirecional), None)) #cotacao

        if str(listaOrdenada[0]) == str(valorMid):
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Mid", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(valorMid), None)) #cotacao
        
    def melhorPrazo(Pedido,INFORMACOES):
        RODONAVES = INFORMACOES.RODONAVES
        SAO_MIGUEL = INFORMACOES.SAO_MIGUEL
        ALLIEX = INFORMACOES.ALLIEX
        TRANSREIS = INFORMACOES.TRANSREIS
        DIRECIONAL = INFORMACOES.DIRECIONAL
        MID = INFORMACOES.MID
        
 

        prazoMid = MID[4]
        prazoDirecional = DIRECIONAL[4]
        prazoRte = RODONAVES[4]
        prazoSaoMiguel = SAO_MIGUEL[4]
        prazoAlliex = ALLIEX[4]
        prazoTransreis = TRANSREIS[4]

        lista_prazo = list()

        if prazoMid in '12345678910111213141516171819202122232425262728293031323334353637383940':
            prazoMid = int(prazoMid)
            lista_prazo.append(prazoMid)
        
        if prazoDirecional in '12345678910111213141516171819202122232425262728293031323334353637383940':
            prazoDirecional = int(prazoDirecional)
            lista_prazo.append(prazoDirecional)
        
        if prazoRte in '12345678910111213141516171819202122232425262728293031323334353637383940':
            prazoRte = int(prazoRte)
            lista_prazo.append(prazoRte)
        
        if prazoSaoMiguel in '12345678910111213141516171819202122232425262728293031323334353637383940':
            prazoSaoMiguel = int(prazoSaoMiguel)
            lista_prazo.append(prazoSaoMiguel)
        
        if prazoAlliex in '12345678910111213141516171819202122232425262728293031323334353637383940':
            prazoAlliex = int(prazoAlliex)
            lista_prazo.append(prazoAlliex)
        
        if prazoTransreis in '12345678910111213141516171819202122232425262728293031323334353637383940':
            prazoTransreis = int(prazoTransreis)
            lista_prazo.append(prazoTransreis)
        
        lista_sem_0 = list()
        for dias in lista_prazo:
            if dias != 0:
                lista_sem_0.append(dias)


        listaOrdenada = sorted(lista_sem_0)

        if str(listaOrdenada[0]) == str(prazoTransreis):
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(prazoTransreis), None)) #cotacao

        
        if str(listaOrdenada[0]) == str(prazoAlliex):
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(prazoAlliex), None)) #cotacao

        if str(listaOrdenada[0]) == str(prazoSaoMiguel):
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Expresso S\u00e3o Miguel", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(82, 153, 0);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(prazoSaoMiguel), None)) #cotacao

        if str(listaOrdenada[0]) == str(prazoRte):
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(prazoRte), None)) #cotacao

        if str(listaOrdenada[0]) == str(prazoDirecional):
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Direcional", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(prazoDirecional), None)) #cotacao

        if str(listaOrdenada[0]) == str(prazoMid):
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Mid", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(prazoMid), None)) #cotacao
        
    def preenche_Cliente(Pedido,INFORMACOES):
        Cliente = INFORMACOES.CLIENTE
        try:
            widgets.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(Cliente[1]), None)) #NOME
        except:
            widgets.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format('Cliente'), None)) #NOME
        try:
            widgets.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} - {}   Tabela: {}".format(Cliente[7], Cliente[6], Cliente[12]), None)) #PRODUTO
        except:
            widgets.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} ".format('Endereco'), None)) #PRODUTO
        try:
            widgets.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(Cliente[9]), None)) #FRETE
        except:
            widgets.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(''), None)) #FRETE
        try:
            widgets.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(Cliente[8]), None)) #VALOR PEDIDO
        except:
            widgets.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(''), None)) #VALOR PEDIDO
        try:
            widgets.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(Cliente[10]), None)) #VALOR PEDIDO
        except:
            widgets.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format('0'), None)) #VALOR PEDIDO

    def localizaMelhorcotacao(Pedido,INFORMACOES):
        RODONAVES = INFORMACOES.RODONAVES
        SAO_MIGUEL = INFORMACOES.SAO_MIGUEL
        ALLIEX = INFORMACOES.ALLIEX
        TRANSREIS = INFORMACOES.TRANSREIS
        MID = INFORMACOES.MID

        mid_valor = MainWindow.trata_valor(MID[3])
        rte_valor = MainWindow.trata_valor(RODONAVES[3])
        sm_valor = MainWindow.trata_valor(SAO_MIGUEL[3])
        alx_valor = MainWindow.trata_valor(ALLIEX[3])
        trs_valor = MainWindow.trata_valor(TRANSREIS[3])


        precos = [mid_valor,rte_valor,sm_valor,alx_valor,trs_valor]

        new_list = list()
        for preco in precos:
            if preco > 0 :
                new_list.append(preco)
            else:
                pass

        menor = new_list[0]
        for i in new_list:
            if i < menor:
                menor = i

        if mid_valor == menor:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MID", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(mid_valor), None)) 
        
        elif rte_valor == menor:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Rodonaves", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(rte_valor), None)) 
            
        elif sm_valor == menor:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Expresso S\u00e3o Miguel", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(82, 153, 0);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(sm_valor), None)) 
        
    
        elif alx_valor == menor:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Alliex", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(alx_valor), None)) 

        elif trs_valor == menor:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transreis", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(trs_valor), None))
      
    def trata_valor(valor):
       valor = str(valor).replace(',','.')
       valor = float(valor)
       return valor
    
    def salvaRodonaves(self):
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['COD_TRANSPORTADORA'] = '09'
        TRANSPORTADORA['TRANSPOTADORA'] = 'RODONAVES'
        MainWindow.verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA)
            
    def limpatelacotacoes():
        widgets.lineEdit_3.setStyleSheet(u"")
        widgets.lineEdit_2.setStyleSheet(u"")
        widgets.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #PRODUTO
        widgets.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #FRETE
        widgets.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #VALOR PEDIDO
        widgets.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #VALOR PEDIDO
        widgets.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u" ", None)) #VALOR PEDIDO
        widgets.lineEdit_256.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #cotacao
        widgets.lineEdit_257.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #valor
        widgets.lineEdit_258.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Prazo
        widgets.lineEdit_259.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cidade
        widgets.lineEdit_261.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Medidas
        widgets.lineEdit_262.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cubagem
        widgets.lineEdit_260.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_248.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #cotacao
        widgets.lineEdit_249.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #valor
        widgets.lineEdit_250.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Prazo
        widgets.lineEdit_251.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cidade
        widgets.lineEdit_253.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Medidas
        widgets.lineEdit_254.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cubagem
        widgets.lineEdit_252.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_240.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #cotacao
        widgets.lineEdit_241.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #valor
        widgets.lineEdit_242.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Prazo
        widgets.lineEdit_243.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cidade
        widgets.lineEdit_245.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Medidas
        widgets.lineEdit_246.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cubagem
        widgets.lineEdit_244.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_232.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #cotacao
        widgets.lineEdit_233.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #valor
        widgets.lineEdit_234.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Prazo
        widgets.lineEdit_235.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cidade
        widgets.lineEdit_237.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Medidas
        widgets.lineEdit_238.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cubagem
        widgets.lineEdit_236.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_224.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #cotacao
        widgets.lineEdit_225.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #valor
        widgets.lineEdit_226.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Prazo
        widgets.lineEdit_227.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cidade
        widgets.lineEdit_229.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Medidas
        widgets.lineEdit_230.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Cubagem
        widgets.lineEdit_228.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_264.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_265.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_266.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_267.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_268.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_269.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        widgets.lineEdit_270.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #Quantidade
        
    def salvaSaoMiguel(self):
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['COD_TRANSPORTADORA'] = '64'
        TRANSPORTADORA['TRANSPOTADORA'] = 'SAO MIGUEL'

        MainWindow.verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA)
         
    def salvaAlliex(self):
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['COD_TRANSPORTADORA'] = '92'
        TRANSPORTADORA['TRANSPOTADORA'] = 'ALLIEX'

        MainWindow.verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA)
    
    def salvaMID(self):
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['COD_TRANSPORTADORA'] = '80'
        TRANSPORTADORA['TRANSPOTADORA'] = 'MID'

        MainWindow.verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA)
    
    def salvaTransreis(self):
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['COD_TRANSPORTADORA'] = '90'
        TRANSPORTADORA['TRANSPOTADORA'] = 'TRANSREIS'
        MainWindow.verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA)
    
    def salvaDirecional(self):
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['COD_TRANSPORTADORA'] = '96'
        TRANSPORTADORA['TRANSPOTADORA'] = 'Direcional'
        MainWindow.verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA)
    
    def verifica_e_altera_cotacao_salva(Pedido,TRANSPORTADORA):
        if Pedido == '':
            pass
        else:
            verifica = VeridicaPedidoSalvo(Pedido)
            if verifica == ():
                SalvaCotacaoNoPedido(TRANSPORTADORA)
                sucesso = Pop_Up()
                sucesso.show()      
            else:
                duplicado = popUp_Duplicado(TRANSPORTADORA)
                duplicado.show()

    def BuscaPedido(self):
        Pedido = widgets.lineEdit.text()
        INFORMACOES = CARREGA_INFORMACOES_BANCO(Pedido)
        MainWindow.preenche_Cliente(Pedido,INFORMACOES)
        MainWindow.preencheCotacaoRodonaves(Pedido,INFORMACOES)
        MainWindow.preencheCotacaoSaoMiguel(Pedido,INFORMACOES)
        MainWindow.preencheCotacaoAlliex(Pedido,INFORMACOES)
        MainWindow.preencheCotacaoTransReis(Pedido,INFORMACOES)
        MainWindow.preencheCotacaoMid(Pedido,INFORMACOES)
        MainWindow.preencheCotacaoDirecional(Pedido,INFORMACOES)
        MainWindow.melhorPrazo(Pedido,INFORMACOES)
        MainWindow.melhorValor(Pedido,INFORMACOES)
        
    def preencheCotacaoRodonaves(Pedido,INFORMACOES):
        RODONAVES = INFORMACOES.RODONAVES
        try:
            widgets.lineEdit_224.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(RODONAVES[2]), None)) #cotacao
        except:
            widgets.lineEdit_224.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #cotacao
        try:
            widgets.lineEdit_225.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(RODONAVES[3]), None)) #valor
        except:
            widgets.lineEdit_225.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #valor
        try:
            widgets.lineEdit_226.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(RODONAVES[4]), None)) #Prazo
        except:
            widgets.lineEdit_226.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(''), None)) #Prazo
        try:
            widgets.lineEdit_227.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} {}".format(RODONAVES[6],RODONAVES[7]), None)) #Cidade
        except:
            widgets.lineEdit_227.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cidade
        try:
            widgets.lineEdit_229.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(RODONAVES[12]), None)) #Medidas
        except:
            widgets.lineEdit_229.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Medidas
        try:
            widgets.lineEdit_230.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(RODONAVES[11]), None)) #Cubagem
        except:
            widgets.lineEdit_230.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cubagem
        try:
            widgets.lineEdit_228.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(RODONAVES[9]), None)) #Quantidade
        except:
            widgets.lineEdit_228.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Quantidade
        
    def preencheCotacaoSaoMiguel(Pedido,INFORMACOES):
        SAO_MIGUEL = INFORMACOES.SAO_MIGUEL
        try:
            widgets.lineEdit_232.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[2]), None)) #cotacao
        except:
            widgets.lineEdit_232.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #cotacao
        try:
            widgets.lineEdit_233.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[3]), None)) #valor
        except:
            widgets.lineEdit_233.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #valor
        try:
            widgets.lineEdit_234.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(SAO_MIGUEL[4]), None)) #Prazo
        except:
            widgets.lineEdit_234.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(''), None)) #Prazo
        try:
            widgets.lineEdit_235.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} {}".format(SAO_MIGUEL[6],SAO_MIGUEL[7]), None)) #Cidade
        except:
            widgets.lineEdit_235.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cidade
        try:
            widgets.lineEdit_237.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[12]), None)) #Medidas
        except:
            widgets.lineEdit_237.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Medidas
        try:
            widgets.lineEdit_238.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[11]), None)) #Cubagem
        except:
            widgets.lineEdit_238.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cubagem
        try:
            widgets.lineEdit_236.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[9]), None)) #Quantidade
        except:
            widgets.lineEdit_236.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Quantidade
    
    def preencheCotacaoAlliex(Pedido,INFORMACOES):
        SAO_MIGUEL = INFORMACOES.ALLIEX
        try:
            widgets.lineEdit_240.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[2]), None)) #cotacao
        except:
            widgets.lineEdit_240.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #cotacao
        try:
            widgets.lineEdit_241.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[3]), None)) #valor
        except:
            widgets.lineEdit_241.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #valor
        try:
            widgets.lineEdit_242.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(SAO_MIGUEL[4]), None)) #Prazo
        except:
            widgets.lineEdit_242.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(''), None)) #Prazo
        try:
            widgets.lineEdit_243.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} {}".format(SAO_MIGUEL[6],SAO_MIGUEL[7]), None)) #Cidade
        except:
            widgets.lineEdit_243.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cidade
        try:
            widgets.lineEdit_245.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[12]), None)) #Medidas
        except:
            widgets.lineEdit_245.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Medidas
        try:
            widgets.lineEdit_246.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[11]), None)) #Cubagem
        except:
            widgets.lineEdit_246.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cubagem
        try:
            widgets.lineEdit_244.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[9]), None)) #Quantidade
        except:
            widgets.lineEdit_244.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Quantidade

    def preencheCotacaoTransReis(Pedido,INFORMACOES):
        SAO_MIGUEL = INFORMACOES.TRANSREIS
        try:
            widgets.lineEdit_248.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[2]), None)) #cotacao
        except:
            widgets.lineEdit_248.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #cotacao
        try:
            widgets.lineEdit_249.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[3]), None)) #valor
        except:
            widgets.lineEdit_249.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #valor
        try:
            widgets.lineEdit_250.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(SAO_MIGUEL[4]), None)) #Prazo
        except:
            widgets.lineEdit_250.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(''), None)) #Prazo
        try:
            widgets.lineEdit_251.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} {}".format(SAO_MIGUEL[6],SAO_MIGUEL[7]), None)) #Cidade
        except:
            widgets.lineEdit_251.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cidade
        try:
            widgets.lineEdit_253.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[12]), None)) #Medidas
        except:
            widgets.lineEdit_253.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Medidas
        try:
            widgets.lineEdit_254.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[11]), None)) #Cubagem
        except:
            widgets.lineEdit_254.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cubagem
        try:
            widgets.lineEdit_252.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[9]), None)) #Quantidade
        except:
            widgets.lineEdit_252.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Quantidade
    
    def preencheCotacaoMid(Pedido,INFORMACOES):
        SAO_MIGUEL = INFORMACOES.MID
        try:
            widgets.lineEdit_256.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[2]), None)) #cotacao
        except:
            widgets.lineEdit_256.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #cotacao
        try:
            widgets.lineEdit_257.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[3]), None)) #valor
        except:
            widgets.lineEdit_257.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #valor
        try:
            widgets.lineEdit_258.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(SAO_MIGUEL[4]), None)) #Prazo
        except:
            widgets.lineEdit_258.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(''), None)) #Prazo
        try:
            widgets.lineEdit_259.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} {}".format(SAO_MIGUEL[6],SAO_MIGUEL[7]), None)) #Cidade
        except:
            widgets.lineEdit_259.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cidade
        try:
            widgets.lineEdit_261.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[12]), None)) #Medidas
        except:
            widgets.lineEdit_261.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Medidas
        try:
            widgets.lineEdit_262.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[11]), None)) #Cubagem
        except:
            widgets.lineEdit_262.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cubagem
        try:
            widgets.lineEdit_260.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[9]), None)) #Quantidade
        except:
            widgets.lineEdit_260.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Quantidade

    def preencheCotacaoDirecional(Pedido,INFORMACOES):
        SAO_MIGUEL = INFORMACOES.DIRECIONAL
        try:
            widgets.lineEdit_264.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[2]), None)) #cotacao
        except:
            widgets.lineEdit_264.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #cotacao
        try:
            widgets.lineEdit_265.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[3]), None)) #valor
        except:
            widgets.lineEdit_265.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #valor
        try:
            widgets.lineEdit_266.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(SAO_MIGUEL[4]), None)) #Prazo
        except:
            widgets.lineEdit_266.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(''), None)) #Prazo
        try:
            widgets.lineEdit_267.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} {}".format(SAO_MIGUEL[6],SAO_MIGUEL[7]), None)) #Cidade
        except:
            widgets.lineEdit_267.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cidade
        try:
            widgets.lineEdit_269.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[12]), None)) #Medidas
        except:
            widgets.lineEdit_269.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Medidas
        try:
            widgets.lineEdit_270.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[11]), None)) #Cubagem
        except:
            widgets.lineEdit_270.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Cubagem
        try:
            widgets.lineEdit_268.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(SAO_MIGUEL[9]), None)) #Quantidade
        except:
            widgets.lineEdit_268.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None)) #Quantidade

    def DesabilitaWidgets():
        widgets.lineEdit_7.setDisabled(True)
        widgets.lineEdit_5.setDisabled(True)
        widgets.lineEdit_4.setDisabled(True)
        widgets.lineEdit_9.setDisabled(True)
        widgets.lineEdit_8.setDisabled(True)
        widgets.lineEdit_223.setDisabled(True)
        widgets.lineEdit_224.setDisabled(True)
        widgets.lineEdit_225.setDisabled(True)
        widgets.lineEdit_226.setDisabled(True)
        widgets.lineEdit_227.setDisabled(True)
        widgets.lineEdit_228.setDisabled(True)
        widgets.lineEdit_230.setDisabled(True)
        widgets.lineEdit_231.setDisabled(True)
        widgets.lineEdit_232.setDisabled(True)
        widgets.lineEdit_233.setDisabled(True)
        widgets.lineEdit_234.setDisabled(True)
        widgets.lineEdit_235.setDisabled(True)
        widgets.lineEdit_229.setDisabled(True)
        widgets.lineEdit_236.setDisabled(True)
        widgets.lineEdit_237.setDisabled(True)
        widgets.lineEdit_238.setDisabled(True)
        widgets.lineEdit_239.setDisabled(True)
        widgets.lineEdit_240.setDisabled(True)
        widgets.lineEdit_241.setDisabled(True)
        widgets.lineEdit_242.setDisabled(True)
        widgets.lineEdit_243.setDisabled(True)
        widgets.lineEdit_244.setDisabled(True)
        widgets.lineEdit_245.setDisabled(True)
        widgets.lineEdit_246.setDisabled(True)
        widgets.lineEdit_247.setDisabled(True)
        widgets.lineEdit_248.setDisabled(True)
        widgets.lineEdit_249.setDisabled(True)
        widgets.lineEdit_250.setDisabled(True)
        widgets.lineEdit_251.setDisabled(True)
        widgets.lineEdit_252.setDisabled(True)
        widgets.lineEdit_253.setDisabled(True)
        widgets.lineEdit_254.setDisabled(True)
        widgets.lineEdit_255.setDisabled(True)
        widgets.lineEdit_256.setDisabled(True)
        widgets.lineEdit_257.setDisabled(True)
        widgets.lineEdit_258.setDisabled(True)
        widgets.lineEdit_259.setDisabled(True)
        widgets.lineEdit_260.setDisabled(True)
        widgets.lineEdit_261.setDisabled(True)
        widgets.lineEdit_262.setDisabled(True)
        widgets.lineEdit_263.setDisabled(True)
        widgets.lineEdit_264.setDisabled(True)
        widgets.lineEdit_265.setDisabled(True)
        widgets.lineEdit_266.setDisabled(True)
        widgets.lineEdit_267.setDisabled(True)
        widgets.lineEdit_268.setDisabled(True)
        widgets.lineEdit_269.setDisabled(True)
        widgets.lineEdit_270.setDisabled(True)
        widgets.lineEdit_3.setDisabled(True)
        widgets.lineEdit_6.setDisabled(True)
        widgets.lineEdit_10.setDisabled(True)

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.home)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.widgets)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.new_page) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

        if btnName == "btn_save":
            print("Save BTN clicked!")

        # PRINT BTN NAME
        print(f'Button "{btnName}" pressed!')


    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

        # PRINT MOUSE EVENTS
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()

    sys.exit(app.exec_())
