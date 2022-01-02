from collections.abc import Iterable

def progressBar(itens,length=50,prefixo="Progress",sufixo="Complete",preenchimento="#",onProgress=""):

    if(length > 100 or length < 10):
        length = 50

    # Pega o número total de items de um iterable como uma list
    totalItems = len(itens) 
    #atualziar  a barra de progress
    def atualiza(itemAtual):
        #Calculo da porcentagem da barra de progresso
        porcentagem = "{0:.0f}".format((itemAtual / float(totalItems)*100))
        #Calculo para preenchimento dos items
        tamanhoPreenchimento = int((length * float(porcentagem)) / 100)
        #String para preencher no print
        preenchimentoAtual = (preenchimento * tamanhoPreenchimento )+ "-" * (length - tamanhoPreenchimento)
        #Corpo da striing
        barra = "{0} -> |{1}| {2}% {3} {4}".format(prefixo,preenchimentoAtual,porcentagem,sufixo,onProgress)
        
        #exibição ;)
        print(barra,end='\r')

    #primeira atualização, literalmente o inicio da barra
    atualiza(0)

    # atualização da barra de progresso feito a cada atualização
    # e validacao dos tipos range ou interable
    try:
        if isinstance(itens,Iterable):
            for index,value in enumerate(itens):
                # retorna valor para utilizar numa estrutura de repetição
                yield value
                atualiza(index + 1)
        else:
            for index in itens:
                yield index
                atualiza(index +1 )
    except:
        print("only interable or range allowed!")
        
    if(onProgress != "\n"):
        print()