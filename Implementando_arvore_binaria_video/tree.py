import random
from collections import deque


class Node :
    # definição do que é nó com direita e esquerda:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str (self.data)


class BinaryTree:
    # definição da arvore:
    def __init__(self,data=None, node = None):
        if node:
            self.root = node
        elif data:
            node = Node(data)
            self.root = node
        else:
            self.root = None

    # percurso em ordem simetrica:
    def simetric_traversal(self, node = None):
        
        # se o nó for vasio percorra a partir da raiz 
        if node is None:
            node = self.root
        if node.left:
            print("(" , end="")
            self.simetric_traversal(node.left)
        
        print(node , end="")

        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")

    #percurso em pós ordem:
    def postorder_traversal(self, node=None):
        if node is None :
            node = self.root
        if node.left :
            self.postorder_traversal(node.left)
        if node.right:
            self.postorder_traversal(node.right)
        print(node)    

    # calcular altura da arvore 
    def hight(self, node=None):
        if node is None :
            node = self.root
        hleft = 0
        hright = 0   
        if node.left :
            hleft = self.hight(node.left)
        if node.right:
            hright = self.hight(node.right)

        if hright > hleft :
            return hright +1
        return hleft+1

# arvore binária de busca:
class BinarySearchTree(BinaryTree):
    # função insere :
    def insert(self , value):
        parent = None
        x = self.root
        while(x):
            parent = x
            if value < x.data :
                x = x.left
            else:
                x = x.right
        if parent is None :
            self.root = Node(value)
        elif value < parent.data :
            parent.left = Node(value)

        else:
            parent.right = Node(value)
    
    # função de busca :
    def search (self, value , node = 0 ):
        if node == 0 :
            node = self.root
        if node is None or node.data == value:
            return BinarySearchTree(node)
        if value < node.data:
            return self.search(value, node.left)
        return self.search(value,node.right )
    
    def inorder_traversal(self , node = None):
        if node is None:
            node = self.root
        if node.left:
            self.inorder_traversal(node.left)      
        print(node , end=" ")
        if node.right:
            self.inorder_traversal(node.right) 

    # Função contem usando o search 
    def contem(self, value):
        result = self.search(value)
        if result.root is not None:
            print(f"O número {value} está na árvore.")
        else:
            print(f"O número {value} não está na árvore.")

    # função que gera a lista da arvore
    def geraLista(self , node=0):
        lista =[]
        if node == 0 :
            node = self.root
        if node == None:
            print("arvore vazia")
        if not node.left == None :
            lista = self.geraLista(node.left)
        lista.append (node.data)
        if not node.right == None:
            lista.extend(self.geraLista(node.right))
        
        return lista 
    
    def min ( self , node = 0 ):
        if node ==0 :
            node = self.root
        while node.left:
            node = node.left
        return node.data

    def max ( self , node = 0 ):
        if node ==0 :
            node = self.root
        while node.right:
            node = node.right 
        return node.data

    def remove(self , value , node =0 ):
        if node == 0:
            node = self.root
        if node == None :
            print ("arvore vazia") 
        # remove folha
        if value < node.data:
            node.left = self.remove(value , node.left)
        elif value > node.data:
            node.right = self.remove(value , node.right)
        else :
            # 1 filho
            if node.left is None :
                return node.right
            elif node.right is None:
                return node.left
            # 2 filhos
            else : 
                substituto = self.min(node.right)
                node.data = substituto
                node.right = self.remove(substituto , node.right)
        return node
    
    # rotação para direita 
    def rotacao_direita(self, node):
        if node is None or node.left is None:
            return node  # Não pode rotacionar se não houver filho esquerdo

        new_root = node.left
        node.left = new_root.right
        new_root.right = node

        return new_root

    def balance_from_list(self):
    #Criar lista ordenada com os elementos
        lista = self.geraLista()

    #Construir árvore balanceada a partir da lista
        def construir_arvore(lista):
            if not lista:
                return None
            meio = len(lista) // 2
            novo_no = Node(lista[meio])  # Escolhe o nó do meio como raiz
            novo_no.left = construir_arvore(lista[:meio])  # Subárvore esquerda
            novo_no.right = construir_arvore(lista[meio + 1:])  # Subárvore direita
            return novo_no
        self.root = construir_arvore(lista)

    def print_tree_structure(self):
        if self.root is None:
            print("Árvore vazia")
            return
        
        queue = deque([(self.root, 0)])  # Fila para BFS (nó, nível)
        current_level = 0
        level_nodes = []
    
        while queue:
            node, level = queue.popleft()
        
            if level != current_level:  # Mudança de nível
                print(" | ".join(level_nodes))  # Imprime a linha anterior
                level_nodes = []
                current_level = level
        
            level_nodes.append(str(node.data))
        
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
    
        print(" | ".join(level_nodes))  # Imprime o último nível

#testes:

arvore = BinarySearchTree()

for val in [1,2,3,4,5,6,7,8,9,10]:
    arvore.insert(val)

lista = arvore.geraLista()
print(lista)

listaNova=arvore.geraLista()
print (listaNova)

arvore.print_tree_structure()

print("agora a arvore balanceada:")
arvore.balance_from_list()
arvore.print_tree_structure()




