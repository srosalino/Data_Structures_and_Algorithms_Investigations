# ---------------------------------------------------Enquadramento------------------------------------------------------
# Trabalho 6
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
# Ano letivo 2020/2021- 2º Semestre
# Realizado por Sebastião Manuel Inácio Rosalino - n.º 98437 - Turma CDA1

# ---------------------------------------------------------------------------------------------------------------------

# Questão 2 - Criação de uma representação gráfica do Metro de Lisboa

"""O programa pode ser executado através de um menu com as seguintes opções:
----- Bem-Vindo ao menu do metro de Lisboa -----
0. Sair do menu
1. Consultar todas estações
2. Consultar todas as linhas
3. Consultar as ligações entre estações
4. Ver mapa do Metro de Lisboa
"""

# Importação das bibliotecas necessárias
import re
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# a) Em Vertex, crie uma subclasse Station, para conter o id da estação e a posição, em graus decimais, da localização
# do objeto à superfície da terra.


class Vertex:               # Criação da classe Vertex
    __slots__ = "_iden"     # Reserva do único atributo da classe

    def __init__(self, iden):   # Construtor da classe que recebe como input para criação de objetos uma identificação
        self._iden = iden

    def iden(self):             # Propriedade iden da classe Vertex
        return self._iden

    def __str__(self):          # Método para utilização do comando print sobre os objetos da classe
        return "Vertex: {}".format(self._iden)

    def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
        if isinstance(other, Vertex):
            return self._iden == other._iden()
        return False

    def __hash__(self):         # Método para garantir a unicidade dos objetos
        return hash(id(self))

    class Station:             # Criação da subclasse Station e reserva dos atributos da classe
        __slots__ = "_iden", "_latitude", "_longitude", "_name", "_list_stations", "_ids", "_coordinates", "_labels"

        def __init__(self):    # Construtor da subclasse Station
            self._iden = None
            self._latitude = None
            self._longitude = None
            self._name = None
            self._list_stations = []
            self._ids = []
            self._coordinates = []
            self._labels = []

        @property             # Propriedade iden dos objetos
        def iden(self):
            return self._iden

        @property            # Propriedade latitude dos objetos
        def latitude(self):
            return self._latitude

        @property           # Propriedade longitude dos objetos
        def longitude(self):
            return self._longitude

        @property           # Propriedade name dos objetos
        def name(self):
            return self._name

        def __str__(self):  # Método para utilização do comando print sobre os objetos da classe
            return "Estação: Id: {}, Latitude: {}, Longitude: {}, Nome: {}".format(self._iden, self._latitude,
                                                                                   self.longitude(), self._name)

        def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
            if isinstance(other, Vertex.Station):
                return self.iden == other.iden and self.latitude == other.latitude and self.longitude == other.longitude and self.name == other.name
            else:
                return False

        def __hash__(self):         # Método para garantir a unicidade dos objetos
            return hash(id(self))

        def show_list(self):        # Método para retornar a lista com todos os objetos da classe Station
            return self._list_stations

        def get_coordinates(self):  # Método para retornar as coordenadas das estações
            return self._coordinates

        def get_id(self):           # Método para retornar as identificações das estações
            return self._ids

        def get_labels(self):       # Método para retornar os nomes das estações
            return self._labels

        def insert_stations(self, new_id, new_latitude, new_longitude, new_name):   # Método para inserir estações
            self._list_stations.append([new_id - 1, new_latitude, new_longitude, new_name])
            self._coordinates.append([new_longitude, new_latitude])
            self._ids.append(new_id - 1)
            self._labels.append(new_name)

# b) Criação da uma lista de objetos Station a partir do conjunto de dados lisbon.station.csv

        def obj_stations(self):
            f = open('lisbon.stations.csv', 'r')    # Leitura do ficheiro csv
            linhas = f.readlines()
            stations = []
            for linha in linhas:
                stripped_line = linha.strip()
                splitted_line = stripped_line.split(",")    # Limpeza das linhas do ficheiro csv
                stations.append(splitted_line)
            clean_stations = stations[1:]   # Apenas interessam os dados da linha 2 até ao final
            for e in clean_stations:
                new_id = int(e[0])           # Criação de um novo id a colocar na lista de estações
                new_latitude = float(e[1]) * 1.26   # Criação de uma nova latitude a colocar na lista de estações
                new_longitude = float(e[2])         # Criação de uma nova longitude a colocar na lista de estações
                new_name = str(e[3])                # Criação de um novo nome a colocar na lista de estações
                new_name_clean = re.sub('"', '', new_name)  # Remoção de aspas indevidamente presentes
                self.insert_stations(new_id, new_latitude, new_longitude, new_name_clean)   # Inserção da nova estação


# c) Em Edge, crie uma subclasse Edge_line, para conter a linha de que a conexão faz parte

class Edge:
    __slots__ = "_origem", "_destino", "_peso"          # Reserva dos únicos atributos da classe

    def __init__(self, origem, destino, peso=None):     # Inicialização do construtor da classe
        self._origem = origem
        self._destino = destino
        self._peso = peso

    @property       # Propriedade origem dos objetos
    def origem(self):
        return self._origem

    @property        # Propriedade destino dos objetos
    def destino(self):
        return self._destino

    @property       # Propriedade peso dos objetos
    def peso(self):
        return self._peso

    def endpoints(self):    # Método para retornar em forma de tuplo a origem e o destino de um objeto
        return self._origem, self._destino

    def opposite(self, v):  # Método para retornar a localização oposta de um objeto
        return self._destino if v is self._origem else self._origem

    def __str__(self):      # Método para utilização do comando print sobre os objetos da classe
        return f"Edge:({self._origem}, {self._destino})"

    def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
        if isinstance(other, Edge):
            return self._origem == other._origem and self._destino == other._destino and self._peso == other._peso
        return False

    def __hash__(self):         # Método para garantir a unicidade dos objetos
        return hash((id(self._origem), id(self._destino)))

    class Edge_line:            # Criação da subclasse Edge_line
        __slots__ = "_line", "_name", "_colour", "_list_edges"      # Reserva dos atributos da classe

        def __init__(self):     # Construtor da subclasse
            self._line = None
            self._name = None
            self._colour = None
            self._list_edges = []

        @property               # Propriedade line dos objetos
        def line(self):
            return self._line

        @property               # Propriedade name dos objetos
        def name(self):
            return self._name

        @property               # Propriedade colour dos objetos
        def colour(self):
            return self._colour

        def show_list(self):    # Método para retornar a lista edges
            return self._list_edges

        def insert_edges(self, new_line, new_name, new_colour):     # Método para inserir edges
            self._list_edges.append([new_line, new_name, new_colour])

# d) Criação da uma lista de objetos Edge a partir do conjunto de dados lisbon.lines.csv

        def obj_edge(self):
            f = open('lisbon.lines.csv', 'r')       # Leitura do ficheiro csv
            linhas = f.readlines()
            edges = []
            for linha in linhas:
                stripped_line = linha.strip()
                splitted_line = stripped_line.split(",")    # Limpeza das linhas do ficheiro csv
                edges.append(splitted_line)
            clean_edges = edges[1:-1]       # Foi necessário adaptar este comando pois apenas interessam os dados
            for e in clean_edges:           # referentes às linhas de ligação de estações
                new_line = int(e[0])        # Criação de uma nova linha a colocar na lista de edges
                new_name = str(e[1])        # Criação de um novo nome a colocar na lista de edges
                new_colour = str(e[2])      # Criação de uma nova cor a colocar na lista de edges
                new_colour_clean = re.sub('"', '', new_colour)  # Remoção de aspas indevidamente presentes
                self.insert_edges(new_line, new_name, new_colour_clean)    # Inserção da nova edge

        def get_colour(self, line):    # Método para retornar a cor dada a indentificação de uma edge como input
            found = False
            for edge in self.show_list():
                if edge[0] == line:
                    found = True
                    return edge[2]
            if found:
                pass
            else:
                print("Esta linha não existe.")

        def __str__(self):          # Método para utilização do comando print sobre objetos da classe
            return "Nº de linha: {}, Nome: {}, Cor: {}".format(self._line, self._name, self._colour)

        def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
            if isinstance(other, Edge.Edge_line):
                return self._line == other._line and self._name == other._name and self._colour == other._colour
            else:
                return False

        def __hash__(self):         # Método para garantir a unicidade dos objetos
            return hash(id(self))


# Criação da classe Connection necessária para assegurar as ligações entre estações

class Connection:
    __slots__ = "_station1", "_station2", "_line", "_list_connections"  # Reserva dos atributos da classe

    def __init__(self):     # Construtor da classe
        self._station1 = None
        self._station2 = None
        self._line = None
        self._list_connections = []

    @property               # Propriedade station1 do objeto
    def station1(self):
        return self._station1

    @property               # Propriedade station2 do objeto
    def station2(self):
        return self._station2

    @property               # Propriedade line do objeto
    def line(self):
        return self._line

    def __str__(self):      # Método para utilização do comando print sobre os objetos da classe
        return "Conecção entre estações: {}, {}, usando a linha: {}".format(self._station1, self._station2, self._line)

    def __eq__(self, other):    # Método para avaliar a igualdade entre dois objetos
        if isinstance(other, Connection):
            return self._station1 == other._station1 and self._station2 == other._station2 and self._line == other._line
        else:
            return False

    def insert_connection(self, new_station1, new_station2, new_line):   # Método para criar conecções entre estações
        self._list_connections.append([new_station1 - 1, new_station2 - 1, new_line])   # usando uma determinada linha

    def show_list(self):    # Método de conversão da lista de conecções num array e retorno do mesmo
        return np.array(self._list_connections)

    def obj_connection(self):   # Método para criar todas as conecções presentes no ficheiro lisbon.connections.csv
        f = open('lisbon.connections.csv', 'r')      # Leitura do ficheiro csv
        linhas = f.readlines()
        connections = []
        for linha in linhas:
            stripped_line = linha.strip()
            splitted_line = stripped_line.split(",")    # Limpeza das linhas do ficheiro csv
            connections.append(splitted_line)
        clean_connections = connections[1:]     # Apenas interessam os dados da linha 2 até ao final
        for e in clean_connections:
            new_station1 = int(e[0])            # Criação de uma nova estação 1
            new_station2 = int(e[1])            # Criação de uma nova estação 2
            new_line = int(e[2])                # Criação de uma linha de ligação
            self.insert_connection(new_station1, new_station2, new_line)    # Inserção da nova conecção


# e) Crie uma estrutura de Grafo, i.e., utilize uma das classes do exercício 3) do Módulo 7

class Grafo:                                # Baseado em representação de um mapa de adjacência
    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())
        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v)

    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, x=None):
        e = Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_vertex(self, v):
        for i in self.incident_edges(v):
            self.remove_edge(v, i)
        del self._outgoing[v]
        if self.is_directed():
            for i in self.incident_edges(v, False):
                self.remove_edge(i, v)
            del self._incoming[v]
        return v

    def remove_edge(self, u, v):
        for e in self._outgoing[u]:
            x, y = e.endpoints()
            if u == x and v == y:
                self._outgoing[u].remove(e)
                self._incoming[v].remove(e)


# f) Crie um procedimento/método para poder visualizar a rede


class Visualizar:           # Criação da classe Visualizar para construção da rede com recurso à biblioteca networkx
    def __init__(self):     # Construtor da classe
        self.visual = []
        self._connection = None
        self.g = nx.Graph()
        self.colors = []

    def add_connection(self, connection):  # Método que recebe com input uma conecção e a atribui ao atributo connection
        self._connection = connection

    def add_edges(self):       # Método para adicionar edges
        e = Edge.Edge_line()   # Invocação da classe Edge_line
        e.obj_edge()           # Todas as edges do ficheiro csv são geradas
        # A cor a colocar no grafo é dada pelo resultado do método get_colour definido na classe Edge_line
        color_map = e.get_colour((int(self._connection[2])))
        self.g.add_edge(self._connection[0], self._connection[1], color=color_map)    # Adição da edge
        return self.g

    def draw_network(self, graph, stations, edges, color):      # Método para apresentação do grafo
        locations = {}              # A variável locations é iniciada a um dicionário vazio
        ids = stations.get_id()     # A variável ids é atribuida às identificações das estações
        coordinates = stations.get_coordinates()     # A variável coordinates é atribuida às coordenadas das estações
        label = stations.get_labels()   # A variável label é atribuida aos nomes das estações
        labels = {}                     # A variáveç labels é iniciada a um dicionário vazio
        for i in range(0, len(coordinates)):   # Adição das informações relevantes de nome e coordenadas aos dicionários
            labels[ids[i]] = label[i]          # locations e labels
        for i in range(0, len(coordinates)):
            locations[ids[i]] = coordinates[i]
        plt.figure(figsize=(150, 150))         # Definições de tamanho da imagem
        plt.title("Mapa do metro de Lisboa")   # Título da imagem
        nx.draw_networkx(graph, pos=locations, labels=labels,  edge_color=color, edgelist=edges)


def show_graph():
    stations = Vertex.Station()     # Invocação da classe Station na variável stations
    stations.obj_stations()         # Criação de todas as estações presentes no ficheiro csv
    v = Visualizar()                # Invocação da classe Visualizar na variável V
    c = Connection()                # Invocação da classe Connection na variável c
    c.obj_connection()              # Criação de todas as conecções presentes no ficheiro csv
    connection_final_list = c.show_list()       # A variável connection_final_list é atribuida à matriz de conecções
    for i in range(0, len(c.show_list()) - 1):  # Adição das conecções ao grafo
        v.add_connection(connection_final_list[i])
        graph = v.add_edges()
    # Criação final do grafo
    edges_map, colors = zip(*nx.get_edge_attributes(graph, 'color').items())
    v.draw_network(graph, stations, edges_map, color=colors)


def abrir_menu():   # Função para apresentação do menu
    opcao = ""      # A variável opção é iniciada a uma string vazia
    while opcao != "0":     # É apresentado o seguinte menu de opções, sendo 0 a opção de saída do menu
        print("\n----- Bem-Vindo ao menu do metro de Lisboa -----\n")
        print("0. Sair do menu\n")
        print("1. Consultar todas estações\n")
        print("2. Consultar todas as linhas\n")
        print("3. Consultar as ligações entre estações\n")
        print("4. Ver mapa do Metro de Lisboa\n")
        opcao = input("Introduza a opção pretendida: \n")
        if opcao == "1":
            s = Vertex.Station()
            s.obj_stations()
            for station in s.show_list():
                print(station)
        elif opcao == "2":
            e = Edge.Edge_line()
            e.obj_edge()
            for edge in e.show_list():
                print(edge)
        elif opcao == "3":
            c = Connection()
            c.obj_connection()
            for connection in c.show_list():
                print(connection)
        elif opcao == "4":
            return show_graph()
        elif opcao == "0":
            print("Obrigado")
        else:
            print("Opção inválida, tente de novo")


if __name__ == '__main__':      # Comando para apresentar a disposição do menu
    abrir_menu()

# -------------------------------------------------- fim de código -----------------------------------------------------
