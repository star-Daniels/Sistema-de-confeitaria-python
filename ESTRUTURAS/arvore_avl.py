
class No:
    def __init__(self, bolo):
        self.bolo = bolo
        self.esquerda = None
        self.direita = None
        self.altura = 1


class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        return no.altura if no else 0

    def balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita) if no else 0

    def rotacao_direita(self, y):
        x = y.esquerda
        y.esquerda = x.direita
        x.direita = y
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        x.direita = y.esquerda
        y.esquerda = x
        x.altura = 1 + max(self.altura(x.esquerda), self.altura(x.direita))
        y.altura = 1 + max(self.altura(y.esquerda), self.altura(y.direita))
        return y

    def balancear(self, no):
        no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))
        fator = self.balanceamento(no)

        if fator > 1:
            if self.balanceamento(no.esquerda) < 0:
                no.esquerda = self.rotacao_esquerda(no.esquerda)
            return self.rotacao_direita(no)

        if fator < -1:
            if self.balanceamento(no.direita) > 0:
                no.direita = self.rotacao_direita(no.direita)
            return self.rotacao_esquerda(no)

        return no

    def inserir(self, bolo):
        self.raiz = self._inserir(self.raiz, bolo)

    def _inserir(self, no, bolo):
        if no is None:
            return No(bolo)

        nome = bolo.nome.lower()
        atual = no.bolo.nome.lower()

        if nome < atual:
            no.esquerda = self._inserir(no.esquerda, bolo)
        elif nome > atual:
            no.direita = self._inserir(no.direita, bolo)
        else:
            return no

        return self.balancear(no)

    def buscar(self, nome):
        atual = self.raiz
        nome = nome.lower()

        while atual:
            if nome == atual.bolo.nome.lower():
                return atual.bolo
            atual = atual.esquerda if nome < atual.bolo.nome.lower() else atual.direita

        return None

    def remover(self, nome):
        self.raiz = self._remover(self.raiz, nome.lower())

    def _remover(self, no, nome):
        if no is None:
            return None

        atual = no.bolo.nome.lower()

        if nome < atual:
            no.esquerda = self._remover(no.esquerda, nome)
        elif nome > atual:
            no.direita = self._remover(no.direita, nome)
        else:
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda

            sucessor = no.direita
            while sucessor.esquerda:
                sucessor = sucessor.esquerda

            no.bolo = sucessor.bolo
            no.direita = self._remover(no.direita, sucessor.bolo.nome.lower())

        return self.balancear(no)

    def percorrer(self, no, ordem):
        if no is None:
            return []

        bolo = [no.bolo]
        esquerda = self.percorrer(no.esquerda, ordem)
        direita = self.percorrer(no.direita, ordem)

        if ordem == "pre":
            return bolo + esquerda + direita
        if ordem == "pos":
            return esquerda + direita + bolo
        return esquerda + bolo + direita

    def em_ordem(self):
        return self.percorrer(self.raiz, "em")

    def pre_ordem(self):
        return self.percorrer(self.raiz, "pre")

    def pos_ordem(self):
        return self.percorrer(self.raiz, "pos")
