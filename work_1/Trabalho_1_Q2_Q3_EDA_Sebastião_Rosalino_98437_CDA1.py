# ---------------------------------------------------Enquadramento------------------------------------------------------
# Trabalho 1 (questões 2 e 3)
# UC - Estruturas de Dados e Algoritmos da Licenciatura de Ciência de Dados
# Ano letivo 2020/2021- 2º Semestre
# Realizado por Sebastião Manuel Inácio Rosalino - n.º 98437 - Turma CDA1

# Objetivo:
# Q2) Elaborar uma hierarquia de classes, cuja raiz é a classe Forma, com atributo principal a cor da forma, e que
# tem como subclasses as formas Circulo, Retangulo e Triangulo, cada uma com métodos para, pelo menos, indicar a área e
# o perímetro de cada figura geométrica.
# Q3) Completar a hierarquia com mais um nível de especialização para sólidos geométricos, que disponibilize como métodos,
# pelo menos, o volume e a área de base de cada um.

# ------------------------------------------------------Código----------------------------------------------------------

import math
# biblioteca importada para utilização da constante PI


class Forma:
    def __init__(self, cor):
        self._cor = cor

    def __str__(self):
        return "{}".format(self._cor)


class Retangulo(Forma):                             # subclasse retangulo da classe Forma
    def __init__(self, comprimento, largura, cor):
        super().__init__(cor)
        self._comprimento = comprimento
        self._largura = largura

    def area1(self):
        return self._comprimento * self._largura

    def perimetro(self):
        return (self._comprimento * 2) + (self._largura * 2)

    def __str__(self):
        return "Retângulo ({}, {}), cor: {}".format(self._comprimento, self._largura, self._cor)


class Triangulo(Forma):                             # subclasse triangulo da classe Forma
    def __init__(self, l1, l2, l3, cor):            # Considerou-se para efeitos desta aplicação, triângulos do tipo Retângulo e do tipo Equilátero
        super().__init__(cor)
        assert l1 + l2 > l3                         # a soma dos dois lados mais pequenos (l1 e l2) deve ser maior que o maior dos lados (l3)
        self._l1 = l1
        self._l2 = l2
        self._l3 = l3

    # a área é calculada por tipo de triângulo, definidos nas subclasses seguintes

    def perimetro(self):
        return self._l1 + self._l2 + self._l3

    def __str__(self):
        return "Triângulo ({}, {}, {}), cor: {}".format(self._l1, self._l2, self._l3, self._cor)


class TrianguloRetangulo(Triangulo):                # subclasse "triangulo retangulo" da classe triangulo
    def area2(self):
        return (self._l1 * self._l2) / 2            # em triangulos retangulos a altura corresponde a um dos lados,
                                                    # que se considerou ser o lado 1 (l1)

    def perimetro(self):
        return super().perimetro()


class TrianguloEquilatero(Triangulo):                # subclasse "triangulo equilatero" da classe triangulo
    def area3(self):
        return self._l2 * (self._l1 * ((3) ** (1 / 2)) / 2) / 2     # em triangulos equilateros a altura é deduzida pelo
                                                                    # teorema de pitagoras e pela aplicação da formula da
                                                                    # area correspondente: (base (l2) * altura) / 2

    def perimetro(self):
        return super().perimetro()


class Circulo(Forma):                               # subclasse triangulo da classe Forma
    def __init__(self, diamentro, cor):
        super().__init__(cor)
        self._diamentro = diamentro
        self._raio = self._diamentro / 2            # o raio foi criado para dedução das medidas solicitadas

    def area4(self):
        return (math.pi * (self._raio)**2)

    def perimetro(self):
        return 2*(math.pi)*self._raio

    def __str__(self):
        return "Circulo de diamentro ({}), cor {}".format(self._diamentro, self._cor)


class Paralelipipedo(Retangulo):                # subclasse paralelipipedo que herda das classes retangulo e forma
    def __init__(self, comprimento, largura, altura, cor):
        super().__init__(comprimento, largura, cor)
        self._altura = altura

    def area5(self):                                    # area total
        return ((self._comprimento * self._largura) * 2) + ((self._comprimento * self._altura) * 2) + ((
                    self._largura * self._altura) * 2)

    def areabase(self):                                  # area da base
        return super().area1()

    def volume(self):
        return self._comprimento * self._largura * self._altura

    def __str__(self):
        return "Paralelipedo (Altura: {}, Comprimento: {}, Largura: {}), cor: {}".format(self._altura, self._comprimento, self._largura, self._cor)


class PiramideRetangular(Retangulo):                # subclasse "piramide retangular" que herda das classes retangulo e forma
    def __init__(self, comprimento, largura, altura, cor):
        super().__init__(comprimento, largura, cor)
        self._altura = altura

    def areabase(self):
        return super().area1()

    def volume(self):
        return (super().area1() * self._altura) / 3

    def __str__(self):
        return "Pirâmide Retangular (Base: {}, {}, Altura: {}), cor: {}".format(self._comprimento, self._largura, self._altura, self._cor)


class PiramideTriangular(TrianguloEquilatero):               # subclasse "piramide triangular" que herda das classes triangulo equilatero e forma
    def __init__(self, l1, l2, l3, altura, cor):
        super().__init__(l1, l2, l3, cor)
        self._altura = altura

    def area6(self):                                                # area total
        return super().area3() * 4

    def areabase(self):                                             # area base
        return super().area3()

    def volume(self):
        return (super().area3() * self._altura) / 3

    def __str__(self):
        return "Pirâmide Triângular (Base: {}, {}, {}, Altura: {}), cor: {}".format(self._l1, self._l2, self._l3, self._altura, self._cor)


class Esfera(Circulo):                                        # subclasse "Esfera" que herda das classes Circulo e forma
    def __init__(self, diametro, cor):
        super().__init__(diametro, cor)
        self._raio = diametro / 2

    def area_superficie_esferica(self):
        return 4 * math.pi * (self._raio) ** 2

    def volume(self):
        return (4/3 * math.pi * (self._raio)**3)

    def __str__(self):
        return "Esfera (Diamentro: {}), cor: {}".format(self._diamentro, self._cor)

# ---------------------------------------------------Fim de Código------------------------------------------------------

#   Criação de instâncias para fins de teste


a = Retangulo(1,2,"amarelo")
b = TrianguloRetangulo(3,3,4,"azul")
c = TrianguloEquilatero(4,4,4, "vermelho")
d = Circulo(5, "azul")
e = Paralelipipedo(4,3,2, "rosa")
f = PiramideRetangular(4,4,4,"preto")
g = PiramideTriangular(3,3,3,4, "verde")
h = Esfera(5, "rosa")









