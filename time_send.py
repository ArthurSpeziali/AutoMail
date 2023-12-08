#Importanto as bibliotecas:
import datetime
from time import sleep

#Função para esperar chegar a data/hora específicas, e depois continuar o funcionamento dos emais:
def time_send():
    print('Você quer repertir quantas vezes? Digite "0" Para sempre!')
    
    #Vendo quantas vezes ele vai repetir, no caso de 0 será um ciclo while:
    while True:
        try:
            repeat = int(input())
            break
        except ValueError:
            print('Número inválido, tente novamente!')
            
    print('Digite o dia e mês (05/12) que vai mandar o E-mail. (Coloque só o dia se quiser mandar o e-mail sempre neste dia)')
    
    #Vendo se a data digita é valida, podendo ter so o dia, ou o dia e mês:
    while True:
        data_prog = input().strip()
        
        if len(data_prog) > 5:
            print('Data inválida, tente novamente!')    
        
        
        #Separa do dia do mês:
        else:
            data_prog = data_prog.split('/')
        
            try:
               
                #Calcula dia e mês de hoje, segundo o relógio do seu sistema.
                #Tira o ano primeiro, depois inverte o mês com o dia:
                data_now = str(datetime.date.today()).split('-')
                data_now.pop(0)
                data_now.insert(0, data_now.pop(1))
                
                #Coloca temporariamente o mês de hoje, para verificar se o dia não passa de 31, e o mês de 12.
                #Coloca este mês amais, pois se o usuario colocar só o dia, e verificação para.
                #Se já tiver dia e mês, e adicionar este mês amais, continua funcionando corretamente:
                data_prog.append(data_now[1])
                if int(data_prog[0]) > 31 or int(data_prog[1]) > 12:
                    print('Data inválida, tente novamente!')
                    
                else:
                    #Tira o mês adicionado anteriormente:
                    data_prog.pop()                       
                    break
                    
            
            except ValueError:
                print('Data inválida, tente novamente!')

    #Faz o mesmo processo, agora com hora e minuto.
    #Diferente do outro, é obrigado os 2 parâmetros:
    print('Qual será a hora e o minuto? (15:30)')
    while True:
        tempo_prog = input().strip()
       
        if len(tempo_prog) > 5:
            print('Tempo inválido, tente novamente!')
        
        else:
            tempo_prog = tempo_prog.split(':')
            
            try:
                #Cria uma lista com hora e minuto atuais.
                #Usa o zfill para adcionar um "0" se preciso. A hora retornada seria 23,5, mas com zfill fica 23,05:
                tempo_now = [str(datetime.datetime.now().hour).zfill(2), str(datetime.datetime.now().minute).zfill(2)]
                
                if int(tempo_prog[0]) > 23 or int(tempo_prog[1]) > 59:
                    print('Tempo inválido, tente novamente!')    
                    
                else:
                    break
                    
            
            except ValueError:
                print('Tempo inválido, tente novamente!')    

    #Função para processar se já chegou na data programada.
    #se não, espera uma quantidade que resta de segundos para esperar até o dia:
    def wait_send():
        while True:
            
            #Se a data tiver dia e mês, espera a quantidade certa até o próximo dia e mês.
            #Expresão com muitos parenteeses, para calcular na ordem certa:
            if len(data_prog) == 2:
                days = ((int(data_prog[1]) - 1) * 30 + int(data_prog[0])) - ((int(data_now[1]) -1) * 30 + int(data_now[0]))
                
            #Se não, só calcula até o proximo dia:
            else:
                days = int(data_prog[0]) - int(data_now[0])
            
            #Se o dia/mês programado for menor que o dia atual, ele vai ficar negativo:
            if days < 0:
                
                #Então eu calcula aproximadamente, quanto que falta para o proximo ano:
                if len(days) == 2:
                    days = 370 - ((int(data_now[1]) -1) * 30 + int(data_now[0]))
                
                #Se tiver só o dia, calcula para o próximo mês
                else:
                    days = 33 - days
            
            #Calcula aproximadamente o segundos de 1 dias. Diferença de 400 segundos:
            secs = days * 86000
            
            #Tiver no dia, days será 0, nisto ele só vai esperar 60 segundos
            if days == 0:
                secs = 60
                
            
            #Se tiver mês e dia, esperará pelo mês antes:                                    
            if len(data_prog) == 2:
                #Se não for o mês correto, dormira até a data aproximada:
                if data_prog[1] != data_now[1]:
                    sleep(secs)

            #Mesma coisa, só agora com os dias:
            if data_prog[0] == data_now[0]:
                
                #Mesma coisa, com as horas:
                if tempo_now[0] == tempo_prog[0]:
                    
                    #Agora, com os minutos:
                    if tempo_now[1] == tempo_prog[1]:
                        print('Tempo esgotato, começando a enviar o E-mail!')
                        break
                    
                    #Para o minuto errado, somente dorme por 1 segundo:
                    else:
                        sleep(1)
                        
                #Para a hora errado, somente dorme por 60 segundos:
                else:
                    sleep(60)

            #Para o dia errado, somente dormepelo tempo aproximado até a data:
            else:
                sleep(secs)

    
    #Se o úsuario colocou um numero válido acima de 0, repetira isto com o for.
    #Caso ele tenha colocado 0, reepetirá com while:
    if repeat == 0:
        print('\nEsperando o tempo certo...')
        while True:
            wait_send()        
        
    else:
        print('\nEsperando o tempo certo...')
        for i in range(repeat):
            wait_send()

time_send()