from collections import deque
import functools
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
   
def clickInButton(value):
   button = driver.find_element(by=By.XPATH, value=value)
   button.click()
   time.sleep(3)

def checkExpectedText(xpathText,expectedText):
   Text = driver.find_element(by=By.XPATH, value=xpathText).text
   assert Text == expectedText
   time.sleep(3)

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
clickInButton('//*[@id="__next"]/div/div[1]/header/a[2]/img')

#Voltando para o binary tree
windowBefore = driver.window_handles[0]
driver.switch_to.window(windowBefore)
time.sleep(3)

#Clicando no botão create tree quando não foi preenchido o campo de inserir nó
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[1]')

#Verificando se aparece um alerta de notificação para o usuário preencher o nó
alert = driver.switch_to.alert
text = alert.text
assert text == "Enter the number of nodes"
alert.dismiss()

#Colocando numero 5 no campo "number of nodes"
inputField = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/input')
inputField.send_keys('5')
time.sleep(3)

#Clicando em Create Tree
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[1]')

#Checando se aparece Tree created no historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/h3', 'Tree created')

#Clicando no botão PreOrder
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[2]')

#Checando se aparece Pre Order no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[3]/h3', 'Pre order')

#Checando se a arvore foi ordenada corretamente em Pre Order
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[3]/p', 'Pre')

#Clicando no botão InOrder
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[3]')

#Checando se aparece In Order no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/h3', 'In order')

#Checando se a arvore foi ordenada corretamente em In Order
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/p', 'In')

#Clicando no botão PostOrder
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[4]')

#Checando se aparece Post Order no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[5]/h3', 'Post order')

#Checando se a arvore foi ordenada corretamente em Post Order
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[5]/p', 'Post')

#Clicando no botão Breadth-first search
clickInButton('//*[@id="__next"]/div/div[2]/div[1]/button[5]')

#Checando se aparece Breadth-first search no Historico
checkExpectedText('//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/h3', 'Breadth-first search')

#Checando se a arvore foi ordenada corretamente em BFS
compareBinaryTree('//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p', '//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/p', 'BFS')

#Clicando no botão Staff
clickInButton('//*[@id="__next"]/div/nav/a[2]')

#Clicando nas redes sociais do Michel
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[1]/div/a')

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais do Denis
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[1]')

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais do Denis
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[2]/div/a[2]')

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando nas redes sociais da Laiça
clickInButton('//*[@id="__next"]/div/div[2]/ul/li[3]/div/a')

#Voltando no historico
driver.back()
time.sleep(3)

#Clicando no titulo BinaryTree
clickInButton('//*[@id="__next"]/div/div[1]/header/a[1]')

# Fechar o navegador
driver.quit()