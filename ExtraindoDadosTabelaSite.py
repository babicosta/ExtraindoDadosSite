from selenium import webdriver as opcoesSelenium
from selenium.webdriver.common.by import By
import pyautogui

navegador = opcoesSelenium.Chrome()

#Abrindo site
navegador.get('https://rpachallengeocr.azurewebsites.net/')

#Inspecionando a tabela
elementoTabela = navegador.find_element(By.XPATH, '//*[@id="tableSandbox"]')
pyautogui.sleep(2)

linhas = elementoTabela.find_elements(By.TAG_NAME, 'tr')
colunas = elementoTabela.find_elements(By.TAG_NAME, 'td')
pyautogui.sleep(2)

linha = 1
for linhaAtual in linhas:

    print((linhaAtual.text))
    linha = linha + 1


navegador.close()