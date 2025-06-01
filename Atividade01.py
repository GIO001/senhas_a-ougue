from collections import deque
from typing import Deque

class Pilha:
    def __init__(self):
        self.elementos = []

    def empilha(self, elemento):
        self.elementos.append(elemento)

    def desempilha(self):
        if self.vazio():
            raise IndexError("A pilha está vazia")
        return self.elementos.pop()

    def vazio(self):
        return len(self.elementos) == 0

    def __str__(self):
        retorno = "\nEstrutura Pilha (Topo para Base)\n"
        for indice, elemento in enumerate(reversed(self.elementos)):
            retorno += f"{len(self.elementos) - 1 - indice} - {elemento}\n"
        return retorno


class Fila:
    def __init__(self):
        self.fila_elementos: Deque[int] = deque()

    def incluir_na_fila(self, elemento):
        self.fila_elementos.append(elemento)

    def incluir_muitos_na_fila(self, varios_elementos: list[int]):
        for elemento in varios_elementos:
            self.fila_elementos.append(elemento)

    def retirar_da_fila(self):
        if not self.fila_elementos:
            raise IndexError("A fila está vazia")
        return self.fila_elementos.popleft()

    def __str__(self):
        retorno = "\nEstrutura Fila (Frente para Trás)\n"
        for indice, elemento in enumerate(self.fila_elementos):
            retorno += f"{indice} - {elemento}\n"
        return retorno



p = Pilha()
p.empilha(1)
p.empilha(2)
p.empilha(3)
print(p)

f = Fila()
f.incluir_na_fila(10)
f.incluir_muitos_na_fila([20, 30])
print(f)

print("Desempilhando:", p.desempilha())
print("Retirando da fila:", f.retirar_da_fila())
