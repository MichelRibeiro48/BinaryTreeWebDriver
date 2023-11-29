from selenium import webdriver

# Usada para gerenciar automaticamente os drivers do navegador
from webdriver_manager.chrome import ChromeDriverManager

#A classe Keys fornece teclas no teclado como RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

#A classe By é usada para localizar elementos dentro de um documento.
from selenium.webdriver.common.by import By
import time

# Instanciando o driver do Chrome

driver = webdriver.Edge()

#O método driver.get navegará para uma página fornecida pela URL.
driver.get("https://binarytreevisualiser.vercel.app/")

#A próxima linha é uma afirmação para confirmar que o título contém a palavra “Web Form”:
title = driver.title
assert title == "Binary Tree | Home"

driver.maximize_window()
time.sleep(3)

projectGitButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/header/a[2]/img')
projectGitButton.click()
time.sleep(3)

windowBefore = driver.window_handles[0]
driver.switch_to.window(windowBefore)
time.sleep(3)

inputField = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/input')
inputField.send_keys('5')
time.sleep(3)

createTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[1]')
createTreeButton.click()
time.sleep(3)

titleTreeCreated = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/h3').text
assert titleTreeCreated == 'Tree created'
time.sleep(3)

PreInTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[2]')
PreInTreeButton.click()
time.sleep(3)

InTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[3]')
InTreeButton.click()
time.sleep(3)

PostTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[4]')
PostTreeButton.click()
time.sleep(3)

BreadthFirstTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[5]')
BreadthFirstTreeButton.click()
time.sleep(3)

StaffButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/nav/a[2]')
StaffButton.click()
time.sleep(3)

MichelGitLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[1]/div/a')
MichelGitLink.click()
time.sleep(3)

driver.back()
time.sleep(3)

DenisGitLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[1]')
DenisGitLink.click()
time.sleep(3)

driver.back()
time.sleep(3)

DenisLinkedInLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[2]')
DenisLinkedInLink.click()
time.sleep(3)

driver.back()
time.sleep(3)

laicaInstaLink = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/ul/li[3]/div/a')
laicaInstaLink.click()
time.sleep(3)

driver.back()
time.sleep(3)

logoBinaryTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[1]/header/a[1]')
logoBinaryTreeButton.click()
time.sleep(3)







# expandTree = driver.find_element(by=By.XPATH, value='//*[@id="treeWrapper"]/button')
# expandTree.click()
# time.sleep(3)

# closeExpandTree = driver.find_element(by=By.CSS_SELECTOR, value='#treeWrapper > button > svg > line:nth-child(1)')
# closeExpandTree.click()
# time.sleep(3)

# Fechar o navegador
driver.quit()