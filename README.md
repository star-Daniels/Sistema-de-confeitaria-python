# Sistema de Gestão de Confeitaria

Sistema de gerenciamento de uma confeitaria desenvolvido em Python para execução no terminal.

O projeto foi desenvolvido com o objetivo de aplicar conceitos de programação, orientação a objetos, organização de projetos e estruturas de dados.

## Objetivo

O sistema permite controlar diferentes áreas de uma confeitaria, como:

* Cadastro e gerenciamento de bolos
* Controle de ingredientes
* Produção de bolos
* Realização de vendas
* Histórico de vendas
* Cálculo de faturamento
* Controle de usuários
* Diferenciação entre administrador e funcionário

Além das funcionalidades do sistema, o projeto utiliza estruturas de dados e algoritmos implementados manualmente.

---

## Tecnologias

* Python
* Programação Orientada a Objetos
* Estruturas de Dados
* Git e GitHub

---

## Estrutura do projeto

```text
Sistema-de-confeitaria-python/
│
├── CAIXA/
│   └── caixa.py
│
├── COZINHA/
│   └── cozinha.py
│
├── ESTRUTURAS/
│   ├── fila_prioridade.py
│   └── pilha.py
│
├── ESTOQUE/
│   └── estoque.py
│
├── HISTORICO/
│   └── historico.py
│
├── LOGIN/
│   └── login.py
│
├── MODELOS/
│   ├── bolo.py
│   ├── item_venda.py
│   ├── usuario.py
│   └── venda.py
│
└── main.py
```

---

# Organização do sistema

## MODELOS

A pasta `MODELOS` contém as classes utilizadas para representar os objetos do sistema.

### `bolo.py`

Contém a classe `Bolo`.

A classe representa um bolo cadastrado na confeitaria.

Um bolo possui:

* Nome
* Preço
* Ingredientes

Os ingredientes são armazenados como objetos `Item`.

Exemplo:

```python
Bolo(
    "Bolo de Chocolate",
    35.00,
    ingredientes
)
```

O `Bolo` não possui estoque próprio. O estoque dos ingredientes é controlado separadamente pelo módulo de estoque.

---

### `item_venda.py`

Contém a classe `ItemVenda`.

Essa classe representa um bolo dentro de uma venda.

Possui:

* Bolo
* Quantidade
* Total

Exemplo:

```text
Bolo de Chocolate
Quantidade: 2
Total: R$ 70,00
```

---

### `venda.py`

Contém a classe `Venda`.

Uma venda pode possuir vários `ItemVenda`.

A classe armazena:

* Itens da venda
* Preço total da venda

Isso permite que uma única venda tenha diferentes tipos de bolo.

---

### `usuario.py`

Contém a classe `Usuario`.

Representa os usuários que podem acessar o sistema.

Possui:

* Nome
* Usuário
* Senha
* Tipo

O tipo pode ser:

```text
ADM
FUNC
```

O tipo de usuário é utilizado para controlar quais partes do sistema podem ser acessadas.

---

# ESTOQUE

A pasta `ESTOQUE` é responsável pelo controle dos ingredientes.

## `estoque.py`

Contém a classe `Item`.

Um `Item` representa um ingrediente armazenado no estoque.

Possui:

* Nome
* Quantidade

Exemplo:

```text
Farinha - 10
Ovos - 30
Chocolate - 5
```

O módulo também possui funções para:

* Adicionar ingredientes
* Remover ingredientes
* Listar o estoque

O estoque é armazenado em uma lista.

---

# COZINHA

A pasta `COZINHA` controla os bolos e a produção.

## `cozinha.py`

Esse módulo é responsável por:

* Cadastrar bolos
* Remover bolos
* Listar bolos
* Pesquisar bolos
* Verificar ingredientes
* Calcular quantos bolos podem ser produzidos
* Retirar ingredientes do estoque
* Controlar a fila de produção

### Busca de ingredientes

A função `buscar_item()` percorre o estoque procurando um ingrediente pelo nome.

Ela utiliza uma busca sequencial:

```python
for item in estoque:
    if item.nome == nome:
        return item
```

Isso demonstra a utilização de um algoritmo de busca implementado manualmente.

---

### Quantidade de bolos possíveis

A função `quantidade_bolos_possiveis()` verifica quantos bolos podem ser produzidos com os ingredientes disponíveis.

Por exemplo, se um bolo precisa de:

```text
2 ovos
1 farinha
```

e o estoque possui:

```text
10 ovos
3 farinhas
```

o sistema calcula:

```text
10 / 2 = 5
3 / 1 = 3
```

Portanto, podem ser produzidos 3 bolos.

O ingrediente que permite produzir a menor quantidade determina o limite de produção.

---

### Retirada de ingredientes

A função `retirar_ingredientes()` diminui do estoque os ingredientes utilizados na produção ou venda.

Por exemplo:

```text
Estoque:
Farinha: 10
```

Se forem utilizados 2:

```text
Farinha: 8
```

---

# CAIXA

A pasta `CAIXA` é responsável pelas vendas.

## `caixa.py`

O módulo permite:

* Listar bolos disponíveis
* Selecionar um bolo
* Definir quantidade
* Calcular o valor da venda
* Adicionar vários bolos à mesma venda
* Confirmar ou cancelar uma venda
* Registrar a venda no histórico

Antes de permitir uma venda, o sistema verifica a quantidade de bolos que pode ser produzida com os ingredientes disponíveis.

Quando a venda é confirmada, os ingredientes utilizados são retirados do estoque.

---

# HISTÓRICO

A pasta `HISTORICO` é responsável pelas informações das vendas realizadas.

## `historico.py`

O módulo possui funções para:

* Listar vendas
* Listar vendas ordenadas por valor
* Calcular faturamento
* Calcular quantidade de bolos vendidos

### Listar vendas

A função `listar_vendas()` utiliza uma pilha para apresentar as vendas mais recentes primeiro.

Isso segue o conceito:

```text
LIFO
Last In, First Out
```

Ou seja:

```text
Última venda registrada
        ↓
Primeira venda exibida
```

A pilha é utilizada sem eliminar permanentemente as vendas do histórico.

---

### Listar vendas por valor

A função `listar_vendas_por_valor()` utiliza o algoritmo **Selection Sort**.

O algoritmo procura a maior venda restante e coloca essa venda na posição correta.

As vendas são organizadas do maior para o menor valor.

O algoritmo é implementado manualmente, sem utilizar:

```python
sorted()
```

---

### Calcular faturamento

A função `calcular_faturamento()` percorre todas as vendas e soma o valor de cada item vendido.

Exemplo:

```text
Venda 1: R$ 50,00
Venda 2: R$ 80,00
Venda 3: R$ 30,00

Faturamento: R$ 160,00
```

---

### Quantidade de bolos vendidos

A função `qtd_bolos_vendidos()` percorre todas as vendas e soma as quantidades dos bolos vendidos.

---

# LOGIN

A pasta `LOGIN` controla o acesso ao sistema.

## `login.py`

O módulo permite:

* Cadastrar usuários
* Pesquisar usuários
* Realizar login

Durante o cadastro, o usuário escolhe entre:

```text
1 - Administrador
2 - Funcionário
```

O sistema então armazena:

```text
ADM
```

ou:

```text
FUNC
```

---

# Permissões

O tipo de usuário determina quais módulos podem ser acessados.

## Administrador

O administrador possui acesso a:

```text
Cozinha
Estoque
Caixa
Histórico
```

## Funcionário

O funcionário possui acesso a:

```text
Caixa
Histórico
```

Dessa forma, o sistema possui diferentes níveis de acesso.

---

# ESTRUTURAS

A pasta `ESTRUTURAS` contém as estruturas de dados utilizadas no projeto.

## Lista

As listas são utilizadas em diferentes partes do sistema.

Exemplos:

```python
lista_bolo = []
estoque = []
vendas = []
```

As listas permitem armazenar vários objetos e percorrê-los utilizando estruturas de repetição.

---

## Pilha

A pilha está implementada em `pilha.py`.

A estrutura segue o conceito:

```text
LIFO
Last In, First Out
```

O último elemento inserido é o primeiro a ser retirado.

Principais operações:

### `empilhar()`

Adiciona um elemento ao topo da pilha.

### `desempilhar()`

Remove e retorna o elemento que está no topo.

### `topo()`

Retorna o elemento do topo sem removê-lo.

### `vazia()`

Verifica se a pilha está vazia.

A pilha é utilizada no histórico para mostrar primeiro as vendas mais recentes.

---

## Fila de prioridade

A fila de prioridade está implementada em `fila_prioridade.py`.

Diferentemente de uma fila comum, os elementos são atendidos de acordo com sua prioridade.

No sistema, ela é utilizada para controlar a produção de bolos.

Cada bolo recebe uma prioridade de 1 a 5.

Exemplo:

```text
Bolo A → prioridade 2
Bolo B → prioridade 5
Bolo C → prioridade 3
```

O sistema irá retirar primeiro:

```text
Bolo B
```

porque possui a maior prioridade.

A busca da maior prioridade é realizada manualmente.

---

# Algoritmos

O projeto utiliza algoritmos implementados manualmente.

## Busca sequencial

A busca sequencial percorre os elementos um por um até encontrar o elemento procurado.

Exemplo:

```python
for bolo in lista_bolo:

    if bolo.nome == nome:

        return bolo
```

É utilizada para encontrar bolos e ingredientes.

---

## Selection Sort

O projeto utiliza Selection Sort para ordenar as vendas pelo valor total.

O algoritmo procura o maior elemento e troca sua posição com o elemento atual.

Exemplo:

```python
for i in range(len(vendas)):

    maior = i

    for j in range(i + 1, len(vendas)):

        if vendas[j].preco_total > vendas[maior].preco_total:

            maior = j

    vendas[i], vendas[maior] = vendas[maior], vendas[i]
```

O resultado é uma lista ordenada do maior valor para o menor.

---

# Fluxo do sistema

O sistema começa pelo `main.py`.

```text
main.py
   |
   v
Menu de Login
   |
   +-- Entrar
   |
   +-- Cadastrar usuário
   |
   v
Usuário autenticado
   |
   v
Menu Principal
   |
   +-- Cozinha
   |
   +-- Estoque
   |
   +-- Caixa
   |
   +-- Histórico
   |
   v
Sair
```

---

# Fluxo de uma venda

Uma venda segue o seguinte processo:

```text
Selecionar bolo
      |
      v
Informar quantidade
      |
      v
Verificar ingredientes
      |
      v
Adicionar bolo à venda
      |
      v
Adicionar outros bolos
      |
      v
Exibir resumo
      |
      v
Confirmar venda
      |
      v
Retirar ingredientes
      |
      v
Registrar venda
      |
      v
Histórico
```

---

# Requisitos de estruturas de dados

O projeto utiliza os requisitos propostos:

| Requisito          | Implementação                  |
| ------------------ | ------------------------------ |
| Lista              | Bolos, estoque, vendas e itens |
| Pilha              | Histórico de vendas            |
| Fila de prioridade | Fila de produção               |
| Busca manual       | Busca de bolos e ingredientes  |
| Ordenação manual   | Selection Sort                 |

---

# Execução

Para executar o sistema, abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

O sistema será iniciado pelo menu de login.

---

# Objetivo acadêmico

O projeto tem como principal objetivo demonstrar na prática a utilização de:

* Python
* Classes e objetos
* Funções
* Listas
* Pilhas
* Filas de prioridade
* Busca sequencial
* Selection Sort
* Modularização
* Controle de acesso
* Manipulação de dados em memória
* Organização de um sistema em diferentes módulos

```

Esse README já fica adequado para colocar no GitHub e também deixa claro **onde cada requisito do trabalho foi aplicado**, principalmente Lista, Pilha, Fila de Prioridade, Busca e Selection Sort.

Se quiser, depois podemos fazer uma segunda versão mais "profissional de GitHub", com **badges, instalação, exemplos de uso e screenshots**, mas essa versão acima é melhor para explicar o projeto acadêmico.
```
