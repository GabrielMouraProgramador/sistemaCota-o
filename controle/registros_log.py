from time import gmtime, strftime

data_atual = strftime("%d-%m-%Y")

class log:
    def escreve(str=str()):
        with open('Logs\\registro atividade\\Atividade {}.txt'.format(data_atual), 'a+') as arquivo:
            data = strftime("%a, %d/%m/%Y as %H:%M:%S ")
            arquivo.write(str +' {}'.format(data) + '\n')
            
    def escreve_erro(str=str()):
        with open('Logs/registro erro/Log Erro {}.txt'.format(data_atual), 'a+') as arquivo:
            data = strftime("%a, %d/%m/%Y as %H:%M:%S ")
            arquivo.write(str +' {}'.format(data) + '\n')
            
