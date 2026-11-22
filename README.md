# Sistema de Gestão de Confeitaria

Sistema de gerenciamento de confeitaria feito em Python para rodar no terminal. O projeto aplica orientação a objetos e estruturas de dados implementadas manualmente.

## Versões e branches

Cada versão está em uma branch:

| Branch | Versão | Estruturas |
| ------ | ------ | ---------- |
| `v1` | Versão 1 | Listas, pilha, fila de prioridade, Selection Sort |
| `v2` | Versão 2 | Árvore AVL, tabela hash, Merge Sort, pilha, fila de prioridade |

Para trocar de versão:

```bash
git checkout v1
git checkout v2
```

## Funcionalidades

* Cadastro de bolos e ingredientes
* Controle de estoque
* Fila de produção por prioridade
* Vendas com vários bolos
* Histórico, faturamento e total de bolos vendidos
* Login com dois tipos de usuário: administrador (`ADM`) e funcionário (`FUNC`)

| Usuário | Acesso |
| ------- | ------ |
| ADM | Cozinha, Estoque, Caixa, Histórico |
| FUNC | Caixa, Histórico |

## Estrutura do projeto

```text
CAIXA/        caixa.py            vendas
COZINHA/      cozinha.py          bolos, receitas e fila de produção
ESTOQUE/      estoque.py          ingredientes
HISTORICO/    historico.py        vendas realizadas
LOGIN/        login.py            cadastro e login
MODELOS/      bolo, item, item_venda, usuario, venda
ESTRUTURAS/   arvore_avl, tabela_hash, merge_sort, pilha, fila_prioridade
main.py
```

## Estruturas de dados na v2

| Estrutura | Onde é usada | Para quê |
| --------- | ------------ | -------- |
| Árvore AVL | Catálogo de bolos | Buscar, inserir e remover bolos por nome, com a lista sempre em ordem alfabética |
| Tabela hash | Estoque | Guardar ingredientes e impedir itens repetidos |
| Merge Sort | Histórico | Ordenar vendas do maior para o menor valor |
| Pilha | Histórico | Mostrar as vendas mais recentes primeiro |
| Fila de prioridade | Cozinha | Produzir primeiro os bolos de menor número de prioridade (1 a 5) |

## O que mudou da v1 para a v2

| Área | v1 | v2 |
| ---- | -- | -- |
| Bolos | Lista | Árvore AVL |
| Estoque | Lista | Tabela hash |
| Ordenar vendas | Selection Sort | Merge Sort |
| Itens repetidos | Permitidos | Bloqueados |

Complexidade:

| Operação | v1 | v2 |
| -------- | -- | -- |
| Buscar ou remover bolo | O(n) | O(log n) |
| Ordenar vendas | O(n²) | O(n log n) |

## Como executar

```bash
git checkout v2
python main.py
```

O sistema abre no menu de login.
