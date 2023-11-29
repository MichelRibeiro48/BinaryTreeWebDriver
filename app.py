from collections import deque
import functools
from selenium import webdriver

# Usada para gerenciar automaticamente os drivers do navegador
from webdriver_manager.chrome import ChromeDriverManager

#A classe Keys fornece teclas no teclado como RETURN, F1, ALT etc.
from selenium.webdriver.common.keys import Keys

#A classe By é usada para localizar elementos dentro de um documento.
from selenium.webdriver.common.by import By
import time

#Preparando Função para testar a arvore binaria]

def OrdenarListaArvore(numeros): 
  lista = numeros.split('(')
  lista = [s.strip(')') for s in lista]
  lista.pop(0)
  lista = [int(s) for s in lista]
  return lista
# novalista = OrdenarListaArvore('(87(48(37))(98))')

def compararListas(lista1, numeros2): 
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
# Insert Node
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
   def PrintTree(self):
      if self.left:
         self.left.PrintTree()
      print( self.data),
      if self.right:
         self.right.PrintTree()
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

#Checando se a arvore foi ordenada corretamente em Pre Order
treeInString = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[1]/p').text
preOrderInString = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[3]/p').text
novalista = OrdenarListaArvore(treeInString)
root = Node(novalista[0])
for i in range(len(novalista)):
   root.insert(novalista[i])
assert compararListas(root.PreorderTraversal(root), preOrderInString) == True
print("ordenação feita pelo python",root.PreorderTraversal(root))
print("ordenação feita pelo site",preOrderInString)
time.sleep(3)

#Clicando no botão InOrder
InTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[3]')
InTreeButton.click()
time.sleep(3)

#Checando se aparece In Order no Historico
titleInOrderHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/h3').text
assert titleInOrderHistory == 'In order'
time.sleep(3)

#Checando se a arvore foi ordenada corretamente em In Order
InOrderInString = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[4]/p').text
root = Node(novalista[0])
for i in range(len(novalista)):
   root.insert(novalista[i])
assert compararListas(root.inOrderTraversal(root), InOrderInString) == True
print("ordenação feita pelo python", root.inOrderTraversal(root))
print("ordenação feita pelo site", InOrderInString)
time.sleep(3)

#Clicando no botão PostOrder
PostTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[4]')
PostTreeButton.click()
time.sleep(3)

#Checando se aparece Post Order no Historico
titlePostOrderHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[5]/h3').text
assert titlePostOrderHistory == 'Post order'
time.sleep(3)

#Checando se a arvore foi ordenada corretamente em Post Order
postOrderInString = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[5]/p').text
root = Node(novalista[0])
for i in range(len(novalista)):
   root.insert(novalista[i])
assert compararListas(root.PostorderTraversal(root), postOrderInString) == True
print("ordenação feita pelo python",root.PostorderTraversal(root))
print("ordenação feita pelo site",postOrderInString)
time.sleep(3)

#Clicando no botão Breadth-first search
BreadthFirstTreeButton = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[1]/button[5]')
BreadthFirstTreeButton.click()
time.sleep(3)

#Checando se aparece Breadth-first search no Historico
titleBreadthFirstHistory = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/h3').text
assert titleBreadthFirstHistory == 'Breadth-first search'
time.sleep(3)

#Checando se a arvore foi ordenada corretamente em BFS
BFSInString = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div/div[2]/div[3]/ul/li[6]/p').text
root = Node(novalista[0])
for i in range(len(novalista)):
   root.insert(novalista[i])
assert compararListas(root.BFSTraversal(root), BFSInString) == True
print("ordenação feita pelo python",root.BFSTraversal(root))
print("ordenação feita pelo site",BFSInString)
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