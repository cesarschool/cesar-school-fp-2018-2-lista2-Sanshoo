## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    anobissexto = bool(False)
    ano = int(input("digite o ano da data desejada: "))
    mes = int(input("digite o mes da data desejada: "))
    dia = int(input("digite o mes da data desejada: "))
    if (ano % 4) == 0:
        if (ano % 100) == 0:
            if (ano % 400) == 0:
                anobissexto = True
            else:
                anobissexto = False
        else:
            anobissexto = True
    else:
        anobissexto = False

    if anobissexto == False:
        if mes == 1:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 2:
            if (dia == 28):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 3:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 4:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 5:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 6:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 7:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 8:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 9:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 10:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 11:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 12:
            if (dia == 31):   
                dia = 1
                mes = 1
                ano = ano+1
            
            else:
                dia = dia+1
    elif anobissexto == True:
        if mes == 1:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 2:
            if (dia == 29):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 3:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 4:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 5:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 6:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 7:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 8:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 9:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 10:
            if (dia == 31):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 11:
            if (dia == 30):   
                dia = 1
                mes = mes+1
            
            else:
                dia = dia+1
        elif mes == 12:
            if (dia == 31):   
                dia = 1
                mes = 1
                ano = ano+1
            
            else:
                dia = dia+1
                
    print(str(ano) + "-" + str(mes) + "-" + str(dia))


    
if __name__ == '__main__':
    main()
