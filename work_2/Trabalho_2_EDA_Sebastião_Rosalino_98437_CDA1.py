# ---------------------------------------------------Enquadramento------------------------------------------------------
# Trabalho 2 (questões: 1 ; 2a) ; 2b) e 2c))
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
# Ano letivo 2020/2021- 2º Semestre
# Realizado por Sebastião Manuel Inácio Rosalino - n.º 98437 - Turma CDA1

# ---------------------------------------------------------------------------------------------------------------------

# Questões:
#
#    1. Usando o Numpy, criar uma classe de Matrizes (Matrix), que deve:
#    --» receber o n.º de linhas, número de colunas e uma lista (list) de números ou um código < z =matriz de zeros (0);
#        u = matriz de uns (1); i = matriz identidade)
#    --» validar o input (por exemplo, se receber um código deve verificar que, no mínimo, recebeu umn.º ou de linhas,
#        ou de colunas)
#    --» ter métodos para, pelo menos: somar matrizes - sumM ; multiplicar matrizes - mulM ; transpor matrizes - trM ;
#        criar a matriz de valores simétricos - simM e inverter matrizes (se forem invertíveis) – invM.
#
#    2. Usando a classe Matrix, o módulo random o método matmul do Numpy:
#    a) Criar código para produzir matrizes quadradas (com os mesmos valores aleatórios) usando o método array do
#       numpy e usando a classe Matrix;
#    b) Para cada par de matrizes criadas com dimensões nxn, com n ∈ {100, 300, 500, 800, 1100, 1400, 1700, 2000},
#       executar e cronometrar os tempos médios de 500 execuções de: multiplicações mulM em Matrix e matmul em numpy;
#    c) Utilizando o módulo do Matplotlib para criar gráficos de visualização de linhas indicado na folha do módulo 3,
#       criar gráfico (de pontos ou de linhas) de modo a comparar os diversos tempos de execução entre as duas
#       possibilidades de multiplicação.

# ------------------------------------------------------Código----------------------------------------------------------

import numpy as np
import timeit
import random
import matplotlib.pyplot as plt

# Questão 1


class Matrix:
    def __init__(self, linhas, colunas, lista, code=None):
        self._linhas = linhas
        self._colunas = colunas
        self._lista = lista
        self._code = code
        assert self._linhas > 0 and self._colunas > 0         # validação do input introduzido, garantindo a introdução de linhas e colunas
        if lista is not None:
            self._matrix = np.array(lista).reshape(linhas, colunas)
        if code == "z":
            self._matrix = np.zeros([linhas, colunas])
        elif code == "u":
            self._matrix = np.ones([linhas, colunas])
        elif code == "i":
            self._matrix = np.identity(linhas)

    def __str__(self):
        return "Matriz {} por {} de elementos {}".format(self._linhas, self._colunas, self._lista)

    def sumM(self, other):
        a = self._matrix
        b = other._matrix
        add = np.add(a, b)
        return add

    def mulM(self, other):
        a = self._matrix
        b = other._matrix
        mul = a.dot(b)
        return mul

    def matmul(self, other):
        a = self._matrix
        b = other._matrix
        mat = np.matmul(a, b)
        return mat

    def trM(self):
        trans = np.transpose(self._matrix)
        return trans

    def simM(self):
        sym = self._matrix * (-1)
        return sym

    def invM(self):
        if np.linalg.det(self._matrix) == 0:
            raise Exception('Determinante igual a 0 - matriz nao invertivel')
        inverter = np.linalg.inv(self._matrix)
        return inverter

    def somaDosValoresDaMatriz(self):
        soma = np.sum(self._matrix)
        return soma


# Questão 2

# alinea a)

def rand_sq_matrix_for_visualization(n):
    lista_elementos = []
    for i in range((n*n)):
        b = random.randint(1, 30)
        lista_elementos.append(b)
    new_matrix = Matrix(n, n, lista_elementos)
    print(new_matrix)


def rand_sq_matrix_use(n):
    lista_elementos = []
    for i in range((n*n)):
        b = random.randint(1, 30)
        lista_elementos.append(b)
    new_matrix = Matrix(n, n, lista_elementos)
    return new_matrix


# alinea b)


def average_em_matrix(repeat=500):
    dominio = [100, 300, 500, 800, 1100, 1400, 1700, 2000]
    lista_de_tempos = []
    for i in dominio:
        total_time = 0
        m1 = rand_sq_matrix_use(i)
        m2 = rand_sq_matrix_use(i)
        for n in range(0, repeat):
            time_start = timeit.default_timer()
            m1.mulM(m2)
            total_time += timeit.default_timer() - time_start
            a = total_time / 500
            lista_de_tempos.append(a)
        return lista_de_tempos


def average_em_matmul(repeat=500):
    dominio = [100, 300, 500, 800, 1100, 1400, 1700, 2000]
    lista_de_tempos = []
    for i in dominio:
        total_time = 0
        m1 = rand_sq_matrix_use(i)
        m2 = rand_sq_matrix_use(i)
        for n in range(0, repeat):
            time_start = timeit.default_timer()
            m1.matmul(m2)
            total_time += timeit.default_timer() - time_start
            a = total_time / 500
            lista_de_tempos.append(a)
        return lista_de_tempos


# Alinea c)

lista_mulM = average_em_matrix()
lista_matmul = average_em_matmul()
dominio = [100, 300, 500, 800, 1100, 1400, 1700, 2000]

plt.plot(range(500), [x for x in lista_mulM], label="Processamento mulM")
plt.plot(range(500), [x for x in lista_matmul], label="Processamento matmul")
plt.legend()
plt.show()

# ---------------------------------------------------Fim de Código------------------------------------------------------

# Criação de instâncias da classe Matrix para fins de teste

a = Matrix(2,2,[5,6,7,8])
b = Matrix(2,2,[1,2,3,4])
c = Matrix(2,2,None,"z")
d = Matrix(2,2,None, "i")
e = Matrix(2,2,None,"u")
f = Matrix(3,3,[1,2,3,4,5,6,7,8,9])
# g = Matrix(-1,0,[1212]) instância para verificação de inputs introduzidos incorretamente


