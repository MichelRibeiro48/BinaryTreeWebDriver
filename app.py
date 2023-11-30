from collections import deque
import functools
import pprint
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions

#A classe By é usada para localizar elementos dentro de um documento.
from selenium.webdriver.common.by import By
import time

#Preparando Função para testar a arvore binaria

def OrderBinaryList(numeros): 
  lista = numeros.split('(')
  lista = [s.strip(')') for s in lista]
  lista.pop(0)
  lista = [int(s) for s in lista]
  return lista

#Preparando função para comparar lista da arvore binaria em python com a do site
def compareLists(lista1, numeros2): 
  lista2 = numeros2.split(', ')
  lista2 = [int(s) for s in lista2]
  if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,lista2,lista1), True):
    return True
  else:
    return False

#Criando arvore binaria em python
class Node:
   def __init__(self, data):
      self.left = None
      self.right = None
      self.data = data
   def insert(self, data):
      if self.data:
         if data < self.data:
            if self.left is None:
               self.left = Node(data)
            else:
               self.left.insert(data)
         elif data > self.data:
            if self.right is None:
               self.right = Node(data)
            else:
               self.right.insert(data)
         else:
            self.data = data
   def PreorderTraversal(self, root):
      res = []
      if root:
         res.append(root.data)
         res = res + self.PreorderTraversal(root.left)
         res = res + self.PreorderTraversal(root.right)
      return res
   def PostorderTraversal(self, root):
    res = []
    if root:
      res = self.PostorderTraversal(root.left)
      res = res + self.PostorderTraversal(root.right)
      res.append(root.data)
    return res
   def inOrderTraversal(self, root):
      res = []
      if root:
         res = self.inOrderTraversal(root.left)
         res.append(root.data)
         res = res + self.inOrderTraversal(root.right)
      return res
   def BFSTraversal(self, root):
        if root is None:
            return []

        res = []
        queue = deque()
        queue.append(root)

        while queue:
            current_node = queue.popleft()
            res.append(current_node.data)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return res
   
#Função para clicar em botões
def clickInButton(value):
   button = driver.find_element(by=By.XPATH, value=value)
   button.click()
   time.sleep(3)

#Função para comparar textos do site com o esperado passado no parametro
def checkExpectedText(xpathText,expectedText):
   Text = driver.find_element(by=By.XPATH, value=xpathText).text
   assert Text == expectedText
   time.sleep(3)

#Função para comparar a arvore binaria do site é igual com a arvore realizada em python
def compareBinaryTree(treeSite, TreeOrderSite, funcOrder):
   treeInString = driver.find_element(by=By.XPATH, value=treeSite).text
   siteOrderInString = driver.find_element(by=By.XPATH, value=TreeOrderSite).text
   novalista = OrderBinaryList(treeInString)
   root = Node(novalista[0])
   def defineNode():
      if funcOrder == 'Pre':
         return root.PreorderTraversal(root)
      if funcOrder == 'In':
        return root.inOrderTraversal(root)
      if funcOrder == 'Post':
         return root.PostorderTraversal(root)
      if funcOrder == 'BFS':
         return root.BFSTraversal(root) 
   for i in range(len(novalista)):
      root.insert(novalista[i])
   print("ordenação feita pelo python",defineNode())
   print("ordenação feita pelo site",siteOrderInString)
   assert compareLists(defineNode(), siteOrderInString) == True
   time.sleep(3)

coverage = {}
# Instanciando o driver do Edge
driver = webdriver.Edge()

#O método driver.get navegará para uma página fornecida pela URL.
driver.get("https://binarytreevisualiser.vercel.app/")

#A próxima linha é uma afirmação para confirmar que o título contém a palavra “Binary Tree | Home”:
title = driver.title
assert title == "Binary Tree | Home"
coverage.update({'TitlePage': 'Ok'})

#Deixando em tela cheia
driver.maximize_window()
time.sleep(3)

#Testando o botão do github
clickInButton('//*[@id="__next"]/div/div[1]/header/a[2]/img')

#Voltando para o binary tree
windowBefore = driver.window_handles[0]
driver.switch_to.window(windowBefore)
time.sleep(3)
coverage.update({'GitHub Project': 'Ok'})

#Clicando no botão create tree quando não foi preenchido o campo de inserir nó
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[1]')

#Verificando se aparece um alerta de notificação para o usuário preencher o nó
alert = driver.switch_to.alert
text = alert.text
assert text == "Enter the number of nodes"
coverage.update({'Empty Nodes Alert': 'Ok'})
alert.dismiss()

#Colocando numero 5 no campo "number of nodes"
inputField = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/input')
inputField.send_keys('5')
time.sleep(3)
coverage.update({'Input Node': 'Ok'})

#Clicando em Create Tree
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[1]')
coverage.update({'Button Create Tree': 'Ok'})

#Checando se aparece Tree created no historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/h3', 'Tree created')
coverage.update({'History Create Tree': 'Ok'})

#Clicando no botão PreOrder
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[2]')
coverage.update({'Button Pre Order': 'Ok'})

#Checando se aparece Pre Order no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[3]/h3', 'Pre order')
coverage.update({'History Pre Order ': 'Ok'})

#Checando se a arvore foi ordenada corretamente em Pre Order
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[3]/p', 'Pre')
coverage.update({'Algorithm Pre Order': 'Ok'})

#Clicando no botão InOrder
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[3]')
coverage.update({'Button In Order': 'Ok'})

#Checando se aparece In Order no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/h3', 'In order')
coverage.update({'History In Order': 'Ok'})

#Checando se a arvore foi ordenada corretamente em In Order
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/p', 'In')
coverage.update({'Algorithm In Order': 'Ok'})

#Clicando no botão PostOrder
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[4]')
coverage.update({'Button Post Order': 'Ok'})

#Checando se aparece Post Order no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[5]/h3', 'Post order')
coverage.update({'History Post Order': 'Ok'})

#Checando se a arvore foi ordenada corretamente em Post Order
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[5]/p', 'Post')
coverage.update({'Algorithm Post Order': 'Ok'})

#Clicando no botão Breadth-first search
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[5]')
coverage.update({'Button BFS': 'Ok'})

#Checando se aparece Breadth-first search no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/h3', 'Breadth-first search')
coverage.update({'History BFS': 'Ok'})

#Checando se a arvore foi ordenada corretamente em BFS
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/p', 'BFS')
coverage.update({'Algorithm BFS': 'Ok'})

#Clicando no botão Staff
clickInButton('//*[@id="__next"]/div/nav/a[2]')
coverage.update({'Button Staff': 'Ok'})

#Clicando nas redes sociais do Michel
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[1]/div/a')
coverage.update({'Button Michel GitHub': 'Ok'})

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais do Denis
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[1]')
coverage.update({'Button Denis GitHub': 'Ok'})

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais do Denis
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[2]')
coverage.update({'Button Denis Linkedin': 'Ok'})

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais da Laiça
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[3]/div/a')
coverage.update({'Button Laiça Instagram': 'Ok'})

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando no titulo BinaryTree
clickInButton('//*[@id="__next"]/div/div[1]/header/a[1]')
coverage.update({'Button Logo Binary Tree': 'Ok'})

pprint.pprint(coverage)
# Fechar o navegador
driver.quit()