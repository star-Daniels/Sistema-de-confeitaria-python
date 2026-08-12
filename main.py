from MODELOS.bolo import Bolo
from MODELOS.venda import Venda
from CAIXA.caixa import realizar_venda


bolos = [
    Bolo(1, "Bolo de Café", 25.00, 3),
    Bolo(2, "Bolo de Chocolate", 30.00, 5),
    Bolo(3, "Bolo de Morango", 35.00, 2)
]
vendas=[]


realizar_venda(bolos,vendas)