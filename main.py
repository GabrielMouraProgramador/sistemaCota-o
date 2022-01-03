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
from modules import ui_vincularCotacao
from modules import ui_vincularCotacaoManual
from modules import ui_AjusteFrete
from banco.consultas import Banco
from banco.consultas import CommercePlus
import pandas as pd
from controle.gerar_cotacao import *
from controle.apiCep import *
from time import gmtime, strftime

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
widgets_PopUP_Duplicado = None
widgets_ajusteFrete = None
widgets_vinvulaPedido = None
widgets_cotacao_Manual = None
lista_produtos = []

class VincularCotaccao(QMainWindow):
    def __init__(self,TRANSPORTADORA , COTACAO,PRAZO,VALOR,CEP):
        QMainWindow.__init__(self)
        self.ui = ui_vincularCotacao.Ui_Ui_VinculaPedido()
        self.ui.setupUi(self)
        global widgets_vinvulaPedido
        widgets_vinvulaPedido = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        UIFunctions.uiDefinitions(self)
        self.transporte = TRANSPORTADORA
        self.COTACAO = COTACAO
        self.VALOR = VALOR
        self.PRAZO = PRAZO
        self.CEP = CEP
        
        widgets_vinvulaPedido.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"{}".format(TRANSPORTADORA), None))
        widgets_vinvulaPedido.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"{}".format(COTACAO), None))
        widgets_vinvulaPedido.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"{}".format(VALOR), None))
        widgets_vinvulaPedido.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"{}".format(PRAZO), None))
        
        widgets_vinvulaPedido.pushButton.clicked.connect(self.buttonClick)
        widgets_vinvulaPedido.pushButton_2.clicked.connect(self.buttonClick)

    def salvaCotacaoComPedido(self):
        apicep = API_CEP(self.CEP)
        try:
            cidade = str(apicep['localidade']).upper()
        except:
            cidade = 'CIDADE'
        try:
            estado = str(apicep['localidade']).upper()
        except:
            estado = 'ESTADO'
            
        numeroPedido = widgets_vinvulaPedido.lineEdit.text()
        
        if len(numeroPedido) == 6 :
            frete_pedido = Banco.getValorDoFrete(int(numeroPedido))
        else:
            frete_pedido = CommercePlus.getFrete(numeroPedido)

        
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = numeroPedido
        TRANSPORTADORA['TRANSPOTADORA'] = self.transporte
        TRANSPORTADORA['FRETECLIENTE'] = frete_pedido
        TRANSPORTADORA['FRETETRANSPORTADORA'] = self.VALOR
        TRANSPORTADORA['CIDADE'] = cidade
        TRANSPORTADORA['ESTADO'] = estado
        TRANSPORTADORA['FRETECLIENTEMODIFICACAO'] = str(f"PEDIDO VINCULADO MANUALMENTE")
        TRANSPORTADORA['FRETETRANSPORTADORAMODIFICACAO'] = str(f"PEDIDO VINCULADO MANUALMENTE")
        
        
        Banco.alteraTransportdoraNoBanco(TRANSPORTADORA)
    

        
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        TRANSPORTADORA = self.transporte
            
        if btnName == "pushButton":
            VincularCotaccao.salvaCotacaoComPedido(self)
            self.hide()
            Sucesso = Pop_Up()
            Sucesso.show()
            
        
        if btnName == "pushButton_2":
            self.hide()
               
                   
class Ui_AjusteFrete(QMainWindow):
    def __init__(self,TRANSPORTADORA,Pedido):
        QMainWindow.__init__(self)
        self.ui = ui_AjusteFrete.Ui_AjusteFrete()
        self.ui.setupUi(self)
        global widgets_ajusteFrete
        widgets_ajusteFrete = self.ui
        UIFunctions.uiDefinitions(self)
        self.Transporte = TRANSPORTADORA
        self.Pedido = Pedido
        
        widgets_ajusteFrete.lineEdit_5.setText(QCoreApplication.translate("AjusteFrete", u"R$ {}".format(TRANSPORTADORA['FRETECLIENTE']), None))
        widgets_ajusteFrete.lineEdit_6.setText(QCoreApplication.translate("AjusteFrete", u"R$ {}".format(TRANSPORTADORA['FRETETRANSPORTADORA']), None))

        if TRANSPORTADORA['TRANSPOTADORA'] == 'RODONAVES':
            widgets_ajusteFrete.lineEdit_3.setText(QCoreApplication.translate("AjusteFrete", u"Transportadora Rodonaves", None))
            widgets_ajusteFrete.lineEdit_3.setStyleSheet(u"background-color: rgb(195, 159, 0);")
        
        elif TRANSPORTADORA['TRANSPOTADORA'] == 'ALLIEX':
            widgets_ajusteFrete.lineEdit_3.setText(QCoreApplication.translate("AjusteFrete", u"Transportadora Alliex", None))
            widgets_ajusteFrete.lineEdit_3.setStyleSheet(u"background-color: rgb(95, 85, 149);")
        
        elif TRANSPORTADORA['TRANSPOTADORA'] == 'MID':
            widgets_ajusteFrete.lineEdit_3.setText(QCoreApplication.translate("AjusteFrete", u"Transportadora Mid", None))
            widgets_ajusteFrete.lineEdit_3.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            
        elif TRANSPORTADORA['TRANSPOTADORA'] == 'DIRECIONAL':
            widgets_ajusteFrete.lineEdit_3.setText(QCoreApplication.translate("AjusteFrete", u"Transportadora Direcional", None))
            widgets_ajusteFrete.lineEdit_3.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            
        elif TRANSPORTADORA['TRANSPOTADORA'] == 'TRANSREIS':
            widgets_ajusteFrete.lineEdit_3.setText(QCoreApplication.translate("AjusteFrete", u"Transportadora Transreis", None))
            widgets_ajusteFrete.lineEdit_3.setStyleSheet(u"background-color: rgb(204, 85, 179);")
      
        elif TRANSPORTADORA['TRANSPOTADORA'] == 'SAO MIGUEL':
            widgets_ajusteFrete.lineEdit_3.setText(QCoreApplication.translate("AjusteFrete", u"Transportadora São Miguel", None))
            widgets_ajusteFrete.lineEdit_3.setStyleSheet(u"background-color: rgb(82, 153, 0);")
        
        
        widgets_ajusteFrete.pushButton.clicked.connect(self.salvaCotacaoAlterada)
        widgets_ajusteFrete.pushButton_2.clicked.connect(self.cancelar)
    
    def cancelar(self):
        self.hide()
    
    def salvaCotacaoAlterada(self):
        TRANSPORTADORA = self.Transporte
        Pedido = self.Pedido
        acrecimo_desconto_freteCliente = widgets_ajusteFrete.lineEdit_2.text()
        regraCliente = widgets_ajusteFrete.comboBox.currentText()
        
        acrecimo_desconto_freteTransportadora = widgets_ajusteFrete.lineEdit.text()
        regraTransporte = widgets_ajusteFrete.comboBox_2.currentText()
        
        TRANSPORTADORA = Ui_AjusteFrete.tratamentoAjusteFrete(acrecimo_desconto_freteCliente,regraCliente,acrecimo_desconto_freteTransportadora,regraTransporte,TRANSPORTADORA)
    
        verifica = Banco.veridicaPedidoSalvo(Pedido)
        if verifica == ():
            Banco.salvaCotacaoNoPedido(TRANSPORTADORA)
            sucesso = Pop_Up()
            sucesso.show()      
        else:
            duplicado = popUp_Duplicado(TRANSPORTADORA)
            duplicado.show()
        
        self.hide()
    
    def tratamentoAjusteFrete(acrecimo_desconto_freteCliente,regraCliente,acrecimo_desconto_freteTransportadora,regraTransporte,TRANSPORTADORA):

        if regraCliente == 'Normal':
            TRANSPORTADORA['FRETECLIENTEMODIFICACAO'] = str(f"MODIFICAÇÂO: {regraCliente}")
            
        elif regraCliente == 'Acréscimo Frete':
            TRANSPORTADORA['FRETECLIENTEMODIFICACAO'] = str(f"FRETE CLIENTE: {TRANSPORTADORA['FRETECLIENTE']} MODIFICAÇÂO: {regraCliente} VALOR: {acrecimo_desconto_freteCliente} ")
            TRANSPORTADORA['FRETECLIENTE'] = float(TRANSPORTADORA['FRETECLIENTE']) + float(str(acrecimo_desconto_freteCliente).replace(",",'.'))
            
        elif regraCliente == 'Desconto Frete':
            TRANSPORTADORA['FRETECLIENTEMODIFICACAO'] = str(f"FRETE CLIENTE: {TRANSPORTADORA['FRETECLIENTE']} MODIFICAÇÂO: {regraCliente} VALOR: {acrecimo_desconto_freteCliente} ")
            TRANSPORTADORA['FRETECLIENTE'] = float(TRANSPORTADORA['FRETECLIENTE']) - float(str(acrecimo_desconto_freteCliente).replace(",",'.'))
            
        
        if regraTransporte == 'Normal':
            TRANSPORTADORA['FRETETRANSPORTADORAMODIFICACAO'] = str(f"MODIFICAÇÂO: {regraTransporte}")

        elif regraTransporte == 'Acréscimo Frete':
            TRANSPORTADORA['FRETETRANSPORTADORAMODIFICACAO'] = str(f"FRETE TRANSPORTADORA: {TRANSPORTADORA['FRETETRANSPORTADORA']} MODIFICAÇÂO: {regraTransporte} VALOR: {acrecimo_desconto_freteTransportadora} ")
            TRANSPORTADORA['FRETETRANSPORTADORA'] = float(TRANSPORTADORA['FRETETRANSPORTADORA']) + float(str(acrecimo_desconto_freteTransportadora).replace(",",'.'))
        
        elif regraTransporte == 'Desconto Frete':
            TRANSPORTADORA['FRETETRANSPORTADORAMODIFICACAO'] = str(f"FRETE TRANSPORTADORA: {TRANSPORTADORA['FRETETRANSPORTADORA']} MODIFICAÇÂO: {regraTransporte} VALOR: {acrecimo_desconto_freteTransportadora} ")
            TRANSPORTADORA['FRETETRANSPORTADORA'] = float(TRANSPORTADORA['FRETETRANSPORTADORA']) - float(str(acrecimo_desconto_freteTransportadora).replace(",",'.'))
        
            
            
        return TRANSPORTADORA
        
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
            
class VincularCotacaoManuel(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = ui_vincularCotacaoManual.Ui_VinculaPedidoManual()
        self.ui.setupUi(self)
        global widgets_cotacao_Manual
        widgets_cotacao_Manual = self.ui
        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        UIFunctions.uiDefinitions(self)
        
        widgets_cotacao_Manual.pushButton.clicked.connect(self.salvaManual)


    def salvaManual(self):
        Pedido = widgets_cotacao_Manual.lineEdit.text()
        Transportadora = widgets_cotacao_Manual.comboBox.currentText()
        frete_cliente = widgets_cotacao_Manual.lineEdit_3.text()
        frete_Transporte = widgets_cotacao_Manual.lineEdit_4.text()
        
        if len(Pedido) == 6 :
            cep = Banco.getCepSite(int(Pedido))
        else:
            cep = CommercePlus.getCep(Pedido)
            

        apicep = API_CEP(cep)
        try:
            cidade = str(apicep['localidade']).upper()
        except:
            cidade = 'CIDADE'
        try:
            estado = str(apicep['localidade']).upper()
        except:
            estado = 'ESTADO'
        
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = Transportadora
        TRANSPORTADORA['FRETECLIENTE'] = str(frete_cliente).replace(',','.')
        TRANSPORTADORA['FRETETRANSPORTADORA'] = str(frete_Transporte).replace(',','.')
        TRANSPORTADORA['CIDADE'] = cidade
        TRANSPORTADORA['ESTADO'] = estado
        TRANSPORTADORA['FRETECLIENTEMODIFICACAO'] = str(f"PEDIDO VINCULADO MANUALMENTE")
        TRANSPORTADORA['FRETETRANSPORTADORAMODIFICACAO'] = str(f"PEDIDO VINCULADO MANUALMENTE")
        
        Banco.alteraTransportdoraNoBanco(TRANSPORTADORA)

        self.hide()
        Sucesso = Pop_Up()
        Sucesso.show()
        
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
        widgets.btn_adjustments.clicked.connect(self.buttonClick)
    
        
        
        #GERAR COTACAO
        widgets.gerar_cotacao_btn.clicked.connect(self.gerarCotacao)
        widgets.pushButton_2.clicked.connect(self.tabela_cubagem)
        widgets.pushButton_3.clicked.connect(self.buttonClick)
        widgets.pushButton_9.clicked.connect(self.buttonClick)
        widgets.pushButton_10.clicked.connect(self.buttonClick)
        widgets.pushButton_11.clicked.connect(self.buttonClick)
        widgets.pushButton_12.clicked.connect(self.buttonClick)
        
        widgets.pushButton_4.clicked.connect(self.lemparTelaCotacao)
        
        #BUSCA INFORMACOES PEDIDOS
        widgets.pushButton_14.clicked.connect(self.buscaInformacoesPedido)
       
        
        #BUSCAR COTACAO
        widgets.pushButton.clicked.connect(self.buscarCotacao)
        widgets.pushButton_5.clicked.connect(self.salvaRodonaves)
        widgets.pushButton_31.clicked.connect(self.salvaSaoMiguel)
        widgets.pushButton_32.clicked.connect(self.salvaAlliex)
        widgets.pushButton_33.clicked.connect(self.salvaTransreis)
        widgets.pushButton_34.clicked.connect(self.salvaMID)
        widgets.pushButton_35.clicked.connect(self.salvaDirecional)
        widgets.pushButton_13.clicked.connect(self.vinvularCotacaoManual)
        
        #RELATORIO COTAXAO
        widgets.pushButton_7.clicked.connect(self.gerarRelatorioCotacoes)
        widgets.pushButton_6.clicked.connect(self.salvaRelatorio)
        widgets.pushButton_8.clicked.connect(self.limpaTelaRelatorio)
    

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        #widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

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
      
        elif melhor_valor['TRANSPORTADORA'] == 'SAOMIGUEL':
            widgets.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Expresso São Miguel", None))
            widgets.lineEdit_2.setStyleSheet(u"background-color: rgb(82, 153, 0);")
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
      
        elif melhor_prazo['TRANSPORTADORA'] == 'SAOMIGUEL':
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora Expresso São Miguel", None))
            widgets.lineEdit_3.setStyleSheet(u"background-color: rgb(82, 153, 0);")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(melhor_prazo['PRAZO']), None)) #cotacao
        else:
            widgets.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Transportadora ", None))
            widgets.lineEdit_3.setStyleSheet(u"")
            widgets.lineEdit_6.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} Dias".format(0), None)) #cotacao
        
        #
        widgets.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['NOME']), None))
        widgets.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['PRAZOENTREGA']), None))
        widgets.lineEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoes['VALORFRETE']), None))
        widgets.lineEdit_8.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoes['TOTALPEDIDO']), None))
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
        
        #SAOMIGUEL
        widgets.lineEdit_235.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_236.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_238.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_232.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['SAOMIGUEL']['COTACAO']), None))
        widgets.lineEdit_233.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(str(informacoes['SAOMIGUEL']['VALOR'])).replace('.',','), None))
        widgets.lineEdit_234.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['SAOMIGUEL']['PRAZO']), None))
        widgets.lineEdit_237.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['SAOMIGUEL']['MEDIDAS']), None))
        
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
        sao_miguel = cotacoes['SAOMIGUEL']['VALOR']
        
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
        try:
            sao_miguel = float(transreis)
        except:
            sao_miguel = 10000
            
        lista_prazos = list()
        lista_prazos.append(rte)
        lista_prazos.append(alliex)
        lista_prazos.append(mid)
        lista_prazos.append(direcional)
        lista_prazos.append(transreis)
        lista_prazos.append(sao_miguel)
      
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
        
        elif lista_organizada[0] == sao_miguel:
            retorno = {'TRANSPORTADORA': 'SAOMIGUEL','VALOR': lista_organizada[0]}
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
        
        saoMiguel = cotacoes['SAOMIGUEL']['PRAZO']
        if saoMiguel == 0 :
            saoMiguel = 1000
        
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
        try:
            saoMiguel = int(saoMiguel)
        except:
            saoMiguel = 100
            
        lista_prazos = list()
        lista_prazos.append(rte)
        lista_prazos.append(alliex)
        lista_prazos.append(mid)
        lista_prazos.append(direcional)
        lista_prazos.append(transreis)
        lista_prazos.append(saoMiguel)
      
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
        
        elif lista_organizada[0] == saoMiguel:
            retorno = {'TRANSPORTADORA': 'SAOMIGUEL','PRAZO': lista_organizada[0]}
       
        else:
            retorno = {'TRANSPORTADORA': '','PRAZO': 0}
            
        return retorno
    
    def verificaCotacaSalvas(Pedido,TRANSPORTADORA):
       
        if Pedido == '':
            pass
        
        else:
            ajusteFrete = Ui_AjusteFrete(TRANSPORTADORA,Pedido)
            ajusteFrete.show()

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
    
    def salvaSaoMiguel(self):
        Pedido= widgets.lineEdit.text()
        informacoes = self.info
        TRANSPORTADORA = dict()
        TRANSPORTADORA['PEDIDO'] = Pedido
        TRANSPORTADORA['TRANSPOTADORA'] = 'SAO MIGUEL'
        TRANSPORTADORA['FRETECLIENTE'] = informacoes['VALORFRETE']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['SAOMIGUEL']['VALOR']
        TRANSPORTADORA['FRETETRANSPORTADORA'] = informacoes['SAOMIGUEL']['VALOR']
        TRANSPORTADORA['CIDADE'] = informacoes['CIDADE']
        TRANSPORTADORA['ESTADO'] = informacoes['UF']
        
        MainWindow.verificaCotacaSalvas(Pedido,TRANSPORTADORA)
    
    def limpatelacotacoes():
        widgets.lineEdit_3.setStyleSheet(u"")
        widgets.lineEdit_2.setStyleSheet(u"")
        widgets.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
        widgets.lineEdit_45.setPlaceholderText(QCoreApplication.translate("MainWindow", u"", None)) #NOME
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
    def buscaInformacoesPedido(self):
        numeroPedido = widgets.lineEdit_54.text()
        informacoes = Banco.getInformacoesCotacao(numeroPedido)
        informacoesCotUtilizadas = MainWindow.CotacaoUtilizadas(numeroPedido)

        if len(numeroPedido) == 6:
            produtos = Banco.getProdutosPedido(numeroPedido)
        else:
            produtos = CommercePlus.getProdutosPedido(numeroPedido)
      
        widgets.tableWidget_3.setRowCount(len(produtos))
        row=0
        for informacoes_tabela in produtos:        

            widgets.tableWidget_3.setItem(row, 0,QTableWidgetItem(str(informacoes_tabela['product_id'])))
            widgets.tableWidget_3.setItem(row, 1,QTableWidgetItem(str(informacoes_tabela['model'])))
            widgets.tableWidget_3.setItem(row, 2,QTableWidgetItem(str(informacoes_tabela['nome'])))
            widgets.tableWidget_3.setItem(row, 3,QTableWidgetItem(str(informacoes_tabela['quantidade'])))
            widgets.tableWidget_3.setItem(row, 4,QTableWidgetItem(str(informacoes_tabela['peso'])))
            widgets.tableWidget_3.setItem(row, 5,QTableWidgetItem(str(informacoes_tabela['altura'])))
            widgets.tableWidget_3.setItem(row, 6,QTableWidgetItem(str(informacoes_tabela['largura'])))
            widgets.tableWidget_3.setItem(row, 7,QTableWidgetItem(str(informacoes_tabela['comprimento'])))
            row=row+1
   
        
        if  informacoesCotUtilizadas['TRANSPORTADORA'] == 'RODONAVES':
            widgets.lineEdit_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoesCotUtilizadas['TRANSPORTADORA']), None))
            widgets.lineEdit_70.setStyleSheet(u"background-color: rgb(195, 159, 0);")
            widgets.lineEdit_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['RODONAVES']['MEDIDAS']), None))
            widgets.lineEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['RODONAVES']['COTACAO']), None))
            widgets.lineEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['RODONAVES']['PRAZO']), None))
            widgets.lineEdit_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETETRANSPORTADORA']), None))

        elif informacoesCotUtilizadas['TRANSPORTADORA'] == 'ALLIEX':
            widgets.lineEdit_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoesCotUtilizadas['TRANSPORTADORA']), None))
            widgets.lineEdit_70.setStyleSheet(u"background-color: rgb(95, 85, 149);")
            widgets.lineEdit_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['ALLIEX']['MEDIDAS']), None))
            widgets.lineEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['ALLIEX']['COTACAO']), None))
            widgets.lineEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['ALLIEX']['PRAZO']), None))
            widgets.lineEdit_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETETRANSPORTADORA']), None))
        
        elif informacoesCotUtilizadas['TRANSPORTADORA'] == 'MID':
            widgets.lineEdit_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoesCotUtilizadas['TRANSPORTADORA']), None))
            widgets.lineEdit_70.setStyleSheet(u"background-color: rgb(222, 110, 75);")
            widgets.lineEdit_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['MID']['MEDIDAS']), None))
            widgets.lineEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['MID']['COTACAO']), None))
            widgets.lineEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['MID']['PRAZO']), None))
            widgets.lineEdit_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETETRANSPORTADORA']), None))
        
        elif informacoesCotUtilizadas['TRANSPORTADORA'] == 'DIRECIONAL':
            widgets.lineEdit_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoesCotUtilizadas['TRANSPORTADORA']), None))
            widgets.lineEdit_70.setStyleSheet(u"background-color: rgb(23, 106, 214);")
            widgets.lineEdit_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['DIRECIONAL']['MEDIDAS']), None))
            widgets.lineEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['DIRECIONAL']['COTACAO']), None))
            widgets.lineEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['DIRECIONAL']['PRAZO']), None))
            widgets.lineEdit_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETETRANSPORTADORA']), None))
        elif informacoesCotUtilizadas['TRANSPORTADORA'] == 'TRANSREIS':
            widgets.lineEdit_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoesCotUtilizadas['TRANSPORTADORA']), None))
            widgets.lineEdit_70.setStyleSheet(u"background-color: rgb(204, 85, 179);")
            widgets.lineEdit_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['TRANSREIS']['MEDIDAS']), None))
            widgets.lineEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['TRANSREIS']['COTACAO']), None))
            widgets.lineEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['TRANSREIS']['PRAZO']), None))
            widgets.lineEdit_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETETRANSPORTADORA']), None))
        elif informacoesCotUtilizadas['TRANSPORTADORA'] == 'SAO MIGUEL':
            widgets.lineEdit_70.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoesCotUtilizadas['TRANSPORTADORA']), None))
            widgets.lineEdit_70.setStyleSheet(u"background-color: rgb(82, 153, 0);")
            widgets.lineEdit_65.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['SAOMIGUEL']['MEDIDAS']), None))
            widgets.lineEdit_67.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['SAOMIGUEL']['COTACAO']), None))
            widgets.lineEdit_68.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['SAOMIGUEL']['PRAZO']), None))
            widgets.lineEdit_66.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETETRANSPORTADORA']), None))
    

        
        widgets.lineEdit_72.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(str(informacoesCotUtilizadas['MODCLIENTE']).upper().replace('VALOR:','VALOR: R$')), None))
        widgets.lineEdit_73.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(str(informacoesCotUtilizadas['MODTRANSPORTE']).upper().replace('VALOR:','VALOR: R$')), None))

        
        
        widgets.lineEdit_51.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['NOME']), None))
        widgets.lineEdit_71.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} dias".format(informacoes['PRAZOENTREGA']), None))
        widgets.lineEdit_61.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoesCotUtilizadas['FRETECLIENTE']), None))
        widgets.lineEdit_60.setPlaceholderText(QCoreApplication.translate("MainWindow", u"R$ {}".format(informacoes['TOTALPEDIDO']), None))
        widgets.lineEdit_55.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CPF']), None))
        
        
        widgets.lineEdit_63.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CUBAGEM']), None))
        widgets.lineEdit_56.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['RUA']), None))
        widgets.lineEdit_58.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['BAIRRO']), None))
        widgets.lineEdit_57.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CIDADE']), None))
        widgets.lineEdit_59.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['UF']), None))
        widgets.lineEdit_50.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['CEP']), None))
        widgets.lineEdit_62.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['QUANTIDADETOTAL']), None))
        widgets.lineEdit_64.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{} kg".format(int(informacoes['PESOTOTAL'])), None))
        
        dataNormal  = str(informacoes['DATA'])
        ano = dataNormal[0]+dataNormal[1]+dataNormal[2]+dataNormal[3]
        mes = dataNormal[5]+dataNormal[6]
        dia = dataNormal[8]+dataNormal[9]
        dataFormatada = str(f"{dia}/{mes}/{ano}")
        
        
        widgets.lineEdit_69.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(dataFormatada), None))
        widgets.lineEdit_74.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(informacoes['MARCKETPLACE']), None))
        widgets.lineEdit_75.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(float(informacoesCotUtilizadas['FRETECLIENTE']) - float(informacoesCotUtilizadas['FRETETRANSPORTADORA'])), None))
        
        diferenca = float(informacoesCotUtilizadas['FRETECLIENTE']) - float(informacoesCotUtilizadas['FRETETRANSPORTADORA'])

        if diferenca < 0 :
            widgets.lineEdit_75.setStyleSheet(u"background-color: rgb(227, 38, 0);")
        else:
            widgets.lineEdit_75.setStyleSheet(u"background-color: rgb(100, 151, 0);")
            
    def CotacaoUtilizadas(numeroPedido):
        
        informacoes = Banco.veridicaPedidoSalvo(numeroPedido)
 
        INFORMACOES = dict()
        INFORMACOES['PEDIDO'] = informacoes[0][0]
        INFORMACOES['TRANSPORTADORA'] = informacoes[0][1]
        INFORMACOES['FRETECLIENTE'] = informacoes[0][2]
        INFORMACOES['FRETETRANSPORTADORA'] = informacoes[0][3]
        INFORMACOES['CIDADE'] = informacoes[0][4]
        INFORMACOES['ESTADO'] = informacoes[0][5]
        INFORMACOES['DATA'] = informacoes[0][6]
        INFORMACOES['MODCLIENTE'] = informacoes[0][7]
        INFORMACOES['MODTRANSPORTE'] = informacoes[0][8]
        return  INFORMACOES

        
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
        
        self.cotacoesGerados = cotacoes
        self.cotacoesGeradosCEP = cep


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
       
    def vinvularCotacaoManual(self):
        manual = VincularCotacaoManuel()
        manual.show()
         
       
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
        cidade = widgets.lineEdit_46.text()
        estado = widgets.comboBox_2.currentText()
        
        dataInicial = widgets.lineEdit_47.text()
        dataFinal = widgets.lineEdit_49.text()
        comboBox = widgets.comboBox.currentText()
        transportadora = MainWindow.selecaofiltro(comboBox)

        informacoes_cotacoes = Banco.getDataCotacaoSalvas(dataInicial,dataFinal,transportadora,cidade,estado)
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

        if diferenca < 0 :
            widgets.lineEdit_53.setStyleSheet(u"background-color: rgb(227, 38, 0);")
        else:
            widgets.lineEdit_53.setStyleSheet(u"background-color: rgb(100, 151, 0);")

            
        widgets.label_52.setText(QCoreApplication.translate("MainWindow", u"Resultados: {} resultados encontrados".format(row), None))
        
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
        cidade = widgets.lineEdit_46.text()
        estado = widgets.comboBox_2.currentText()
        nomeSalvo = QtWidgets.QFileDialog.getSaveFileName()[0]

        dataInicial = widgets.lineEdit_47.text()
        dataFinal = widgets.lineEdit_49.text()
        comboBox = widgets.comboBox.currentText()
        transportadora = MainWindow.selecaofiltro(comboBox)

        informacoes_cotacoes = Banco.getDataCotacaoSalvas(dataInicial,dataFinal,transportadora,cidade,estado)
        
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
        
    def limpaTelaRelatorio(self):
        widgets.lineEdit_47.clear()
        widgets.lineEdit_49.clear()
        widgets.lineEdit_46.clear()
        widgets.lineEdit_48.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_52.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_53.setPlaceholderText(QCoreApplication.translate("MainWindow", u"{}".format(''), None))
        widgets.lineEdit_53.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        widgets.label_52.setText(QCoreApplication.translate("MainWindow", u"Resultados:", None))
        widgets.tableWidget.setRowCount(0)
        widgets.tableWidget.clearContents()
       
        
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
        
        if btnName == "btn_adjustments":
            widgets.stackedWidget.setCurrentWidget(widgets.consulataPedido) # SET PAGE
            UIFunctions.resetStyle(self, btnName) # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet())) # SELECT MENU
        
        if btnName == "pushButton_3":
            rte = self.cotacoesGerados.rte
            cep = self.cotacoesGeradosCEP
            cotacao = VincularCotaccao('RODONAVES',rte['N_COTACAO'],rte['PRAZO'],rte['VALOR'],cep )
            cotacao.show()
        
        if btnName == "pushButton_9":
            alliex = self.cotacoesGerados.alliex
            cep = self.cotacoesGeradosCEP
            cotacao = VincularCotaccao('ALLIEX',alliex['N_COTACAO'],alliex['PRAZO'],alliex['VALOR'],cep)
            cotacao.show()

        
        if btnName == "pushButton_10":
            transreis = self.cotacoesGerados.transreis
            cep = self.cotacoesGeradosCEP
            cotacao = VincularCotaccao('TRANSREIS',transreis['N_COTACAO'],transreis['PRAZO'],transreis['VALOR'],cep)
            cotacao.show()

        
        if btnName == "pushButton_11":
            mid = self.cotacoesGerados.mid
            cep = self.cotacoesGeradosCEP
            cotacao = VincularCotaccao('MID',mid['N_COTACAO'],mid['PRAZO'],mid['VALOR'],cep)
            cotacao.show()
        
        if btnName == "pushButton_12":
            direceional = self.cotacoesGerados.direcional
            cep = self.cotacoesGeradosCEP
            cotacao = VincularCotaccao('DIRECIONAL',direceional['N_COTACAO'],direceional['PRAZO'],direceional['VALOR'],cep)
            cotacao.show()
        
            
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
