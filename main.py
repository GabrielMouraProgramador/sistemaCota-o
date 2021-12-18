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

from io import BufferedRandom
import sys
import os
import platform
from PyQt6 import QtWidgets
from PyQt6 import *
from PyQt6 import QtGui
from PySide6 import *
from PySide6 import QtGui



# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from modules import ui_popUP
from modules import ui_popUP_Duplicado
from banco.consultas import Banco
import pandas as pd
from controle.gerar_cotacao import *
from time import gmtime, strftime

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
widgets_PopUP_Duplicado = None
lista_produtos = []

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
        TransportadoraSalva = Banco.getInformacoesCotacaoSalva(f"SELECT TRANSPORTADORA FROM `COTACAO_UTILIZADAS` WHERE PEDIDO={self.transportadora['PEDIDO']}")
        
        widgets_PopUP_Duplicado.label_2.setText(QCoreApplication.translate("MainWindow", u"   Pedido vinculado a transportadora {} ".format(TransportadoraSalva[0][0]), None))
        widgets_PopUP_Duplicado.label.setText(QCoreApplication.translate("MainWindow", u"   Deseja Altera para para {} ??".format(self.transportadora['TRANSPOTADORA']), None))   
        widgets_PopUP_Duplicado.pushButton.clicked.connect(self.buttonClick)
        widgets_PopUP_Duplicado.pushButton_3.clicked.connect(self.buttonClick)


    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()
        
        TRANSPORTADORA = self.transportadora 

        if btnName == "pushButton":
            Banco.alteraTransportdoraNoBanco(TRANSPORTADORA)
            self.hide()
            Sucesso = Pop_Up()
            Sucesso.show()
                   
        elif btnName == "pushButton_3":
            self.hide()
        print(f'Button "{btnName}" pressed!')
            

class Pop_Up(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_popUP.Ui_MainWindow_Pop_Up1()
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
        global lista_produtos 

        lista_produtos = list()
        widgets = self.ui

        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        Settings.ENABLE_CUSTOM_TITLE_BAR = True

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "PneusTyres"
        description = "TRANSTYRES - logística Pneus tyres."
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)
        
        
        

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        #widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////

        # LEFT MENUS
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_widgets.clicked.connect(self.buttonClick)
        widgets.btn_new.clicked.connect(self.buttonClick)
        widgets.btn_share.clicked.connect(self.buttonClick)
        
        
        #GERAR COTACAO
        widgets.gerar_cotacao_btn.clicked.connect(self.gerarCotacao)
        widgets.pushButton_2.clicked.connect(self.tabela_cubagem)
        #widgets.pushButton_4.clicked.connect(self.lemparTelaCotacao)
       
        
        #BUSCAR COTACAO
        widgets.pushButton.clicked.connect(self.buscarCotacao)
        widgets.pushButton_5.clicked.connect(self.salvaRodonaves)
        widgets.pushButton_32.clicked.connect(self.salvaAlliex)
        widgets.pushButton_33.clicked.connect(self.salvaTransreis)
        widgets.pushButton_34.clicked.connect(self.salvaMID)
        widgets.pushButton_35.clicked.connect(self.salvaDirecional)
        
        #RELATORIO COTAXAO
        widgets.pushButton_7.clicked.connect(self.gerarRelatorioCotacoes)
        widgets.pushButton_6.clicked.connect(self.salvaRelatorio)
    

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SHOW APP
        # ///////////////////////////////////////////////////////////////
        self.show()

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
        widgets.stackedWidget.setCurrentWidget(widgets.Inicio)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    
# ///////////////////////////////////////////////////
# ////////////// # BUSCAR COTACAO  //////////////////
# ///////////////////////////////////////////////////
    def buscarCotacao(self):
        numeroPedido = widgets.lineEdit.text()
        informacoes = Banco.getInformacoesCotacao(numeroPedido)
        self.info = informacoes
        print(informacoes)
        melhor_valor = MainWindow.melhorValor_busca(informacoes)
        melhor_prazo = MainWindow.melhorPrazo_busca(informacoes)
        
       
        if melhor_valor['TRANSPORTADORA'] == 'RODONAVES':
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
        
        elif melhor_valor['TRANSPORTADORA'] == 'ALLIEX':
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
        
        elif melhor_valor['TRANSPORTADORA'] == 'MID':
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Mid", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
            
        elif melhor_valor['TRANSPORTADORA'] == 'DIRECIONAL':
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Direcional", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
            
        elif melhor_valor['TRANSPORTADORA'] == 'TRANSREIS':
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
        else:
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora ", None))
            widgets.lineEdit_2.setStyleSheet(u"")
            widgets.lineEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(0), None)) #cotacao
        
        
        if melhor_prazo['TRANSPORTADORA'] == 'RODONAVES':
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        
        elif melhor_prazo['TRANSPORTADORA'] == 'ALLIEX':
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        
        elif melhor_prazo['TRANSPORTADORA'] == 'MID':
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Mid", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
            
        elif melhor_prazo['TRANSPORTADORA'] == 'DIRECIONAL':
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Direcional", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
            
        elif melhor_prazo['TRANSPORTADORA'] == 'TRANSREIS':
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        else:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora ", None))
            widgets.lineEdit_3.setStyleSheet(u"")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(0), None)) #cotacao
        
        #
        widgets.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['NOME']), None))
        widgets.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['PRAZOENTREGA']), None))
        widgets.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['VALORFRETE']), None))
        widgets.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['TOTALPEDIDO']), None))
        widgets.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CPF']), None))
        widgets.lineEdit_45.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['TABELAFRETE']), None))
        
        #RODONAVES
        widgets.lineEdit_227.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_228.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_230.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_224.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['RODONAVES']['COTACAO']), None))
        widgets.lineEdit_225.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(str(informacoes['RODONAVES']['VALOR'])).replace('.',','), None))
        widgets.lineEdit_226.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['RODONAVES']['PRAZO']), None))
        widgets.lineEdit_229.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['RODONAVES']['MEDIDAS']), None))
        
        #ALLIEX
        widgets.lineEdit_243.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_244.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_246.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_240.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['ALLIEX']['COTACAO']), None))
        widgets.lineEdit_241.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(str(informacoes['ALLIEX']['VALOR']).replace('.',',')), None))
        widgets.lineEdit_242.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['ALLIEX']['PRAZO']), None))
        widgets.lineEdit_245.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['ALLIEX']['MEDIDAS']), None))
        
        #TRANSREIS
        widgets.lineEdit_251.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_252.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_254.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_248.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['TRANSREIS']['COTACAO']), None))
        widgets.lineEdit_249.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(str(informacoes['TRANSREIS']['VALOR']).replace('.',',')), None))
        widgets.lineEdit_250.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['TRANSREIS']['PRAZO']), None))
        widgets.lineEdit_253.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['TRANSREIS']['MEDIDAS']), None))
        
        #MID
        widgets.lineEdit_259.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_260.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_262.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_256.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['MID']['COTACAO']), None))
        widgets.lineEdit_257.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(str(informacoes['MID']['VALOR']).replace('.',',')), None))
        widgets.lineEdit_258.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['MID']['PRAZO']), None))
        widgets.lineEdit_261.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['MID']['MEDIDAS']), None))
        
        #DIRECIONAL
        widgets.lineEdit_267.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_268.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_270.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_264.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['DIRECIONAL']['COTACAO']), None))
        widgets.lineEdit_265.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(str(informacoes['DIRECIONAL']['VALOR']).replace('.',',')), None))
        widgets.lineEdit_266.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['DIRECIONAL']['PRAZO']), None))
        widgets.lineEdit_269.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['DIRECIONAL']['MEDIDAS']), None))
    
    def melhorValor_busca(cotacoes):
        rte = cotacoes['RODONAVES']['VALOR']
        alliex = cotacoes['ALLIEX']['VALOR']
        mid = cotacoes['MID']['VALOR']
        direcional = cotacoes['DIRECIONAL']['VALOR']
        transreis = cotacoes['TRANSREIS']['VALOR']
        
        try:
            rte = float(rte)
        except:
            rte = 10000
    
        try:
            alliex = float(alliex)
        except:
            alliex = 10000
            
        try:
            mid = float(mid)
        except:
            mid = 10000
            
        try:
            direcional = float(direcional)
        except:
            direcional = 10000
            
        try:
            transreis = float(transreis)
        except:
            transreis = 10000
            
        lista_prazos = list()
        lista_prazos.append(rte)
        lista_prazos.append(alliex)
        lista_prazos.append(mid)
        lista_prazos.append(direcional)
        lista_prazos.append(transreis)
      
        lista_organizada = sorted(lista_prazos, key=int)
        
        
        nova_lista = list()
        for valoreis in  lista_organizada:
            if valoreis > 0:
                nova_lista.append(valoreis)
                
        lista_organizada =  nova_lista
        lista_organizada = sorted(lista_organizada, key=int)
                
        if lista_organizada[0] == rte:
            retorno = {'TRANSPORTADORA': 'RODONAVES','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == alliex:
            retorno = {'TRANSPORTADORA': 'ALLIEX','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == mid:
            retorno = {'TRANSPORTADORA': 'MID','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == direcional:
            retorno = {'TRANSPORTADORA': 'DIRECIONAL','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == transreis:
            retorno = {'TRANSPORTADORA': 'TRANSREIS','VALOR': lista_organizada[0]}
        else:
            retorno = {'TRANSPORTADORA': '','VALOR': 0}
            
        return retorno
    
    def melhorPrazo_busca(cotacoes):
        rte = cotacoes['RODONAVES']['PRAZO']
        if rte == 0 :
            rte = 1000
        alliex = cotacoes['ALLIEX']['PRAZO']
        if alliex == 0 :
            alliex = 1000
        mid = cotacoes['MID']['PRAZO']
        if mid == 0 :
            mid = 1000
        direcional = cotacoes['DIRECIONAL']['PRAZO']
        if direcional == 0 :
            direcional = 1000
        transreis = cotacoes['TRANSREIS']['PRAZO']
        if transreis == 0 :
            transreis = 1000
        
        try:
            rte = int(rte)
        except:
            rte = 100
    
        try:
            alliex = int(alliex)
        except:
            alliex = 100
            
        try:
            mid = int(mid)
        except:
            mid = 100
            
        try:
            direcional = int(direcional)
        except:
            direcional = 100
            
        try:
            transreis = int(transreis)
        except:
            transreis = 100
            
        lista_prazos = list()
        lista_prazos.append(rte)
        lista_prazos.append(alliex)
        lista_prazos.append(mid)
        lista_prazos.append(direcional)
        lista_prazos.append(transreis)
      
        lista_organizada = sorted(lista_prazos, key=int)
        
        if lista_organizada[0] == rte:
            retorno = {'TRANSPORTADORA': 'RODONAVES','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == alliex:
            retorno = {'TRANSPORTADORA': 'ALLIEX','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == mid:
            retorno = {'TRANSPORTADORA': 'MID','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == direcional:
            retorno = {'TRANSPORTADORA': 'DIRECIONAL','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == transreis:
            retorno = {'TRANSPORTADORA': 'TRANSREIS','PRAZO': lista_organizada[0]}
        else:
            retorno = {'TRANSPORTADORA': '','PRAZO': 0}
            
        return retorno
    
    def verificaCotacaSalvas(Pedido,TRANSPORTADORA):
        if Pedido == '':
            pass
        
        else:
            verifica = Banco.veridicaPedidoSalvo(Pedido)
            if verifica == ():
                Banco.salvaCotacaoNoPedido(TRANSPORTADORA)
                sucesso = Pop_Up()
                sucesso.show()      
            else:
                duplicado = popUp_Duplicado(TRANSPORTADORA)
                duplicado.show()

    def salvaAlliex(self):
        informacoes = self.info
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = 'ALLIEX'
        TRANSPORTADORA['FRETECLIENTE'] = informacoes['VALORFRETE']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['ALLIEX']['VALOR']
        TRANSPORTADORA['CIDADE'] = informacoes['CIDADE']
        TRANSPORTADORA['ESTADO'] = informacoes['UF']


        MainWindow.verificaCotacaSalvas(Pedido,TRANSPORTADORA)
    
    def salvaMID(self):
        Pedido= widgets.lineEdit.text()
        informacoes = self.info
        
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = 'MID'
        TRANSPORTADORA['FRETECLIENTE'] = informacoes['VALORFRETE']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['MID']['VALOR']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['MID']['VALOR']
        TRANSPORTADORA['CIDADE'] = informacoes['CIDADE']
        TRANSPORTADORA['ESTADO'] = informacoes['UF']


        MainWindow.verificaCotacaSalvas(Pedido,TRANSPORTADORA)
    
    def salvaTransreis(self):
        Pedido= widgets.lineEdit.text()
        informacoes = self.info
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = 'TRANSREIS'
        TRANSPORTADORA['FRETECLIENTE'] = informacoes['VALORFRETE']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['TRANSREIS']['VALOR']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['TRANSREIS']['VALOR']
        TRANSPORTADORA['CIDADE'] = informacoes['CIDADE']
        TRANSPORTADORA['ESTADO'] = informacoes['UF']
        
        MainWindow.verificaCotacaSalvas(Pedido,TRANSPORTADORA)
    
    def salvaDirecional(self):
        informacoes = self.info
        Pedido= widgets.lineEdit.text()
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = 'DIRECIONAL'
        TRANSPORTADORA['FRETECLIENTE'] = informacoes['VALORFRETE']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['DIRECIONAL']['VALOR']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['DIRECIONAL']['VALOR']
        TRANSPORTADORA['CIDADE'] = informacoes['CIDADE']
        TRANSPORTADORA['ESTADO'] = informacoes['UF']
        
        MainWindow.verificaCotacaSalvas(Pedido,TRANSPORTADORA)
    
    def salvaRodonaves(self):
        Pedido= widgets.lineEdit.text()
        informacoes = self.info
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = 'RODONAVES'
        TRANSPORTADORA['FRETECLIENTE'] = informacoes['VALORFRETE']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['RODONAVES']['VALOR']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['RODONAVES']['VALOR']
        TRANSPORTADORA['CIDADE'] = informacoes['CIDADE']
        TRANSPORTADORA['ESTADO'] = informacoes['UF']
        
        MainWindow.verificaCotacaSalvas(Pedido,TRANSPORTADORA)
    
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
        
# ///////////////////////////////////////////////////
# ////////////// # BUSCAR COTACAO FIM////////////////
# ///////////////////////////////////////////////////

#---------------------------------------------------
#---------------------------------------------------

# ///////////////////////////////////////////////////
# ////////////// # GERAR COTACAO  ///////////////////
# ///////////////////////////////////////////////////
    def gerarCotacao(self):

        valor_nfe = widgets.gerar_cotacao_valor_nfe.text()
        valor_nfe = valor_nfe.replace(',','.')
        valor_nfe = float(valor_nfe)
        
        
        quantidade = widgets.gerar_cotacao_quantidade.text()
        peso = widgets.gerar_cotacao_peso.text()
        
        cep = widgets.gerar_cotacao_cep.text()
        cep = cep.replace('-','')
        
        
        
        cubagem = MainWindow.calculo_cubagem()
        
        produto = lista_produtos
        
        cotacoes = GerarCotacao(cep,peso,valor_nfe,quantidade,cubagem,produto)
        melhor_prazo = MainWindow.melhorPrazo(cotacoes)
        melhor_valor = MainWindow.melhorValor(cotacoes)
        
        if melhor_prazo['TRANSPORTADORA'] == 'RODONAVES':
            widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
            widgets.lineEdit_11.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        
        elif melhor_prazo['TRANSPORTADORA'] == 'ALLIEX':
            widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
            widgets.lineEdit_11.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        
        elif melhor_prazo['TRANSPORTADORA'] == 'MID':
            widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Mid", None))
            widgets.lineEdit_11.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
            
        elif melhor_prazo['TRANSPORTADORA'] == 'DIRECIONAL':
            widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Direcional", None))
            widgets.lineEdit_11.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
            
        elif melhor_prazo['TRANSPORTADORA'] == 'TRANSREIS':
            widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
            widgets.lineEdit_11.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        else:
            widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora ", None))
            widgets.lineEdit_11.setStyleSheet(u"")
            widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(0), None)) #cotacao
            
            
        
        
        if melhor_valor['TRANSPORTADORA'] == 'RODONAVES':
            widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Rodonaves", None))
            widgets.lineEdit_13.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
        
        elif melhor_valor['TRANSPORTADORA'] == 'ALLIEX':
            widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Alliex", None))
            widgets.lineEdit_13.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
        
        elif melhor_valor['TRANSPORTADORA'] == 'MID':
            widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Mid", None))
            widgets.lineEdit_13.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
            
        elif melhor_valor['TRANSPORTADORA'] == 'DIRECIONAL':
            widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Direcional", None))
            widgets.lineEdit_13.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
            
        elif melhor_valor['TRANSPORTADORA'] == 'TRANSREIS':
            widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Transreis", None))
            widgets.lineEdit_13.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(melhor_valor['VALOR']), None)) #cotacao
        else:
            widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora ", None))
            widgets.lineEdit_13.setStyleSheet(u"")
            widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(0), None)) #cotacao
            
            
            
       
        
        
        widgets.lineEdit_40.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.cep['logradouro']), None))
        widgets.lineEdit_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.cep['bairro']), None))
        widgets.lineEdit_42.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.cep['localidade']), None))
        widgets.lineEdit_43.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.cep['uf']), None))
        
        
        widgets.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.rte['N_COTACAO']), None))
        widgets.lineEdit_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.rte['VALOR']), None))
        widgets.lineEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.rte['PRAZO']), None))
        
        widgets.lineEdit_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.alliex['N_COTACAO']), None))
        widgets.lineEdit_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.alliex['VALOR']), None))
        widgets.lineEdit_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.alliex['PRAZO']), None))
        
        widgets.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.transreis['N_COTACAO']), None))
        widgets.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.transreis['VALOR']), None))
        widgets.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.transreis['PRAZO']), None))
        
        widgets.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.mid['N_COTACAO']), None))
        widgets.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.mid['VALOR']), None))
        widgets.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.mid['PRAZO']), None))
        
        widgets.lineEdit_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.direcional['N_COTACAO']), None))
        widgets.lineEdit_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.direcional['VALOR']), None))
        widgets.lineEdit_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(cotacoes.direcional['PRAZO']), None))
        
        lista_produtos.clear()
    
    def lemparTelaCotacao(self):
        widgets.lineEdit_16.clear()
        widgets.lineEdit_17.clear()
        widgets.lineEdit_18.clear()
        widgets.lineEdit_12.clear()
        widgets.lineEdit_39.clear()
        widgets.gerar_cotacao_valor_nfe.clear()
        widgets.gerar_cotacao_quantidade.clear()
        widgets.gerar_cotacao_peso.clear()
        widgets.gerar_cotacao_cep.clear()
        widgets.lineEdit_40.clear()
        widgets.lineEdit_41.clear()
        widgets.lineEdit_42.clear()
        widgets.lineEdit_43.clear()
        widgets.lineEdit_11.clear()
        widgets.lineEdit_13.clear()
        widgets.lineEdit_14.clear()
        widgets.lineEdit_15.clear()
        widgets.lineEdit_16.clear()
        widgets.lineEdit_17.clear()
        widgets.lineEdit_18.clear()
        widgets.lineEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_14.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_15.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_20.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_25.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_26.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_27.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_28.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_29.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_30.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_31.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_32.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_33.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_34.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_35.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_36.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_37.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_38.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_40.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_41.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_42.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_43.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_44.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_11.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        widgets.lineEdit_13.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        lista_produtos.clear()
        widgets.tableWidget_2.clearContents()
        
    def tabela_cubagem(self): 
        largura = widgets.lineEdit_16.text()
        peso = widgets.lineEdit_44.text()
        altura = widgets.lineEdit_17.text()
        comprimento = widgets.lineEdit_18.text()
        quantidade = widgets.lineEdit_12.text()
        modelo = widgets.lineEdit_39.text()
        produtos = {}
        if modelo:
            informacoes = Banco.getInformacoes(f'SELECT weight,length,width ,height FROM `oc_product` WHERE model = {modelo}')
        
            produtos['ALTURA'] = int(informacoes[0][2])
            produtos['LARGURA'] = int(informacoes[0][1])
            produtos['COMPRIMENTO'] = int(informacoes[0][2])
            produtos['PESO'] = int(informacoes[0][0])
            produtos['QUANTIDADE'] = quantidade
            
        else:
            produtos['ALTURA'] = altura
            produtos['LARGURA'] = largura
            produtos['COMPRIMENTO'] = comprimento
            produtos['PESO'] = peso
            produtos['QUANTIDADE'] = quantidade
            
        lista_produtos.append(produtos)
        
        
        
        row=0
        for produto in lista_produtos:
            widgets.tableWidget_2.setItem(row, 0,QTableWidgetItem(str(produto['ALTURA'])))
            widgets.tableWidget_2.setItem(row, 1,QTableWidgetItem(str(produto['LARGURA'])))
            widgets.tableWidget_2.setItem(row, 2,QTableWidgetItem(str(produto['COMPRIMENTO'])))
            widgets.tableWidget_2.setItem(row, 3,QTableWidgetItem(str(produto['PESO'])))
            widgets.tableWidget_2.setItem(row, 4,QTableWidgetItem(str(produto['QUANTIDADE'])))

            row=row+1
            
        widgets.lineEdit_16.clear()
        widgets.lineEdit_17.clear()
        widgets.lineEdit_18.clear()
        widgets.lineEdit_12.clear()
        widgets.lineEdit_39.clear()
        widgets.lineEdit_44.clear()
    
    def melhorPrazo(cotacoes):
        rte = cotacoes.rte['PRAZO']
        alliex = cotacoes.alliex['PRAZO']
        mid = cotacoes.mid['PRAZO']
        direcional = cotacoes.direcional['PRAZO']
        transreis = cotacoes.transreis['PRAZO']
        
    
        if rte == 0 :
            rte = 1000
     
        if alliex == 0 :
            alliex = 1000

        if mid == 0 :
            mid = 1000
  
        if direcional == 0 :
            direcional = 1000
       
        if transreis == 0 :
            transreis = 1000
            
            
            
        
        try:
            rte = int(rte)
        except:
            rte = 100
    
        try:
            alliex = int(alliex)
        except:
            alliex = 100
            
        try:
            mid = int(mid)
        except:
            mid = 100
            
        try:
            direcional = int(direcional)
        except:
            direcional = 100
            
        try:
            transreis = int(transreis)
        except:
            transreis = 100
            
        lista_prazos = list()
        lista_prazos.append(rte)
        lista_prazos.append(alliex)
        lista_prazos.append(mid)
        lista_prazos.append(direcional)
        lista_prazos.append(transreis)
      
        lista_organizada = sorted(lista_prazos, key=int)
        
        if lista_organizada[0] == rte:
            retorno = {'TRANSPORTADORA': 'RODONAVES','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == alliex:
            retorno = {'TRANSPORTADORA': 'ALLIEX','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == mid:
            retorno = {'TRANSPORTADORA': 'MID','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == direcional:
            retorno = {'TRANSPORTADORA': 'DIRECIONAL','PRAZO': lista_organizada[0]}
        
        elif lista_organizada[0] == transreis:
            retorno = {'TRANSPORTADORA': 'TRANSREIS','PRAZO': lista_organizada[0]}
        else:
            retorno = {'TRANSPORTADORA': '','PRAZO': 0}
            
        return retorno
        
    def melhorValor(cotacoes):
        rte = cotacoes.rte['VALOR']
        alliex = cotacoes.alliex['VALOR']
        mid = cotacoes.mid['VALOR']
        direcional = cotacoes.direcional['VALOR']
        transreis = cotacoes.transreis['VALOR']
        
        try:
            rte = float(rte)
        except:
            rte = 10000
    
        try:
            alliex = float(alliex)
        except:
            alliex = 10000
            
        try:
            mid = float(mid)
        except:
            mid = 10000
            
        try:
            direcional = float(direcional)
        except:
            direcional = 10000
            
        try:
            transreis = float(transreis)
        except:
            transreis = 10000
            
        lista_prazos = list()
        lista_prazos.append(rte)
        lista_prazos.append(alliex)
        lista_prazos.append(mid)
        lista_prazos.append(direcional)
        lista_prazos.append(transreis)
      
        lista_organizada = sorted(lista_prazos, key=int)
        
        
        nova_lista = list()
        for valoreis in  lista_organizada:
            if valoreis > 0:
                nova_lista.append(valoreis)
                
        lista_organizada =  nova_lista
        lista_organizada = sorted(lista_organizada, key=int)
                
        if lista_organizada[0] == rte:
            retorno = {'TRANSPORTADORA': 'RODONAVES','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == alliex:
            retorno = {'TRANSPORTADORA': 'ALLIEX','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == mid:
            retorno = {'TRANSPORTADORA': 'MID','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == direcional:
            retorno = {'TRANSPORTADORA': 'DIRECIONAL','VALOR': lista_organizada[0]}
        
        elif lista_organizada[0] == transreis:
            retorno = {'TRANSPORTADORA': 'TRANSREIS','VALOR': lista_organizada[0]}
        else:
            retorno = {'TRANSPORTADORA': '','VALOR': 0}
            
        return retorno
       
    def calculo_cubagem():
        cubagem = 0
        for produto in lista_produtos:
            cubagem = int(int(produto['ALTURA']) * int(produto['LARGURA']) * int(produto['COMPRIMENTO'])) * int(produto['QUANTIDADE']) / 1000000

        if cubagem == 0:
            cubagem = 0.2
        
       
            
        return cubagem
# ///////////////////////////////////////////////////
# ////////////// FIM GERAR COTACAO  /////////////////
# ///////////////////////////////////////////////////
    
#---------------------------------------------------
#---------------------------------------------------

# ///////////////////////////////////////////////////
# ////////////// # RELATORIO COTACOES ///////////////
# ///////////////////////////////////////////////////

    def gerarRelatorioCotacoes(self):
        dataInicial = widgets.lineEdit_47.text()
        dataFinal = widgets.lineEdit_49.text()
        comboBox = widgets.comboBox.currentText()
        transportadora = MainWindow.selecaofiltro(comboBox)

        informacoes_cotacoes = Banco.getDataCotacaoSalvas(dataInicial,dataFinal,transportadora)
        widgets.tableWidget.setRowCount(len(informacoes_cotacoes))
        
        row=0
        total_cliente = 0
        total_Transporte = 0
        for informacoes in informacoes_cotacoes:        
            total_cliente += float(informacoes[2])
            
            total_Transporte += float(informacoes[3])
            
            diferenca_linha = float(informacoes[2]) - float(informacoes[3])
            diferenca_linha = str('R$ {:.2f}'.format(diferenca_linha))
            diferenca_linha = float(informacoes[2]) - float(informacoes[3])
            diferenca_linha = str('R$ {:.2f}'.format(diferenca_linha))        
            
            widgets.tableWidget.setItem(row, 0,QTableWidgetItem(str(informacoes[0])))
            widgets.tableWidget.setItem(row, 1,QTableWidgetItem(str(informacoes[1])))
            widgets.tableWidget.setItem(row, 2,QTableWidgetItem(str(informacoes[2])))
            widgets.tableWidget.setItem(row, 3,QTableWidgetItem(str(informacoes[3])))
            widgets.tableWidget.setItem(row, 4,QTableWidgetItem(str(informacoes[4])))
            widgets.tableWidget.setItem(row, 5,QTableWidgetItem(str(informacoes[5])))
            widgets.tableWidget.setItem(row, 6,QTableWidgetItem(diferenca_linha))
            widgets.tableWidget.setItem(row, 7,QTableWidgetItem(str(informacoes[6])))
            
            
            row=row+1

        diferenca = total_cliente - total_Transporte

        
        widgets.lineEdit_48.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {:.2f}".format(total_cliente), None))
        widgets.lineEdit_52.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {:.2f}".format(total_Transporte), None))
        widgets.lineEdit_53.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {:.2f}".format(diferenca), None))
    
    def selecaofiltro(filtro):
        filtro = str(filtro).upper()
        if filtro == 'TODAS':
            transporte = '*'
        
        elif filtro == 'RODONAVES':
            transporte = 'RODONAVES'
        elif filtro == 'ALLIEX':
            transporte = 'ALLIEX'
        elif filtro == 'TRANSREIS':
            transporte = 'TRANSREIS'
        elif filtro == 'MID':
            transporte = 'MID'
        elif filtro == 'DIRECIONAL':
            transporte = 'DIRECIONAL'
      
        return transporte

    def salvaRelatorio(relatorio):
        nomeSalvo = QtWidgets.QFileDialog.getSaveFileName()[0]

        dataInicial = widgets.lineEdit_47.text()
        dataFinal = widgets.lineEdit_49.text()
        comboBox = widgets.comboBox.currentText()
        transportadora = MainWindow.selecaofiltro(comboBox)

        informacoes_cotacoes = Banco.getDataCotacaoSalvas(dataInicial,dataFinal,transportadora)
        
        relatorio = dict()
        
        pedidos_linha = list()
        transportadora_linhas = list() 
        frete_cliente_linhas = list()
        frete_frete_transpoirtadora_linhas = list()
        cidade_linhas = list()
        estado_linhas = list()  
        diferenca_linhas = list()
        data_linhas = list()
        
        
        for informacoes in informacoes_cotacoes:
            pedidos_linha.append(informacoes[0])
            transportadora_linhas.append(informacoes[1])
            frete_cliente_linhas.append(informacoes[2])
            frete_frete_transpoirtadora_linhas.append(informacoes[3])
            cidade_linhas.append(informacoes[4])
            estado_linhas.append(informacoes[5])
            data_linhas.append(informacoes[6]) 
            
            diferenca_linha = float(informacoes[2]) - float(informacoes[3])
            diferenca_linha = str('R$ {:.2f}'.format(diferenca_linha))
            diferenca_linhas.append(diferenca_linha)
            
        relatorio['PEDIDO'] = pedidos_linha
        relatorio['TRANSPORTADORA'] = transportadora_linhas
        relatorio['FRETE CLIENTE'] = frete_cliente_linhas
        relatorio['FRETE TRANSPORTADORA'] = frete_frete_transpoirtadora_linhas
        relatorio['CIDADE'] = cidade_linhas
        relatorio['ESTADO'] = estado_linhas
        relatorio['DIFERENÇA'] = diferenca_linhas
        relatorio['DATA'] = data_linhas
        
        
        relatorio = pd.DataFrame(relatorio)
        datatoexcel = pd.ExcelWriter(f'{nomeSalvo}.xlsx')
        relatorio.to_excel(datatoexcel,index=False)
        datatoexcel.save()
        

# ///////////////////////////////////////////////////
# ////////////// # FIM RELATORIO COTACOES ///////////
# ///////////////////////////////////////////////////
    
    
    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.Inicio)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW WIDGETS PAGE
        if btnName == "btn_widgets":
            widgets.stackedWidget.setCurrentWidget(widgets.BuscarCotacao)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # SHOW NEW PAGE
        if btnName == "btn_new":
            widgets.stackedWidget.setCurrentWidget(widgets.GerarCotacao) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
            
        if btnName == "btn_share":
            widgets.stackedWidget.setCurrentWidget(widgets.GerarRelatorio) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU

    # RESIZE EVENTS
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
