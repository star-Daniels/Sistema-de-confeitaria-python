class Pilha:
    def __init__(self):
        self.itens = []

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.itens:
            return None

        return self.itens.pop()

    def topo(self):
        if not self.itens:
            return None

        return self.itens[-1]

    def vazia(self):
        return len(self.itens) == 0