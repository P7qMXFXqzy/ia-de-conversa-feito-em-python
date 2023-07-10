class MecanicasPrograma:
    from pygame import mixer
    estadoAtual = None
    perguntasERespostas = []
    respostaPerguntaEncontrada = None
    imagemPerguntaEncontrada = None
    somEncontrado = None
    mixer.init()
    
    #checar o estado atual do programa, função utilizada dentro da função "definirEstadoERetornar"
    def _lerEstadoNoArquivoTxt(self):
        with open('cDkL4nGwJ9/outrosArquivos/Estado.txt', 'r') as file:
            #ler apenas a primeira linha do arquivo "Estado.txt", checar seu número e retornar o valor do seu estado
            linhaTexto = file.readline().strip()
            return linhaTexto[-1]
        
    #definir uma resposta aleatória
    def escolherRespostaAleatória(self):
        import random
        #0 = resposta muito negativa, 1 = resposta negativa, 2 = resposta neutra, 3 = resposta positiva, 4 = resposta muito positiva
        respostas = [0, 1, 2, 3, 4]
        return random.choice(respostas)

    #definir o valor da variável "estadoAtual" e retornar
    def definirEstadoERetornar(self):
        self.estadoAtual = int(self._lerEstadoNoArquivoTxt())
        return self.estadoAtual
    
    #carregar e tocar som escolhido
    def carregarETocar(self, somCarregado):
        self.mixer.music.load("cDkL4nGwJ9\sons\\" + str(somCarregado))
        self.mixer.music.play()

    #definir que o programa já foi aberto pelo menos uma vez
    def alterarEstado(self):
        redefinirEstado = open('cDkL4nGwJ9/outrosArquivos/Estado.txt', 'w+')
        redefinirEstado.write("Estado: 1")
        redefinirEstado.close()

    #carregar as perguntas e respostas salvas dentro do arquivo "Memória.txt"
    def carregarPerguntasSalvas(self):
        with open('cDkL4nGwJ9/outrosArquivos/Memória.txt', 'r', -1 , "ANSI") as arquivo:
            perguntas = arquivo.readlines()
        #remover o "\n" em cada linha
        perguntas = [linha.strip() for linha in perguntas]
        self.perguntasERespostas = perguntas

    #checar se a pergunta já foi feita anteriormente, retornar True se sim e definir o valor das variáveis para valores encontrados, retornar False se não tiver sido encontrada
    def checarSePerguntaExiste(self, pergunta):
        perguntaEncontrada = False
        for x in range(len(self.perguntasERespostas)):
            if(pergunta == (self.perguntasERespostas[x][:(self.perguntasERespostas[x].index("="))-1])):
                self.respostaPerguntaEncontrada = self.perguntasERespostas[x][((self.perguntasERespostas[x].index("="))+2):((self.perguntasERespostas[x].index("=="))-1)]
                self.imagemPerguntaEncontrada = self.perguntasERespostas[x][((self.perguntasERespostas[x].index("=="))+3):((self.perguntasERespostas[x].index("==="))-1)]
                self.somEncontrado = self.perguntasERespostas[x][((self.perguntasERespostas[x].index("==="))+4):]
                perguntaEncontrada = True
                break
        return perguntaEncontrada
    
    #salvar pergunta (não feita anteriormente), sua resposta e áudio no arquivo "Memória.txt" e re-carregar as perguntas encontradas
    def salvarPerguntaEResposta(self, novaPergunta, resposta, imagem, audio):
        salvar = open('cDkL4nGwJ9/outrosArquivos/Memória.txt', 'a+', -1, "ANSI")
        salvar.write(novaPergunta + " = " + resposta +  " == " + imagem + " === " + audio +"\n")
        salvar.close()
        self.carregarPerguntasSalvas()
#sempre carregar por padrão as perguntas salvas no arquivo "Memória.txt" 
MecanicasPrograma.carregarPerguntasSalvas(MecanicasPrograma)