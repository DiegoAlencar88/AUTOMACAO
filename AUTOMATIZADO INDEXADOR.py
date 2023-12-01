#VARIAVEIS 

import pyautogui
import time

#OLHAR NA PLANILHA CSV QUAL LINHA DEVERA SER INICIADO O LANÇAMENTO
linha_atual =0

#TEMPO PARA STARTAR CODIGO "ENTRE PARENTES COLOQUE O VALOR"
time.sleep(3)

#QUANTIDADE DE VEZES QUE IRA RODAR O COD
for _ in range(20):
    #VELOCIDADE DE CADA LANÇAMENTO
    time.sleep(0.1)

      

    #CRIAR O VINCULO COM A PLANILHA 
    import pandas as pd

    
    #ENTRE ASPAS DIGITE O NOME DA PLANILHA SALVA EM CSV
    tabela = pd.read_csv("nomeplanilha.csv", sep=";")

    for linha in tabela.index:
        #NO ARQUIVO CSV ALTERAR O NOME DA COLUNA QUE IRA SER LANÇADA PARA Lancar
        Lancar = tabela.loc[linha_atual, "Lancar"]
    pyautogui.write(str(Lancar))
        
    pyautogui.press("tab")

    linha_atual += 1

