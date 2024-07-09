# ---------------------------------------------------Enquadramento------------------------------------------------------
# Trabalho 5
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
# Ano letivo 2020/2021- 2º Semestre
# Realizado por Sebastião Manuel Inácio Rosalino - n.º 98437 - Turma CDA1

# ---------------------------------------------------------------------------------------------------------------------
# Questão 2 - Implementação de uma lista ligada estritamente ordenada por ordem crescente

class Node:                                # Criação da classe Node(nó) que servirá de base à criação de classes listas
    def __init__(self, value, prev=None, next=None):  # As instâncias desta classe recebem um valor e um apontador
        self._value = value                           # para o anterior e próximo nó
        self._next = next                             # Elemento (next) inicializado a None
        self._prev = prev                             # Elemento (prev) inicializado a None

    @property
    def value(self):                      # Método para atribuir como propriedade a um nó o seu valor
        return self._value

    @value.setter
    def value(self, new_value):           # Método para permitir a alteração de um valor de um determinado nó
        self._value = new_value

    @property
    def next(self):                       # Método para atribuir como propriedade a um nó o seu próximo nó
        return self._next

    @property
    def prev(self):                       # Método para atribuir como propriedade a um nó o seu nó anterior
        return self._prev

    @next.setter
    def next(self, new_next):             # Método para permitir a alteração do próximo nó a um determinado nó
        self._next = new_next

    @prev.setter
    def prev(self, new_prev):             # Método para permitir a alteração do nó anterior a um determinado nó
        self._next = new_prev

    def __str__(self):                                      # Método para permitir o uso do comando print sobre os nós,
        return "Nó de valor: {}".format(self._value)        # retornando apenas o seu valor


# Utilização da ferramenta main para um teste simples a todas as capacidades da classe Node

if __name__ == "__main__":
    no_1 = Node(155)
    no_2 = Node(21)
    print(no_1)
    print(no_2)


class ListaLigadaEstritamenteCrescente:           # Criação de uma lista dinâmica ligada
    def __init__(self):
        self._head = None            # O elemento head representa o primeiro nó, devendo começar a None
        self._size = 0               # O elemento size representa o tamanho da lista, devendo começar a 0

    def __len__(self):               # Método para uso do comando len sobre a lista retornando o seu tamanho
        return self._size

    def vazia(self):                 # Método para indicar se a lista está vazia
        return self._size == 0

    def limpar(self):                # Método para esvaziar a lista, colocando toda a lista com a sua estrutura inicial
        self._head = None
        self._size = 0
        print("Lista limpa.")

    def __str__(self):             # Método para permitir o uso do comando print sobre a lista mostrando o seu conteúdo
        current = self._head
        txt = "[ "
        while current is not None:
            txt += "{} ".format(current.value)
            current = current.next
            if current is not None:
                txt += ", "
            else:
                pass
        txt += "]"
        return txt

    def existe(self, item):               # Método para indicar se existe na lista um item com um dado valor
        current = self._head              # A variável current é atribuida ao primeiro nó (self._head)
        while current is not None:        # Enquanto existam elementos na lista, o ciclo while é executado
            if current.value == item:     # Caso encontremos o item, retorna True
                return True
            current = current.next        # Caso contrário, avança na pesquisa
        return False                      # Caso não tenha encontrado o elemento, retorna False

    def ver_p(self, pos):                # Método para consultar elemento numa determinada posição
        if pos < 0 or pos >= self._size:          # Só faz sentido pesquisar em posições válidas
            raise IndexError("Posição inválida")  # Caso o utilizador introduza uma posição inválida, lança-se um erro
        current = self._head                      # A variável current é atribuida ao primeiro nó (self._head)
        while pos > 0:                           # Enquanto a posição for superior a 0 o ciclo while é executado
            current = current.next                # Avança na pesquisa
            pos -= 1                              # A cada iteração a posição é reduzida em 1
        print("O elemento é", current.value)
        return current.value                      # Retorna o valor correspondente ao nó em questão

    def ver_min(self):                  # Método para consultar o menor elemento da lista
        return self.ver_p(0)            # Retorna o elemento na posição 0, já que a lista está ordenada

    def ver_max(self):                  # Método para consultar o maior elemento da lista
        return self.ver_p(self._size-1)   # Retorna o elemento na última posição, já que a lista está ordenada

    # Método auxiliar para ordenar de forma crescente a lista - não utilizado nos métodos de inserção e remoção
    def sort_list(self):
        current = self._head            # A variável current é atribuida ao primeiro nó (self._head)
        while current is not None:      # Enquanto existam elementos na lista, o ciclo while é executado
            index = current.next        # A variável index é atribuida ao próximo nó
            while index is not None:    # Enquanto exista um próximo nó
                if current.value > index.value:     # Caso o valor atual seja superior ao do próximo nó
                    temp = current.value            # Os nós são trocados
                    current.value = index.value
                    index.value = temp
                index = index.next
            current = current.next       # Tanto o próximo nó como o nó atual avançam na pesquisa

    def ins(self, item):            # Método para inserir um dado item na lista
        if self.existe(item):       # Não podem existir elementos repetidos na lista
            raise ValueError("Este número já existe, tente de novo.")  # Caso haja, lança-se um erro
        current = self._head        # A variável current é atribuida ao primeiro nó da lista
        anterior = None             # A variável anterior é inicialmente atribuida a None
        stop = False                # A indicação de paragem começa a False
        self._size += 1    # Caso este elemento seja único, significa que vai ser inserido, incrementando o tamanho em 1
        while current is not None and not stop:  # Enquanto existam elementos na lista e ainda não for altura de parar
            if current.value > item:    # Caso o valor do nó em análise for superior ao item a colocar
                stop = True          # Significa que esta lista tinha apenas 1 elemento, portanto a paragem passa a True
            else:                    # Se o valor do nó em análise for inferior ao item a colocar
                anterior = current   # O anterior passa a ser o nó em análise naquele momento
                current = current.next  # E o current avança na navegação da lista
        new_node = Node(item)     # Quando se sai do ciclo, é então criado um nó com o item dado em input
        if anterior is None:      # Se o anterior for None
            new_node.next = self._head  # O nó a inserir passará a ser a cabeça da lista
            self._head = new_node
        else:                     # Se o anterior não for None
            new_node.next = current   # O apontador next do novo nó passará a apontar para o current
            anterior.next = new_node  # E, por fim, o apontador next do nó anterior passará a apontar para o novo nó

    #   Método alternativo menos eficiente utilizando o método sort_list definido acima
    '''
    def ins(self, item):               # Método para inserir um dado item na lista
        if self.existe(item):          # Não podem existir elementos repetidos na lista
            raise ValueError("Este número já existe, tente de novo.")   # Caso haja, lança-se um erro
        else:
            tmp = Node(item)           # É criado um nó com o valor inserido
            tmp.next = self._head
            self._head = tmp           # Este nó é passado para a primeira posição, sendo agora o self._head
            self.sort_list()           # A lista é ordenada por ordem crescente
            self._size += 1            # O tamanho é incrementado em 1 posição
            print("Elemento inserido com sucesso.")    # Mensagem informativa
    '''

    def rem(self, item):               # Método para retirar um determinado item
        current = self._head           # A variável current é atribuida ao primeiro nó (self._head)
        ant = current.prev             # A variável ant é atribuida ao nó anterior
        encontrou = False              # A variável encontrou é iniciada a False
        while current is not None and not encontrou:  # Enquanto existam elementos e ainda não tenha sido encontrado
            if current.value == item:                # O ciclo é executado
                encontrou = True                     # Se for encontrado, encontrou passa a True, saindo assim do ciclo
            else:
                ant = current                         # Caso contrário, o nó anterior passa a ser o nó que foi analisado
                current = current.next                # E o novo nó é o próximo àquele que foi analisado
        if encontrou:
            if ant is None:                          # Se for encontrado e o anterior for None é porque era o primeiro
                self._head = current.next            # A cabeça passa a ser o próximo nó
            else:                                     # Se o anterior não for None
                ant.next = current.next               # O apontador do anterior passa a apontar para próximo nó
            print("Elemento retirado com sucesso.")   # Mensagem informativa
            self._size -= 1                           # O tamanho da lista é reduzido em 1
        else:
            print("A lista não contém o elemento que procura.")    # O utilizador é informado que o elemento não existe

    def rem_min(self):                  # Método para retirar o item com menor valor
        if self.vazia():                # Tal só é possível se a lista não estiver vazia
            print("A lista está vazia!")    # Caso esteja, mensagem informativa
        else:
            minimo = self.ver_min()
            self.rem(minimo)    # Caso contrário, o método rem é utilizado sobre o minimo elemento
            print("O menor elemento que era, ", minimo, " foi removido.")   # Mensagem informativa

    def rem_max(self):                  # Método para retirar o item com maior valor
        if self.vazia():                # Tal só é possível se a lista não estiver vazia
            print("A lista está vazia!")    # Caso esteja, mensagem informativa
        else:
            maximo = self.ver_max()
            self.rem(maximo)        # Caso contrário, o método rem é utilizado sobre o máximo elemento
            print("O maior elemento que era, ", maximo, " foi removido.")  # Mensagem informativa

    def abrir_menu(self):              # Método para abertura do menu de gestão da lista
        opcao = ""                     # A variável opção é iniciada a uma string vazia
        while opcao != "0":            # É disposto o seguinte menu de opções, sendo 0 a opção de saída do menu
            print("\n----- Bem-Vindo ao menu de gestão de lista -----\n")
            print("0. Sair do menu\n")
            print("1. Ver comprimento da lista (quantidade de itens)\n")
            print("2. Indicar se a lista está vazia\n")
            print("3. Esvaziar a lista\n")
            print("4. Mostrar o conteúdo da lista\n")
            print("5. Indicar se existe na lista um item com um dado valor\n")
            print("6. Consultar elemento numa dada posição\n")
            print("7. Consultar o menor elemento\n")
            print("8. Consultar o maior elemento\n")
            print("9. Inserir um dado item na lista\n")
            print("10. Retirar um dado item\n")
            print("11. Retirar o item com menor valor\n")
            print("12. Retirar o item com maior valor\n")
            opcao = input("Introduza a opção pretendida: \n")  # Após a disposição do menu é solicitada
            if opcao == "1":                                   # ao utilizador uma opção
                print(len(self))
            elif opcao == "2":
                if self.vazia():
                    print("Esta lista está vazia.")
                else:
                    print("Esta lista tem pelo menos um elemento.")
            elif opcao == "3":
                self.limpar()
            elif opcao == "4":
                print(self)
            elif opcao == "5":
                item_a_procurar = int(input("Indique o item a procurar: "))
                assert isinstance(item_a_procurar, int)      # Verifica que o item a procurar é um número inteiro
                if self.existe(item_a_procurar):
                    print("Este elemento está presente na lista")
                else:
                    print("Este elemento não existe na lista")
            elif opcao == "6":
                pos_a_procurar = int(input("Indique a posição a procurar: "))
                self.ver_p(pos_a_procurar)
            elif opcao == "7":
                self.ver_min()
            elif opcao == "8":
                self.ver_max()
            elif opcao == "9":
                item_a_inserir = int(input("Indique o item a inserir: "))
                if isinstance(item_a_inserir, int):      # Verifica que o item a inserir é um número inteiro
                    self.ins(item_a_inserir)
                    print("Elemento inserido com sucesso")
                else:
                    raise TypeError("Só podem ser inseridos números")
            elif opcao == "10":
                item_a_retirar = int(input("Indique o item a retirar: "))
                self.rem(item_a_retirar)
            elif opcao == "11":
                self.rem_min()
            elif opcao == "12":
                self.rem_max()
            elif opcao == "0":
                print("Obrigado")
            else:
                print("Opção inválida, tente de novo")


# Utilização da ferramenta main para um teste simples a todas as capacidades da lista

if __name__ == "__main__":
    lista_teste = ListaLigadaEstritamenteCrescente()
    print(lista_teste.vazia())
    lista_teste.ins(1)
    lista_teste.ins(56)
    print(lista_teste)
    print(lista_teste.vazia())
    lista_teste.limpar()
    print(lista_teste)
    lista_teste.ins(2)
    lista_teste.ins(57)
    print(lista_teste.existe(2))
    print(lista_teste.existe(90))
    lista_teste.ver_p(1)
    lista_teste.ver_min()
    lista_teste.ver_max()
    lista_teste.ins(36)
    lista_teste.rem(36)
    lista_teste.ins(-77)
    print(lista_teste)
    lista_teste.rem_min()
    lista_teste.rem_max()
    print(lista_teste)


# Criação da lista de valores 1,3,-1,82,-134,18,-13,0,-20,44 como lista de teste para uso das funcionalidades
# utilizando para tal o menu

lista_teste_menu = ListaLigadaEstritamenteCrescente()
lista_teste_menu.ins(1)
lista_teste_menu.ins(3)
lista_teste_menu.ins(-1)
lista_teste_menu.ins(82)
lista_teste_menu.ins(-134)
lista_teste_menu.ins(18)
lista_teste_menu.ins(-13)
lista_teste_menu.ins(0)
lista_teste_menu.ins(-20)
lista_teste_menu.ins(44)
lista_teste_menu.abrir_menu()    # Comando para apresentar a disposição do menu sempre que o ficheiro é corrido

# ------------------------------------------- fim da questão 2 ---------------------------------------------------------


# Questão 3 - Implementação por ordem crescente lata


class ListaLigadaCrescenteLata:           # Criação de uma lista dinâmica ligada
    def __init__(self):
        self._head = None           # O elemento head representa o primeiro nó, devendo começar a None
        self._size = 0              # O elemento size representa o tamanho da lista, devendo começar a 0

    def __len__(self):              # Método para uso do comando len sobre a lista retornando o seu tamanho
        return self._size

    def vazia(self):                # Método para indicar se a lista está vazia
        return self._size == 0

    def limpar(self):               # Método para esvaziar a lista, colocando toda a lista com a sua estrutura inicial
        self._head = None
        self._size = 0
        print("Lista limpa.")

    def __str__(self):             # Método para permitir o uso do comando print sobre a lista mostrando o seu conteúdo
        current = self._head
        txt = "[ "
        while current is not None:
            txt += "{} ".format(current.value)
            current = current.next
            if current is not None:
                txt += ", "
            else:
                pass
        txt += "]"
        return txt

    def existe(self, item):               # Método para indicar se existe na lista um item com um dado valor
        current = self._head              # A variável current é atribuida ao primeiro nó (self._head)
        while current is not None:        # Enquanto existam elementos na lista, o ciclo while é executado
            if current.value == item:     # Caso encontre o item retorna True
                return True
            current = current.next        # Caso contrário, avança na pesquisa
        return False                      # Caso não tenha encontrado o elemento retorna False

    def ver_p(self, pos):                # Método para consultar elemento numa determinada posição
        if pos < 0 or pos >= self._size:          # Só faz sentido pesquisar em posições válidas
            raise IndexError("Posição inválida")  # Caso o utilizador introduza uma posição inválida, lança-se um erro
        current = self._head                      # A variável current é atribuida ao primeiro nó (self._head)
        while pos > 0:                           # Enquanto a posição for superior a 0 o ciclo while é executado
            current = current.next                # Avança na pesquisa
            pos -= 1                              # A cada iteração a posição é reduzida em 1
        print("O elemento é", current.value)
        return current.value                      # Retorna o valor correspondente ao nó em questão

    def ver_min(self):                  # Método para consultar o menor elemento da lista
        return self.ver_p(0)            # Retorna o elemento na posição 0, já que a lista está ordenada

    def ver_max(self):                  # Método para consultar o maior elemento da lista
        return self.ver_p(self._size-1)   # Retorna o elemento na última posição, já que a lista está ordenada

    # Método auxiliar para ordenar de forma crescente a lista - não utilizado nos métodos de inserção e remoção
    def sort_list(self):
        current = self._head            # A variável current é atribuida ao primeiro nó (self._head)
        while current is not None:      # Enquanto existam elementos na lista o ciclo while é executado
            index = current.next        # A variável index é atribuida ao próximo nó
            while index is not None:    # Enquanto exista um próximo nó
                if current.value > index.value:     # Caso o valor atual seja superior ao do próximo nó
                    temp = current.value            # Os nós são trocados
                    current.value = index.value
                    index.value = temp
                index = index.next
            current = current.next       # Tanto o próximo nó como o nó atual avançam na pesquisa

    def ins(self, item):          # Método para inserir um dado item na lista, neste caso, já pode ser um item repetido
        current = self._head      # A variável current é atribuida ao primeiro nó da lista
        anterior = None           # A variável anterior é inicialmente atribuida a None
        stop = False              # A indicação de paragem começa a False
        self._size += 1    # Caso este elemento seja único, significa que vai ser inserido, incrementando o tamanho em 1
        while current is not None and not stop:  # Enquanto existam elementos na lista e ainda não for altura de parar
            if current.value > item:    # Caso o valor do nó em análise for superior ao item a colocar
                stop = True          # Significa que esta lista tinha apenas 1 elemento, portanto a paragem passa a True
            else:                    # Se o valor do nó em análise for inferior ao item a colocar
                anterior = current   # O anterior passa a ser o nó em análise naquele momento
                current = current.next  # E o current avança na navegação da lista
        new_node = Node(item)     # Quando se sai do ciclo, é então criado um nó com o item dado em input
        if anterior is None:    # Se o anterior for None
            new_node.next = self._head  # O nó a inserir passará a ser a cabeça da lista
            self._head = new_node
        else:                   # Se o anterior não for None
            new_node.next = current   # O apontador next do novo nó passará a apontar para o current
            anterior.next = new_node  # E, por fim, o apontador next do nó anterior passará a apontar para o novo nó

    # Método alternativo menos eficiente utilizando o método sort_list definido acima
    '''
    def ins(self, item):          # Método para inserir um dado item na lista, neste caso, já pode ser um item repetido
        tmp = Node(item)          # É criado um nó com o valor inserido
        tmp.next = self._head
        self._head = tmp          # Este nó é passado para a primeira posição, sendo agora o self._head
        self.sort_list()          # A lista é ordenada por ordem crescente
        self._size += 1           # O tamanho é incrementado em 1 posição
        print("Elemento inserido com sucesso.")    # Mensagem informativa
    '''

    def rem(self, item):       # Método para retirar um determinado item na sua totalidade, ou seja incluindo repetidos
        current = self._head           # A variável current é atribuida ao primeiro nó (self._head)
        ant = current.prev             # A variável ant é atribuida ao nó anterior
        encontrou = False              # A variável encontrou é iniciada a False
        while current is not None:          # Enquanto existam elementos
            if current.value == item:
                encontrou = True            # Se for encontrado, encontrou passa a True
                if ant is None:             # Se for encontrado, e o anterior for None é porque era o primeiro
                    self._head = current.next  # Então a cabeça passa a ser o próximo nó
                else:                       # Se o anterior não for None
                    ant.next = current.next  # O apontador do anterior passa a apontar para próximo nó
                self._size -= 1         # O tamanho da lista é reduzido em 1
                current = self._head    # Sempre que é encontrado um item é preciso reiniciar a variavel current e ant
                ant = current.prev
            else:
                ant = current               # Caso contrário, o nó anterior passa a ser o nó que foi analisado
                current = current.next      # E o novo nó é o próximo àquele que foi analisado
        if encontrou:
            print("Elemento retirado com sucesso.")  # Mensagem informativa
        else:
            print("A lista não contém o elemento que procura.")   # O utilizador é informado que o elemento não existe

    def rem_min(self):                  # Método para retirar o item com menor valor
        if self.vazia():                # Tal só é possível se a lista não estiver vazia
            print("A lista está vazia!")    # Caso esteja, mensagem informativa
        else:
            minimo = self.ver_min()
            self.rem(minimo)    # Caso contrário, o método rem é utilizado sobre o minimo elemento
            print("O menor elemento que era, ", minimo, " foi removido.")   # Mensagem informativa

    def rem_max(self):                  # Método para retirar o item com maior valor
        if self.vazia():                # Tal só é possível se a lista não estiver vazia
            print("A lista está vazia!")    # Caso esteja, mensagem informativa
        else:
            maximo = self.ver_max()
            self.rem(maximo)        # Caso contrário, o método rem é utilizado sobre o máximo elemento
            print("O maior elemento que era, ", maximo, " foi removido.")  # Mensagem informativa

    def abrir_menu(self):              # Método para abertura do menu de gestão da lista
        opcao = ""                     # A variável opção é iniciada a uma string vazia
        while opcao != "0":            # É disposto o seguinte menu de opções, sendo 0 a opção de saída do menu
            print("\n----- Bem-Vindo ao menu de gestão de lista -----\n")
            print("0. Sair do menu\n")
            print("1. Ver comprimento da lista (quantidade de itens)\n")
            print("2. Indicar se a lista está vazia\n")
            print("3. Esvaziar a lista\n")
            print("4. Mostrar o conteúdo da lista\n")
            print("5. Indicar se existe na lista um item com um dado valor\n")
            print("6. Consultar elemento numa dada posição\n")
            print("7. Consultar o menor elemento\n")
            print("8. Consultar o maior elemento\n")
            print("9. Inserir um dado item na lista\n")
            print("10. Retirar um dado item\n")
            print("11. Retirar o item com menor valor\n")
            print("12. Retirar o item com maior valor\n")
            opcao = input("Introduza a opção pretendida: \n")  # Após a disposição do menu é solicitada
            if opcao == "1":                                   # ao utilizador uma opção
                print(self.__len__())
            elif opcao == "2":
                if self.vazia():
                    print("Esta lista está vazia.")
                else:
                    print("Esta lista tem pelo menos um elemento.")
            elif opcao == "3":
                self.limpar()
            elif opcao == "4":
                print(self)
            elif opcao == "5":
                item_a_procurar = int(input("Indique o item a procurar: "))
                assert isinstance(item_a_procurar, int)     # Verifica que o item a procurar é um número inteiro
                if self.existe(item_a_procurar):
                    print("Este elemento está presente na lista")
                else:
                    print("Este elemento não existe na lista")
            elif opcao == "6":
                pos_a_procurar = int(input("Indique a posição a procurar: "))
                self.ver_p(pos_a_procurar)
            elif opcao == "7":
                self.ver_min()
            elif opcao == "8":
                self.ver_max()
            elif opcao == "9":
                item_a_inserir = int(input("Indique o item a inserir: "))
                if isinstance(item_a_inserir, int):  # Verifica que o item a inserir é um número inteiro
                    self.ins(item_a_inserir)
                    print("Elemento inserido com sucesso")
                else:
                    raise TypeError("Só podem ser inseridos números")
            elif opcao == "10":
                item_a_retirar = int(input("Indique o item a retirar: "))
                self.rem(item_a_retirar)
            elif opcao == "11":
                self.rem_min()
            elif opcao == "12":
                self.rem_max()
            elif opcao == "0":
                print("Obrigado")
            else:
                print("Opção inválida, tente de novo")

# -------------------------------------------------- fim de código -----------------------------------------------------
