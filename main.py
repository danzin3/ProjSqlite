import item_lista # Módulo que contém a classe Item, usado no programa

from lista_controller import controller # Variável que controla as operações entre a lista e o banco de dados

lista = []

try:    
    arq = open('words.txt','r',encoding='utf-8') #Abre o arquivo para leitura
    arq.seek(0) # Realinha o ponteiro no arquivo na posição 0
    for linha in arq:
        linha = linha.rstrip() #Retira o caractere final '\n' da linha
        vet = linha.split(' ') #Divide a linha em duas partes
        objIten = item_lista.Item() #Instancia um objeto do tipo Item
        objIten.palavra = vet[0]
        objIten.significado = vet[1]
        lista.append(objIten) #Insere o objeto instanciado na lista
    arq.close()
except Exception as e:
    print("Erro ao abrir o arquivo!\n",e)

for item in lista:
    controller.inserirItens(item) #Insere um item da lista por vez

controller.listarItens(len(lista)) # parametro desse método é o limite de tuplas para se mostrar

controller.closeCon() # Fecha a conexão com o banco pelo controller

"""
Outra forma de fazer esse código:

class Item:
    def __init__(self, palavra, significado):
        self.palavra = palavra
        self.significado = significado

try:
    with open('words.txt', encoding='utf-8') as arq:
        lista = [Item(*linha.rstrip().split()) for linha in arq]

    for item in lista:
        print(f'{item.palavra} => {item.significado}')

except OSError as e:
    print("Erro ao abrir o arquivo: ", e)

"""