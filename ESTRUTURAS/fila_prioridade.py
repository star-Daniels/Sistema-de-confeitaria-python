class FilaPrioridade:

    def __init__(self):
        self.itens = []

    def adicionar(self, item, prioridade):
        self.itens.append((prioridade, item))

    def remover(self):
        if len(self.itens) == 0:
            return None

        menor = 0

        for i in range(1, len(self.itens)):
            if self.itens[i][0] < self.itens[menor][0]:
                menor = i

        return self.itens.pop(menor)

    def vazia(self):
        return len(self.itens) == 0