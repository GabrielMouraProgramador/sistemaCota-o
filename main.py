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
from PyQt6 import QtWidgets
from PyQt6 import *

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *
from widgets import *
from banco.consultas import Banco
from controle.gerar_cotacao import *

os.environ["QT_FONT_DPI"] = "96" # FIX Problem for High DPI and Scale above 100%

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
lista_produtos = []


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
        
        
        #GERAR COTACAO
        widgets.gerar_cotacao_btn.clicked.connect(self.gerarCotacao)
        widgets.pushButton_2.clicked.connect(self.tabela_cubagem)
        
        # // limpar tela cotacao
        widgets.pushButton_4.clicked.connect(self.lemparTelaCotacao)
    

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

    # GERAR COTACAO 
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
        widgets.lineEdit_19.clear()
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
