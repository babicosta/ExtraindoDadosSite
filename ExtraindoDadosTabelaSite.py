from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui
import pandas as pd

navegador = opcoesSelenium.Chrome()

#Abrindo site
navegador.get('https://rpachallengeocr.azurewebsites.net/')

listaDataFrame = []
linha = 1
i = 1

while i < 4:
    elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')

    linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
    colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')
    pyautogui.sleep(2)

    for linhaAtual in linhas:
        print(linhaAtual.text)
        listaDataFrame.append(linhaAtual.text)

        linha = linha + 1

    i = i + 1

    pyautogui.sleep(2)

    navegador.find_element(By.XPATH, '//*[@id="tableSandbox_next"]').click()
    pyautogui.sleep(2)

else:

    print('Dados extraidos com sucesso!')

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')
arquivoExcel.close()

dataFrame = pd.DataFrame(listaDataFrame, columns=['#; ID; Due Date'])

arquivoExcel = pd.ExcelWriter('dadosAbasSite.xlsx', engine='xlsxwriter')

dataFrame.to_excel(arquivoExcel, sheet_name='Dados', index=False)

arquivoExcel.close()

