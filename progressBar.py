def progressBar(itens,length=50,prefixo="Progress",sufixo="Complete",preenchimento="#",onProgress=""):

    '''
        parametros:
        itens - interable para utilizar durante a progress bar (uma list por exemplo)  
        length - Tamanho da progress bar que vai de 10 a 100
        prefixo - palavra/frase que inicia a barra de progresso
        sufixo - palavra/frase que termina na barra de progresso
        preenchimento - valor que vai preencher a barra de progresso, padrão = #
        onProgress - Caractere que é executado após a finalização de um progresso, exemplo caractere é 
                    \n para quebra de linha a cada execução 
    '''

    if(length > 100 or length < 10):
        length = 50

    # Pega o número total de items de um iterable como uma list
    totalItems = len(itens) 
    #atualziar  a barra de progresso
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
    for index,value in enumerate(itens):
        # retorna valor para utilizar numa estrutura de repetição
        yield value
        atualiza(index + 1)

    if(onProgress != "\n"):
        print()