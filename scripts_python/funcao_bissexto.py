def verificador_ano_bissexto():
    ano = int(input())


    if len(str(ano)) == 4 and ((ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0):    
        print('SIM')
    else:
        print('NÃO')

verificador_ano_bissexto()