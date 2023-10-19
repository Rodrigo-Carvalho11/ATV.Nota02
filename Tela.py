from PySide6 import QtWidgets
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QDate
from ModuloInserir import inserir
from ModuloConverteData import converterData

class TelaPrincipal(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        carregador = QUiLoader()
        self.tela = carregador.load("Tela.ui")
        self.componentes()
        
    def componentes(self):
        self.caixaDescricao = self.tela.findChild(QtWidgets.QLineEdit,"caixaDescricao")   
        self.caixaDataIni = self.tela.findChild(QtWidgets.QDateEdit,"caixaDataIni")
        self.caixaDataTer = self.tela.findChild(QtWidgets.QDateEdit,"caixaDataTer")
        self.caixaObs = self.tela.findChild(QtWidgets.QTextEdit,"caixaObs")
        self.comboPriori = self.tela.findChild(QtWidgets.QComboBox,"caixaPriori")
        self.caixaRespo = self.tela.findChild(QtWidgets.QLineEdit,"caixaRespo")
        self.btnCadastrar = self.tela.findChild(QtWidgets.QPushButton,"btnCadastrar")
        self.btnLimpar = self.tela.findChild(QtWidgets.QPushButton,"btnLimpar")
        self.btnCadastrar.clicked.connect(self.cadastrar)
        self.btnLimpar.clicked.connect(self.limpar_campos) 
        
        
    
        
        listaDeOpcoes = ["Selecione","Alta","Media","Baixa"]
        self.comboPriori.addItems(listaDeOpcoes)
        
    def limpar_campos(self):
        self.caixaDescricao.clear()         
        self.comboPriori.setCurrentIndex(0)  
        self.caixaObs.clear()
        self.caixaRespo.clear()
        self.caixaDataIni.setDate(QDate(2018,1,1))
        self.caixaDataTer.setDate(QDate(2018,1,1))
        
           
    def cadastrar(self):
        desc = self.caixaDescricao.text()
        dataI = self.caixaDataIni.text()
        dataT = self.caixaDataTer.text()
        priori = self.comboPriori.currentText()
        respo = self.caixaRespo.text()
        obs = self.caixaObs.toPlainText()
        inserir(desc,converterData(dataI),converterData(dataT),respo,priori,obs)    
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    interface = TelaPrincipal()
    interface.tela.show()
    app.exec()