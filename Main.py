import sys
from cDkL4nGwJ9.Mecanicas import MecanicasPrograma
from PyQt5.QtWidgets import QApplication

def main():
    #permitir a alteração do ícone do programa na barra de tarefas
    import ctypes
    myappid = 'mycompany.myproduct.subproduct.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    from PyQt5.QtGui import QIcon
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("cDkL4nGwJ9\imagens\icone.ico"))
    objetoJanela = None
    mecanicasObjeto = MecanicasPrograma()
    #a janela à ser gerada será definida de acordo com o estado atual do programa dentro do arquivo "Estado.txt"
    #estado: 0 = programa não executado anteriormente, estado: 1 = programa já foi executado anteriormente
    if(mecanicasObjeto.definirEstadoERetornar() == 0):
        mecanicasObjeto.alterarEstado()
        from cDkL4nGwJ9.EstadoZero import Janela
        objetoClasse = Janela(mecanicasObjeto)
        objetoJanela = objetoClasse.retornarJanela(0)
        objetoJanela.showFullScreen()
        app.exec_()
        
    elif(mecanicasObjeto.definirEstadoERetornar() == 1):
        from cDkL4nGwJ9.EstadoZero import Janela
        objetoClasse = Janela(mecanicasObjeto)
        objetoJanela = objetoClasse.retornarJanela(1)
        objetoJanela.showFullScreen()
        app.exec_()

if __name__ == "__main__":
    main()
