# ---------------------------------------------------Enquadramento------------------------------------------------------
# Trabalho 3 (questões: 2 ; 3)
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
# Ano letivo 2020/2021- 2º Semestre
# Realizado por Sebastião Manuel Inácio Rosalino - n.º 98437 - Turma CDA1

# ---------------------------------------------------------------------------------------------------------------------

import random
import timeit
import matplotlib.pyplot as plt

# Questão 2
'''
Criar uma Classe Ordena de funções de ordenação de valores em sequências (lists) que implemente os seguintes algoritmos: 
Bubblesort; Selectionsort; Insertionsort; Mergesort; Quicksort; Shellsort e Python Sorted.
'''


class Ordena:

    @staticmethod
    def bubble_sort(seq):
        sorted = False
        contador = 0
        while not sorted:
            sorted = True
            for i in range(len(seq) - 1 - contador):
                if seq[i] > seq[i + 1]:
                    seq[i], seq[i + 1] = seq[i + 1], seq[i]
                    sorted = False
            contador += 1
        return seq

    @staticmethod
    def selection_sort(seq):
        for i in range(len(seq)):
            min_idx = i
            for j in range(i + 1, len(seq)):
                if seq[min_idx] > seq[j]:
                    min_idx = j
            seq[i], seq[min_idx] = seq[min_idx], seq[i]
        return seq

    @staticmethod
    def insertion_sort(seq):
        for i in range(1, len(seq)):
            j = i
            while j > 0 and seq[j] < seq[j - 1]:
                seq[j], seq[j - 1] = seq[j - 1], seq[j]
                j -= 1
        return seq

    @staticmethod
    def merge_sort(seq):
        if len(seq) < 2:
            return seq
        center = len(seq) // 2
        left = seq[:center]
        Ordena.merge_sort(left)
        right = seq[center:]
        Ordena.merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                seq[k] = left[i]
                i += 1
            else:
                seq[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            seq[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            seq[k] = right[j]
            j += 1
            k += 1
        return seq

    @staticmethod
    def quick_sort(seq, start=0, end=None):
        if end is None:
            end = len(seq) - 1
        if start < end:
            pivot_index = Ordena.quick_sort_partition(seq, start, end)
            Ordena.quick_sort(seq, start, pivot_index - 1)
            Ordena.quick_sort(seq, pivot_index + 1, end)
        return seq

    @staticmethod
    def quick_sort_partition(sequence, start, end):
        pivot_value = sequence[end]
        i = start - 1
        for j in range(start, end):
            if sequence[j] < pivot_value:
                i += 1
                sequence[i], sequence[j] = sequence[j], sequence[i]
        sequence[i + 1], sequence[end] = sequence[end], sequence[i + 1]
        return i + 1

# Implementação do algortimo ShellSort estudado na Questão 1.

    @staticmethod
    def shell_sort(seq):
        n = len(seq)
        esp = n // 2
        while esp > 0:
            for i in range(esp, n):
                temp = seq[i]
                j = i
                while j >= esp and seq[j - esp] > temp:
                    seq[j] = seq[j - esp]
                    j -= esp
                seq[j] = temp
            esp //= 2
        return seq

# Método criado para utilização do sort() pré-implementado do Python - para resposta à alinea a) da questão 3

    @staticmethod
    def sorted_python(seq):
        return sorted(seq)


# Criação de instâncias da Classe Ordena para fins de teste
'''
seq_1 = [1, 7, -87, 6, 50, -23]
print(Ordena.bubble_sort(seq_1))

seq_2 = [7, 8, 14, -9, 22, -2]
print(Ordena.selection_sort(seq_2))

seq_3 = [1, 898, -21, 56, 1, 0]
print(Ordena.insertion_sort(seq_3))

seq_4 = [1, 12, -12, 78, 1, 98]
print(Ordena.merge_sort(seq_4))

seq_5 = [1, 7, -123, 1, 0, 4]
print(Ordena.quick_sort(seq_5))

seq_6 = [12, 45, -12, 67, 1, -6767]
print(Ordena.shell_sort(seq_6))

seq_7 = [11, 22, -33, 99, 456, -10]
print(Ordena.sorted_python(seq_7))
'''

# -------------------------------------------------------------------------------------------------------------------
# Questão 3

'''
Criar uma função para devolver uma list com valores inteiros gerados aleatoriamente e a variar no conjunto 
{1, 2, ..., 10000}
'''


def geradora_listas(number, max_value):
    res = random.sample(range(1, max_value + 1), number)
    return res


# alínea a)
'''
Testar os algoritmos em lists com n, número de elementos, a variar em {50, 100, . . . , 500}(passo 50), cronometrando 
e guardando os tempos médios (gastos apenas na ordenação) de 30 execuções para cada um dos algoritmos da classe Ordena.
'''

Dominio = [x for x in range(50, 501, 50)]


def cronometrar_bubble_sort():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.bubble_sort(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios


def cronometrar_selection_sort():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.selection_sort(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios


def cronometrar_insertion_sort():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.insertion_sort(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios


def cronometrar_merge_sort():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.merge_sort(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios


def cronometrar_quick_sort():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.quick_sort(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios


def cronometrar_shell_sort():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.shell_sort(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios


def cronometrar_sorted_python():
    lista_tempos_medios = []
    for i in Dominio:
        total_time = 0
        time_start = timeit.default_timer()
        for j in range(30):
            l = geradora_listas(i, 10000)
            Ordena.sorted_python(l)
        total_time += timeit.default_timer() - time_start
        tempo_relevante = total_time / 30
        lista_tempos_medios.append(tempo_relevante)
    return lista_tempos_medios

# No ficheiro pdf enviado juntamente com o código foi criada uma tabela com os tempos médios de 30 execuções para cada
# um dos algoritmos da classe Ordena, incluindo o algoritmo nativo do Python (Python Sorted).


# alínea b)
'''
Utilizando o módulo para criar um gráfico de visualização, elaborar um gráfico de linhas de modo a comparar os diversos 
tempos de execução de todos os algoritmos de ordenação.
'''

plt.plot(range(50, 501, 50), cronometrar_bubble_sort(), label="Bubble Sort")
plt.plot(range(50, 501, 50), cronometrar_selection_sort(), label="Selection Sort")
plt.plot(range(50, 501, 50), cronometrar_insertion_sort(), label="Insertion Sort")
plt.plot(range(50, 501, 50), cronometrar_merge_sort(), label="Merge Sort")
plt.plot(range(50, 501, 50), cronometrar_quick_sort(), label="Quick Sort")
plt.plot(range(50, 501, 50), cronometrar_shell_sort(), label="Shell Sort")
plt.plot(range(50, 501, 50), cronometrar_sorted_python(), label="Sorted Python")
plt.title("EDA - Trabalho 3 - Sebastião Rosalino")
plt.xlabel("Níveis de Listas")
plt.xticks(range(50, 501, 50))
plt.ylabel("Tempo médio de execução")
plt.legend()
plt.show()

# alínea c)
'''
Estudo da função de ordenação sort pré-implementada do Python
Resposta remetida no ficheiro pdf.
'''

# alínea d)
'''
Utilizando o módulo para criar um gráfico de visualização, criar um gráfico de linhas de modo a comparar os diversos 
tempos de execução de todos os algoritmos de ordenação - utilizando uma escala logarítmica
'''

plt.figure()
plt.plot(range(50, 501, 50), cronometrar_bubble_sort(), label="Bubble Sort")
plt.plot(range(50, 501, 50), cronometrar_selection_sort(), label="Selection Sort")
plt.plot(range(50, 501, 50), cronometrar_insertion_sort(), label="Insertion Sort")
plt.plot(range(50, 501, 50), cronometrar_merge_sort(), label="Merge Sort")
plt.plot(range(50, 501, 50), cronometrar_quick_sort(), label="Quick Sort")
plt.plot(range(50, 501, 50), cronometrar_shell_sort(), label="Shell Sort")
plt.plot(range(50, 501, 50), cronometrar_sorted_python(), label="Sorted Python")
plt.title("EDA - Trabalho 3 - Sebastião Rosalino")
plt.xlabel("Níveis de Listas")
plt.xticks(range(50, 501, 50))
plt.ylabel("Tempo médio de execução")
plt.yscale('log')
plt.legend()
plt.show()

# alínea e)
'''
Resposta remetida no ficheiro pdf.
'''

# ---------------------------------------------------Fim de Código------------------------------------------------------


