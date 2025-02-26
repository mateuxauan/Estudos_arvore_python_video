import random


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




# teste :

# if  __name__ == "__main__" :
    # tree = BinaryTree(7)
    # tree.root.left = Node(18)
    # tree.root.right = Node(14)

    # print(tree.root)
    # print(tree.root.left)
    # print(tree.root.right)

    
    # tree = BinaryTree()
    # n1=Node('i')
    # n2=Node('n')
    # n3=Node('s')
    # n4=Node('c')
    # n5=Node('r')
    # n6=Node('e')
    # n7=Node('v')
    # n8=Node('a')
    # n9=Node('s')
    # n10=Node('e')
    # n11=Node("-")

    # n6.left = n1
    # n6.right = n5
    # n5.left = n2
    # n5.right = n4
    # n4.right = n3
    # n9.left = n8
    # n8.right = n7
    # n10.left = n6
    # n10.right = n9
    # n9.right = n11

    # tree.root = n10

    # tree.simetric_traversal()
    # print("agora a pos ordem")
    # tree.postorder_traversal() 
    # print( "altura é : ", tree.hight())


# forma de arvore:
#
#
#                  'e'
#             /          \
#           'e'           's'
#          /   \         /   \ 
#        'i'   'r'      'a'   '-'
#              /  \       \ 
#            'n'   'c'     'v'
#                    \
#                    's'
#
#
#
# forma linear:
#
# ((ie(nrcs)))e(av)s-))         


arvore = BinarySearchTree()



for val in [2,4,7,1,8,9]:
    arvore.insert(val)


lista = arvore.geraLista()
print(lista)
arvore.remove(4)
listaNova=arvore.geraLista()
print (listaNova)

