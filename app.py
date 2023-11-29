from selenium import webdriver

# Usada para gerenciar automaticamente os drivers do navegador
from webdriver_manager.chrome import ChromeDriverManager

#A classe Keys fornece teclas no teclado como RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

#A classe By é usada para localizar elementos dentro de um documento.
from selenium.webdriver.common.by import By
import time

# Instanciando o driver do Edge

driver = webdriver.Edge()

#O método driver.get navegará para uma página fornecida pela URL.
driver.get("https://binarytreevisualiser.vercel.app/")

#A próxima linha é uma afirmação para confirmar que o título contém a palavra “Binary Tree | Home”:
title = driver.title
assert title == "Binary Tree | Home"

#Deixando em tela cheia
driver.maximize_window()
time.sleep(3)

#Testando o botão do github
projectGitButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/header/a[2]/img')
projectGitButton.click()
time.sleep(3)

#Voltando para o binary tree
windowBefore = driver.window_handles[0]
driver.switch_to.window(windowBefore)
time.sleep(3)

#Colocando numero 5 no campo "number of nodes"
inputField = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/input')
inputField.send_keys('5')
time.sleep(3)

#Clicando em Create Tree
createTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[1]')
createTreeButton.click()
time.sleep(3)

#Checando se aparece Tree created no historico
titleTreeCreated = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/h3').text
assert titleTreeCreated == 'Tree created'
time.sleep(3)

#Clicando no botão PreOrder
PreOrderTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[2]')
PreOrderTreeButton.click()
time.sleep(3)

#Checando se aparece Pre Order no Historico
titlePreOrderHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[3]/h3').text
assert titlePreOrderHistory == 'Pre order'
time.sleep(3)

#Clicando no botão InOrder
InTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[3]')
InTreeButton.click()
time.sleep(3)

#Checando se aparece In Order no Historico
titleInOrderHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/h3').text
assert titlePreOrderHistory == 'In order'
time.sleep(3)

#Clicando no botão PostOrder
PostTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[4]')
PostTreeButton.click()
time.sleep(3)

#Checando se aparece Post Order no Historico
titleInOrderHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/h3').text
assert titlePreOrderHistory == 'Post order'
time.sleep(3)

#Clicando no botão Breadth-first search
BreadthFirstTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[5]')
BreadthFirstTreeButton.click()
time.sleep(3)

#Checando se aparece Breadth-first search no Historico
titleInOrderHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/h3').text
assert titlePreOrderHistory == 'Breadth-first search'
time.sleep(3)

#Clicando no botão Staff
StaffButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/nav/a[2]')
StaffButton.click()
time.sleep(3)

#Clicando nas redes sociais do Michel
MichelGitLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[1]/div/a')
MichelGitLink.click()
time.sleep(3)

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais do Denis
DenisGitLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[1]')
DenisGitLink.click()
time.sleep(3)

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais do Denis
DenisLinkedInLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[2]')
DenisLinkedInLink.click()
time.sleep(3)

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais da Laiça
laicaInstaLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[3]/div/a')
laicaInstaLink.click()
time.sleep(3)

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando no titulo BinaryTree
logoBinaryTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/header/a[1]')
logoBinaryTreeButton.click()
time.sleep(3)

# Fechar o navegador
driver.quit()