# ---------------------------------------------------Enquadramento------------------------------------------------------
# Trabalho 4
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
# Ano letivo 2020/2021- 2º Semestre
# Realizado por Sebastião Manuel Inácio Rosalino - n.º 98437 - Turma CDA1

# ---------------------------------------------------------------------------------------------------------------------
# Questão 2

import numpy as np    # Importação da biblioteca numpy


# Criação da classe funcionário
class Funcionario:
    def __init__(self, nome):
        self._nome = nome

    def __str__(self):
        return "Funcionário: {}".format(self._nome)


f1 = Funcionario("Sebastião")   # Criação de uma instância da classe Funcionário


class Call:                   # Criação da class Call para manuseamento das operações requeridas
    def __init__(self):
        self._tele_num = []     # Lista para armazenar o número de telefone do cliente
        self._num_chegada = 0   # Comando para inicializar o numero de chegada dos clientes, começando em 0
        self._fila_espera = []  # Fila de espera

    def is_empty(self):         # Método auxiliar para verificação da existência de clientes em fila de espera
        return len(self._fila_espera) == 0

    # Método para gerir chamadas que entram no call center, atribuíndo um número de chegada (relativo à quantidade de
    # chamadas em espera na fila), associando o número de telefone e inserido essa chamada na fila de espera.
    def opcao_i(self, tele_num):
        self._num_chegada += 1                          # O numero de chegada, que começou em 0, é incrementado 1 posição
        self._fila_espera.append(self._num_chegada)     # Adição à fila de espera do numero de chegada
        self._tele_num.append(tele_num)                 # Adição à lista de números de telefone do número do utente em espera

    # Método para o funcionário atender o próximo cliente em espera, diminuindo automaticamente a quantidade de chamadas
    # em espera na fila.
    def opcao_a(self):
        if self.is_empty():         # Verificação se a fila de espera está vazia
            raise ValueError("A lista de espera está vazia!")   # Caso isto se verifique, lança-se um erro
        self._fila_espera.pop(0)    # Caso contrário, remoção do primeiro utente da fila de espera

        '''Método alternativo para atualização do número de chegada em função dos atendimentos que estão a ocorrer,
        reduzindo os indíces em uma unidade
        self._fila_espera = np.array(self._fila_espera) - 1  - Conversão da lista num array para redução dos indíces em 1 posição
        self._fila_espera = list(self._fila_espera)          - Reconversão do array numa lista
        '''
        print("O número que está prestes a atender é o seguinte: ", self._tele_num.pop(0))   # Mensagem informativa

    # Método para ver qual o próximo número de telefone a ser atendido.
    def opcao_p(self):
        if self.is_empty():         # Verificação se a fila de espera está vazia
            raise ValueError("A lista de espera está vazia!")   # Caso isto se verifique, lança-se um erro
        print("O próximo cliente a ser atendido tem o seguinte número: ", self._tele_num[0])    # Caso contrário, mensagem informativa sobre o próximo utente a ser atendido

    # Método para verificar qual a quantidade de chamadas em espera na fila.
    def opcao_n(self):
        print("Existem ", len(self._fila_espera), " chamadas em fila de espera.")      # Mensagem informativa

    # Método para estimar o tempo médio expectável que demorará até atender a última chamada em espera na fila.
    # É usada a premissa de que o tempo mínimo de espera para uma chamada, a partir do momento em que chega à fila, é de 2 minutos.
    def opcao_t(self):
        if self.is_empty():     # Verificação se a fila de espera está vazia
            print("O tempo expectável até o atendimento de todas as chamadas é: ", 0, "minutos")   # Caso isto se verifique, mensagem informativa
        else:
            print("O tempo expectável até o atendimento de todas as chamadas é: ", len(self._fila_espera) * 2 - 2, "minutos")  # Mensagem informativa

    # Método para ver lista de espera a partir do menu.
    def ver_lista(self):
        if self.is_empty():         # Verificação se a fila de espera está vazia
            print("Não existem chamadas por atender.")   # Caso isto se verifique, mensagem informativa
        for i in range(len(self._fila_espera)):    # Caso contrário, percorrer a lista e mostrar no ecrã a informação dos clientes em fila de espera
            print("Número de chegada: ", self._fila_espera[i], "Número de telefone: ", self._tele_num[i])

    # Método para esvaziar toda a lista de espera.
    def esvaziar_lista(self):
        self._fila_espera.clear()       # Instrução de limpeza da lista
        print("A lista de espera está agora vazia.")    # Mensagem informativa

    # Menu para selecionar as opções pedidas no programa.
    def abrir_menu(self):
        op = ""
        print("\n----- Bem-Vindo ao menu de atendimento -----\n-----", f1, "-----")
        print("\nSelecione a sua opção\n")
        print("A - Atender próximo cliente\n")
        print("P - Mostrar próximo cliente\n")
        print("N - Mostrar o número de clientes em lista de espera\n")
        print("T - Tempo médio de atendimento\n")
        print("V - Ver lista de espera\n")
        print("C - Esvaziar a lista de espera\n")
        print("Z - Sair do menu\n")
        while op != "Z":
            op = str(input("\nInsira a sua opção\n"))
            if op == "A":
                self.opcao_a()
            elif op == "P":
                self.opcao_p()
            elif op == "N":
                self.opcao_n()
            elif op == "T":
                self.opcao_t()
            elif op == "V":
                self.ver_lista()
            elif op == "C":
                self.esvaziar_lista()
            else:
                print("Opcão inválida, tente de novo.")


c = Call()      # Invocação da classe Call na variável "c"

# - Criação de chamadas a entrar no callcenter para teste da aplicação -------------------------------------------------
# - Operador automático para inserir chamadas no sistema quando chegam ao callcenter.

c.opcao_i("966973167")
c.opcao_i("975129491")
c.opcao_i("923456672")
c.opcao_i("913456673")
c.opcao_i("933456674")
c.opcao_i("980254294")
c.opcao_i("967851282")
c.opcao_i("985471682")
c.opcao_i("954646528")
c.opcao_i("975412582")
c.opcao_i("985471215")
c.opcao_i("989012831")
c.opcao_i("945852157")
c.opcao_i("941745225")
c.opcao_i("974512285")
c.opcao_i("974585221")
c.opcao_i("945252528")
c.opcao_i("988545225")
c.abrir_menu()      # Ordem para abertura do menu de atendimento

# -----------------------------------------------------fim de código----------------------------------------------------
