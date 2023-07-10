from PyQt5.QtGui import QPixmap
class Janela:
    from win32api import GetSystemMetrics
    from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit
    from PyQt5.QtCore import Qt

    #receber o objeto da classe de mêcanicas criado no Main
    mecanicasObjeto = None
    def __init__(self, objetoMecanicasCriado):
        self.mecanicasObjeto = objetoMecanicasCriado

    #salvar largura e altura do monitor do usuário
    larguraMonitor = GetSystemMetrics(0)
    alturaMonitor = GetSystemMetrics(1)

    #criar a janela e remover o fundo dela
    janela = QWidget()
    janela.setAttribute(Qt.WA_TranslucentBackground, True) 
    janela.setWindowFlag(Qt.FramelessWindowHint)

    #gerar imagem do personagem na tela
    pixmap = QPixmap("cDkL4nGwJ9\imagens\parado1.png")
    labelPersonagem = QLabel(janela)
    labelPersonagem.setPixmap(pixmap)
    labelPersonagem.move(round(larguraMonitor/5.7), round(alturaMonitor/2.25))

    #label da fala do personagem
    labelFala = QLabel(janela)
    labelFala.setText("")
    labelFala.setStyleSheet("""color: red; 
                               font-size: 20px; 
                               border: 5px;
                               border-style: solid;
                               background-color: white;
                            """)
    labelFala.move(round(larguraMonitor/1.7), round(alturaMonitor/1.7))
    labelFala.hide()

    #botão de avançar a fala do personagem
    botaoAvancarFala = QPushButton(janela)
    botaoAvancarFala.setText("->")
    botaoAvancarFala.setGeometry(round(larguraMonitor/1.7), round(alturaMonitor/1.92), round(larguraMonitor/25.5), round(alturaMonitor/16))
    botaoAvancarFala.setStyleSheet("""QPushButton{
                                            background-color: black;
                                            border: 1px;
                                            border-style: solid;
                                            border-color: white; 
                                            color: white;
                                            font-size:40px;
                                      }
                                      QPushButton::pressed{
                                            background-color: white;
                                            color: black;
                                            border-color: black;
                                      }""")
    botaoAvancarFala.hide()

    #campo para digitar o comando
    campoInserirComando = QLineEdit(janela)
    campoInserirComando.setGeometry(round(larguraMonitor/1.7), round(alturaMonitor/1.7), round(larguraMonitor/2.5), round(alturaMonitor/15))
    campoInserirComando.setStyleSheet("""border:5px;
                                         border-style:solid;
                                         border-color: black;
                                         font-size:20px;
                                        """)
    campoInserirComando.hide()

    #botão de inserir o comando dentro do campo de comandos
    botaoInserirComando = QPushButton(janela)
    botaoInserirComando.setText(">>")
    botaoInserirComando.setGeometry(round(larguraMonitor/1.066), round(alturaMonitor/1.518), round(larguraMonitor/20.5), round(alturaMonitor/15))
    botaoInserirComando.setStyleSheet("""QPushButton{
                                            background-color: black;
                                            border: 1px;
                                            border-style: solid;
                                            border-color: white; 
                                            color: white;
                                            font-size:40px;
                                         }
                                         QPushButton::pressed{
                                            background-color: white;
                                            color: black;
                                            border-color: black;
                                         }""")
    botaoInserirComando.hide()

    #tocar som de clique, esconder botão se o label de falas não tiver falas
    def avancarFala(self):
        self.mecanicasObjeto.carregarETocar("click.mp3")
        self.acaoTeclado.activated.disconnect()
        if(self.labelFala.text() == ""):
            self.botaoAvancarFala.hide()
            self.acaoTeclado.activated.connect(self.inserirComando)
    #alterar imagem atual do personagem
    def _mudarImagemPersonagem(self, nomeArquivoImagem):
        self.pixmap = QPixmap("cDkL4nGwJ9\imagens\\" + nomeArquivoImagem)
        self.labelPersonagem.setPixmap(self.pixmap)

    #alterar a fala do personagem
    def _mudarFalaPersonagem(self, textoFala):
        self.labelFala.hide()
        if(not(textoFala == "")):
            #caso o texto tenha atingido a capacidade máxima de largura, inserir uma "quebra de linha" no local
            if(len(textoFala) > 52):
                textoFala = textoFala[:52] + "\n" + textoFala[52:]
                if(len(textoFala) > (52*2+2)):
                    textoFala = textoFala[:(52*2+2)] + "\n" + textoFala[(52*2+2):]
                    if(len(textoFala) > (52*3+2)):
                        textoFala = textoFala[:(52*3+2)] + "\n" + textoFala[(52*3+2):]
                        if(len(textoFala) > (52*4+2)):
                            textoFala = textoFala[:(52*4+2)] + "\n" + textoFala[(52*4+2):]
                            if(len(textoFala) > (52*5+2)):
                                textoFala = textoFala[:(52*5+2)] + "\n" + textoFala[(52*5+2):]
                                if(len(textoFala) > (52*6+2)):
                                    textoFala = textoFala[:(52*6+2)] + "\n" + textoFala[(52*6+2):]
                                    if(len(textoFala) > (52*7+2)):
                                        textoFala = textoFala[:(52*7+2)] + "\n" + textoFala[(52*7+2):]
                                        if(len(textoFala) > (52*8+2)):
                                            textoFala = textoFala[:(52*8+2)] + "\n" + textoFala[(52*8+2):]
                                            if(len(textoFala) > (52*9+2)):
                                                textoFala = textoFala[:(52*9+2)] + "\n" + textoFala[(52*9+2):]
                                                if(len(textoFala) > (52*10+2)):
                                                    textoFala = textoFala[:(52*10+2)] + "\n" + textoFala[(52*10+2):]
                                                    if(len(textoFala) > (52*11+2)):
                                                        textoFala = textoFala[:(52*11+2)] + "[...]"
            self.labelFala.setText(textoFala)
            self.labelFala.show()
        else:
            #manter label da fala escondido se a função não receber nenhum texto como parâmetro
            self.labelFala.setText(textoFala)
            self.labelFala.hide()

    #checar se a pergunta já foi feita anteriormente
    def checarSePerguntaExiste(self, comandoInserido):
        checagem = self.mecanicasObjeto.checarSePerguntaExiste(comandoInserido)
        if(checagem == True):
            #se ela já tiver sido feita, alterar a fala, imagem do personagem e tocar o som correspondente da resposta
            self._mudarFalaPersonagem(self.mecanicasObjeto.respostaPerguntaEncontrada)
            self._mudarImagemPersonagem(self.mecanicasObjeto.imagemPerguntaEncontrada)
            self.mecanicasObjeto.carregarETocar(self.mecanicasObjeto.somEncontrado)
            return True
        else: return False

    acaoTeclado = None
    #executar o comando inserido
    def inserirComando(self):
        comando = self.campoInserirComando.text()
        comando = comando.lower()
        comando = comando.replace("=", "")
        self.campoInserirComando.setText("")
        self.campoInserirComando.hide()
        self.botaoInserirComando.hide()
        if(self.checarSePerguntaExiste(comando) == False):
            if("?" in comando):
                imagemResposta = None
                audioPraSalvar = None
                if("numero" in comando or "numeros" in comando or "número" in comando or "números" in comando or "idade" in comando or "anos" in comando or "tamanho" in comando or "largura" in comando or "distancia" in comando or "distância" in comando or "peso" in comando or "+" in comando or "-" in comando + "/" in comando or "*" in comando):
                    import random
                    escolha = str(random.choice(range(100)))
                    self._mudarFalaPersonagem(escolha + "!")
                    self._mudarImagemPersonagem("falando1.png")
                    self.mecanicasObjeto.carregarETocar("risada1.wav")
                    imagemResposta = "falando1.png"
                    audioPraSalvar = "risada1.wav"
                elif("cor" in comando):
                    import random
                    vetorCores = ["preto", "cinza", "branco", "vermelho", "laranja", "amarelo", "verde", "ciano", "azul", "roxo", "rosa"]
                    self._mudarFalaPersonagem(str(random.choice(vetorCores)) + "!")
                    self._mudarImagemPersonagem("falando1.png")
                    self.mecanicasObjeto.carregarETocar("risada1.wav")
                    imagemResposta = "falando1.png"
                    audioPraSalvar = "risada1.wav"
                elif("gosta" in comando or "é" in comando or "quer" in comando or "sou" in comando or "devia" in comando or "deveria" in comando or "odeia" in comando or "faz" in comando or "você" in comando or "eu" in comando or "meu" in comando or "minha" in comando) :
                    resposta = self.mecanicasObjeto.escolherRespostaAleatória()
                    if(resposta == 0):
                        self._mudarFalaPersonagem("Claro que não!")
                        self._mudarImagemPersonagem("reacaoNegativa1.png")
                        self.mecanicasObjeto.carregarETocar("zangado.mp3")
                        imagemResposta = "reacaoNegativa1.png"
                        audioPraSalvar = "zangado.mp3"
                    elif(resposta == 1):
                        self._mudarFalaPersonagem("Não.")
                        self._mudarImagemPersonagem("reacaoNegativa2.png")
                        self.mecanicasObjeto.carregarETocar("no.mp3")
                        imagemResposta = "reacaoNegativa2.png"
                        audioPraSalvar = "no.mp3"
                    elif(resposta == 2):
                        self._mudarFalaPersonagem("Eu... não tenho certeza...")
                        self._mudarImagemPersonagem("reacaoNeutra.png")
                        self.mecanicasObjeto.carregarETocar("huh.wav")
                        imagemResposta = "reacaoNeutra.png"
                        audioPraSalvar = "huh.wav"
                    elif(resposta == 3):
                        self._mudarFalaPersonagem("Sim.")
                        self._mudarImagemPersonagem("reacaoPositiva1.png")
                        self.mecanicasObjeto.carregarETocar("yes.wav")
                        imagemResposta = "reacaoPositiva1.png"
                        audioPraSalvar = "yes.wav"
                    else:
                        self._mudarFalaPersonagem("Com certeza!")
                        self._mudarImagemPersonagem("reacaoPositiva2.png")
                        self.mecanicasObjeto.carregarETocar("yeah.mp3")
                        imagemResposta = "reacaoPositiva2.png"
                        audioPraSalvar = "yeah.mp3"
                else:
                    self._mudarFalaPersonagem("Desculpa, eu não entendi oque você quis dizer...")
                    self._mudarImagemPersonagem("reacaoConfusa.png")
                    self.mecanicasObjeto.carregarETocar("wha.wav")
                    imagemResposta = "reacaoConfusa.png"
                    audioPraSalvar = "wha.wav"
                self.mecanicasObjeto.salvarPerguntaEResposta(comando, self.labelFala.text(), imagemResposta, audioPraSalvar)
            elif("fechar" in comando or "feche" in comando or "sair" in comando):
                self._mudarFalaPersonagem("Até mais! Volte logo.")
                self._mudarImagemPersonagem("falando1.png")
                self.mecanicasObjeto.carregarETocar("seeYaLater.mp3")
                self.acaoTeclado.activated.disconnect()
                self.acaoTeclado.activated.connect(lambda: self.janela.close())
                self.botaoAvancarFala.clicked.connect(lambda: self.janela.close())
            elif(comando == ""):
                self._mudarFalaPersonagem("?...")
                self.mecanicasObjeto.carregarETocar("huh.wav")
                self._mudarImagemPersonagem("reacaoNegativa2.png")
            else:
                self._mudarFalaPersonagem("Desculpa, eu não entendi oque você quis dizer...")
                self._mudarImagemPersonagem("reacaoConfusa.png")
                self.mecanicasObjeto.carregarETocar("huh.wav")
        def acaoBotao():
            self._mudarFalaPersonagem("")
            self._mudarImagemPersonagem("parado2.png")
            self.campoInserirComando.show()
            self.botaoInserirComando.show()
            self.avancarFala()
        self.acaoTeclado.activated.connect(acaoBotao)
        self.botaoAvancarFala.clicked.connect(lambda: acaoBotao())
        self.botaoAvancarFala.show()

    #animações do personagem
    #numero identificador do frame da animação
    numFrame = 0
    def _animacao(self, idAnimacao):
        from PyQt5.QtCore import QTimer
        temporizador = QTimer(self.janela)
        #animação de introdução
        if(idAnimacao == 0):
            def animar():
                if(self.numFrame == 0):
                    self._mudarImagemPersonagem("parado3.png")
                    self.numFrame = self.numFrame + 1
                elif(self.numFrame == 1):
                    self._mudarImagemPersonagem("falando1.png")
                    self._mudarFalaPersonagem("Hey! Obrigado por me instalar! Pode me chamar de \"Flame\".")
                    self.mecanicasObjeto.carregarETocar("hey1.mp3")
                    self.botaoAvancarFala.show()
                    self.numFrame = self.numFrame + 1
                    temporizador.stop()
                elif(self.numFrame == 2):
                    self._mudarFalaPersonagem("Vamos começar então... Apenas digite oque você quer na caixa que vai aparecer e aperte o botão de enviar! E se for me fazer alguma pergunta, não se esqueça do ponto de interrogação!")
                    self.numFrame = self.numFrame + 1
                elif(self.numFrame == 3):
                    self.numFrame = 0
                    self._mudarImagemPersonagem("parado2.png")
                    self._mudarFalaPersonagem("")
                    self.campoInserirComando.show()
                    self.botaoInserirComando.clicked.connect(self.inserirComando)
                    self.acaoTeclado.activated.connect(self.inserirComando)
                    self.botaoInserirComando.show()
                    self.botaoAvancarFala.clicked.disconnect()
            temporizador.timeout.connect(animar)
            temporizador.start(1000)
            #acão do botão de pular fala
            def acaoBotao():
                animar()
                self.avancarFala()
            #adicionar ação ao botão de pular fala
            self.botaoAvancarFala.clicked.connect(acaoBotao)
            self.acaoTeclado.activated.connect(lambda: acaoBotao())
        else:
            def animar():
                if(self.numFrame == 0):
                    self._mudarImagemPersonagem("parado3.png")
                    self.numFrame = self.numFrame + 1
                elif(self.numFrame == 1):
                    self._mudarImagemPersonagem("reacaoPositiva2.png")
                    self._mudarFalaPersonagem("Hey! Bem vindo de volta! Você já sabe como funciona, apenas digite o comando e confirme!")
                    self.mecanicasObjeto.carregarETocar("hey1.mp3")
                    self.botaoAvancarFala.show()
                    self.numFrame = self.numFrame + 1
                    temporizador.stop()
                elif(self.numFrame == 2):
                    self._mudarImagemPersonagem("parado2.png")
                    self._mudarFalaPersonagem("")
                    self.campoInserirComando.show()
                    self.botaoInserirComando.clicked.connect(self.inserirComando)
                    self.acaoTeclado.activated.disconnect()
                    self.acaoTeclado.activated.connect(self.inserirComando)
                    self.botaoInserirComando.show()
                    self.botaoAvancarFala.clicked.disconnect()
            temporizador.timeout.connect(animar)
            temporizador.start(1000)
            #acão do botão de pular fala
            def acaoBotao():
                animar()
                self.avancarFala()
            #adicionar ação ao botão de pular fala
            self.botaoAvancarFala.clicked.connect(acaoBotao)
            self.acaoTeclado.activated.connect(lambda: acaoBotao())
    
    #retornar a janela criada e executar animação inicial
    def retornarJanela(self, idAnimacaoInicial):
        from PyQt5.QtWidgets import QShortcut
        from PyQt5.QtGui import QKeySequence
        self.acaoTeclado = QShortcut(QKeySequence("Ctrl+I"), self.janela)
        self._animacao(idAnimacaoInicial)
        return self.janela