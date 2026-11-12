
class TabelaHash:

    def __init__(self):
        self.tabela = [[] for _ in range(10)]

    def funcao_hash(self, nome):
        return sum(ord(letra) for letra in nome.lower()) % 10

    def inserir(self, item):
        posicao = self.funcao_hash(item.nome)

        for atual in self.tabela[posicao]:
            if atual.nome.lower() == item.nome.lower():
                return False

        self.tabela[posicao].append(item)
        return True

    def buscar(self, nome):
        posicao = self.funcao_hash(nome)

        for item in self.tabela[posicao]:
            if item.nome.lower() == nome.lower():
                return item

        return None

    def remover(self, nome):
        posicao = self.funcao_hash(nome)

        for item in self.tabela[posicao]:
            if item.nome.lower() == nome.lower():
                self.tabela[posicao].remove(item)
                return True

        return False

    def listar(self):
        itens = []

        for lista in self.tabela:
            itens.extend(lista)

        return itens
