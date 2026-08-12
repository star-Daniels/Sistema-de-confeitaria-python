# Sistema de Gestão para Confeitaria

## 1. Objetivo do Projeto

O projeto consiste no desenvolvimento de um sistema de gestão para uma confeitaria, inicialmente executado diretamente pelo terminal utilizando Python.

O objetivo principal é facilitar o controle de:

- Receitas de bolos;
- Ingredientes;
- Estoque de ingredientes;
- Produção de bolos;
- Estoque de bolos prontos;
- Vendas;
- Custos;
- Lucros;
- Histórico financeiro.

O sistema deverá calcular corretamente o custo e o lucro de cada bolo considerando a quantidade de cada ingrediente utilizada na receita.

O sistema não deverá considerar simplesmente o preço total de um produto comprado. Ele deverá calcular proporcionalmente o custo da quantidade utilizada.

### Exemplo

Uma dúzia de ovos custa R$ 12,00.

Se uma receita utiliza 3 ovos:

```text
12 ovos = R$ 12,00
3 ovos  = R$ 3,00
```

Portanto, o custo de ovos utilizado em um bolo será de R$ 3,00.

O mesmo princípio será aplicado aos demais ingredientes.

---

# 2. Funcionamento Geral

O sistema será dividido em três áreas principais:

1. Cozinha de Bolos;
2. Armazém;
3. Caixa e Histórico.

Além disso, haverá uma separação entre:

- **Bolos cadastrados**, que representam as receitas;
- **Ingredientes em estoque**;
- **Bolos prontos em estoque**.

Um bolo pode estar cadastrado no sistema mesmo que não exista nenhuma unidade pronta e mesmo que não existam ingredientes suficientes para produzi-lo.

### Fluxo principal

```text
Receita cadastrada
       ↓
Verificação do estoque
       ↓
Produção do bolo
       ↓
Ingredientes são retirados do estoque
       ↓
Bolo é adicionado ao estoque de bolos prontos
       ↓
Venda
       ↓
Bolo pronto é retirado do estoque
       ↓
Venda registrada no histórico
```

---

# 3. Cozinha de Bolos

A cozinha será responsável pelo gerenciamento das receitas e pela produção dos bolos.

## 3.1. Cadastro de Bolos

O usuário poderá cadastrar novos bolos informando:

- Nome;
- Preço de venda;
- Ingredientes;
- Quantidade de cada ingrediente;
- Tipo do ingrediente.

O cadastro do bolo representa sua **receita**, e não uma unidade física pronta.

### Exemplo

```text
Bolo de Café

Farinha: 500 g
Açúcar: 300 g
Ovos: 3 unidades
Café: 50 g
```

O Bolo de Café continuará cadastrado mesmo que seu estoque de bolos prontos seja igual a zero.

---

## 3.2. Edição de Bolos

Será possível editar os bolos já cadastrados.

O usuário poderá:

- Alterar o nome;
- Alterar o preço;
- Adicionar ingredientes;
- Remover ingredientes;
- Alterar a quantidade dos ingredientes.

---

## 3.3. Ingredientes Base e Especiais

Os ingredientes das receitas serão divididos em duas categorias.

### Ingredientes Base

São os ingredientes utilizados na estrutura básica do bolo.

Exemplos:

- Farinha;
- Açúcar;
- Ovos;
- Leite;
- Fermento.

### Ingredientes Especiais

São os ingredientes utilizados principalmente para definir o sabor ou característica específica do bolo.

Exemplos:

- Chocolate;
- Café;
- Morango;
- Coco;
- Doce de leite.

Essa separação permitirá utilizar uma mesma base para diferentes tipos de bolo.

---

# 4. Produção de Bolos

O sistema terá uma função específica para **produzir um bolo**.

O usuário poderá escolher uma das receitas cadastradas e informar que deseja produzi-la.

Exemplo:

```text
COZINHA

1 - Cadastrar bolo
2 - Editar bolo
3 - Listar bolos
4 - Produzir bolo
0 - Voltar
```

Ao selecionar a opção de produção, o sistema apresentará os bolos cadastrados.

```text
1 - Bolo de Café
2 - Bolo de Chocolate
3 - Bolo de Morango
0 - Voltar
```

Depois de escolher o bolo, o sistema verificará automaticamente se existem ingredientes suficientes no estoque.

---

## 4.1. Verificação de Estoque

Antes de produzir o bolo, o sistema deverá verificar todos os ingredientes necessários para a receita.

### Exemplo

Receita:

```text
Bolo de Café

Farinha: 500 g
Açúcar: 300 g
Ovos: 3
Café: 50 g
```

Estoque:

```text
Farinha: 2 kg
Açúcar: 1 kg
Ovos: 6
Café: 100 g
```

Nesse caso, todos os ingredientes estão disponíveis e o bolo poderá ser produzido.

---

## 4.2. Ingredientes Insuficientes

Caso um ou mais ingredientes não estejam disponíveis em quantidade suficiente, o sistema não deverá realizar a produção.

Exemplo:

```text
Não é possível produzir o Bolo de Café.

Ingredientes insuficientes:

Ovos
Necessário: 3
Disponível: 2

Café
Necessário: 50 g
Disponível: 20 g
```

Nenhum ingrediente deverá ser retirado do estoque quando a produção não puder ser concluída.

---

## 4.3. Produção Bem-Sucedida

Quando todos os ingredientes necessários estiverem disponíveis:

1. Os ingredientes serão retirados do estoque;
2. O bolo será adicionado ao estoque de bolos prontos;
3. A produção será registrada.

Exemplo:

```text
Antes:

Ovos: 6
Farinha: 2 kg
Café: 100 g

Bolos de Café prontos: 0
```

Após produzir um bolo:

```text
Depois:

Ovos: 3
Farinha: 1,5 kg
Café: 50 g

Bolos de Café prontos: 1
```

---

# 5. Armazém

O armazém será responsável pelo controle dos estoques.

O estoque será dividido em duas categorias:

1. Estoque de ingredientes;
2. Estoque de bolos prontos.

---

## 5.1. Estoque de Ingredientes

O sistema armazenará a quantidade disponível de cada ingrediente.

Exemplo:

```text
Farinha: 2,5 kg
Açúcar: 1,8 kg
Ovos: 12 unidades
Café: 500 g
Chocolate: 1 kg
```

Também será possível visualizar quanto de cada ingrediente está disponível em relação à quantidade necessária para produzir os bolos.

---

## 5.2. Estoque de Bolos Prontos

O estoque de bolos prontos será separado do estoque de ingredientes.

Ele representará somente os bolos que já foram produzidos e ainda estão disponíveis para venda.

Exemplo:

```text
Bolo de Café: 3
Bolo de Chocolate: 5
Bolo de Morango: 2
```

Um bolo cadastrado pode existir no sistema com:

```text
Bolo de Café: 0 unidades
```

Isso significa que a receita existe, mas nenhuma unidade foi produzida.

---

## 5.3. Reabastecimento de Ingredientes

O usuário poderá reabastecer os ingredientes do estoque.

Existirão duas possibilidades:

### Reabastecimento Manual

O usuário informa quanto deseja adicionar.

```text
Farinha atual: 2 kg

Adicionar: 5 kg

Novo estoque: 7 kg
```

### Quantidade Fixa de Reabastecimento

O usuário poderá definir uma quantidade padrão para determinado ingrediente.

Exemplo:

```text
Farinha

Estoque atual: 2 kg
Quantidade de reposição: 5 kg
```

Ao selecionar a opção de reabastecer, o sistema adicionará automaticamente os 5 kg.

---

# 6. Caixa

O caixa será responsável pelo registro das vendas dos bolos.

Ao realizar uma venda, o sistema deverá verificar se existe a quantidade solicitada do bolo no estoque de bolos prontos.

### Exemplo

```text
Bolo de Café em estoque: 3

Venda:
Quantidade: 1

Novo estoque:
Bolo de Café: 2
```

Caso não existam unidades suficientes, a venda não deverá ser realizada.

O sistema registrará informações como:

- Bolo vendido;
- Quantidade;
- Preço de venda;
- Valor total;
- Custo;
- Lucro.

---

# 7. Histórico

O histórico armazenará as informações das vendas realizadas.

Será possível consultar informações relacionadas ao desempenho da confeitaria.

Entre elas:

- Bolos vendidos;
- Quantidade vendida;
- Faturamento;
- Custos;
- Lucro;
- Lucro mensal.

O objetivo é permitir acompanhar o resultado financeiro da confeitaria ao longo do tempo.

---

# 8. Cálculo de Custos

O sistema deverá calcular o custo de cada bolo com base na quantidade utilizada de cada ingrediente.

### Exemplo

```text
12 ovos = R$ 12,00

Receita utiliza:
3 ovos
```

Cálculo:

```text
12 ÷ 3 = 4 bolos

R$ 12,00 ÷ 4 = R$ 3,00 por bolo
```

O mesmo cálculo será realizado para todos os ingredientes.

Ao final:

```text
Custo total =
custo da farinha
+ custo do açúcar
+ custo dos ovos
+ custo do café
+ outros ingredientes
```

---

# 9. Cálculo de Lucro

O lucro será calculado utilizando o preço de venda e o custo de produção.

```text
Lucro = Preço de venda - Custo de produção
```

### Exemplo

```text
Preço de venda: R$ 30,00
Custo de produção: R$ 18,00

Lucro: R$ 12,00
```

Caso o custo seja maior que o preço de venda:

```text
Preço de venda: R$ 20,00
Custo de produção: R$ 23,00

Resultado: -R$ 3,00

⚠ PREJUÍZO
```

O sistema deverá informar quando um bolo estiver gerando prejuízo.

---

# 10. Armazenamento dos Dados

Nesta primeira versão, o sistema não utilizará banco de dados.

As informações serão armazenadas em arquivos **`.txt`**.

Isso permitirá manter o projeto simples e adequado à execução pelo terminal.

---

# 11. Estrutura de Pastas

A estrutura inicial do projeto será:

```text
sistema_confeitaria/
│
├── main.py
│
├── dados/
│   ├── ingredientes.txt
│   ├── estoque.txt
│   ├── bolos.txt
│   ├── receitas.txt
│   ├── estoque_bolos.txt
│   └── vendas.txt
│
├── cozinha/
│   └── cozinha.py
│
├── armazem/
│   └── armazem.py
│
├── caixa/
│   └── caixa.py
│
└── historico/
    └── historico.py
```

---

# 12. Arquivos de Dados

## ingredientes.txt

Armazena os ingredientes cadastrados e seus respectivos preços.

```text
ID|Nome|Unidade|Preço
```

Exemplo:

```text
1|Farinha|kg|8.50
2|Açúcar|kg|4.50
3|Ovos|un|1.00
4|Café|kg|30.00
5|Chocolate|kg|40.00
```

---

## estoque.txt

Armazena a quantidade atual dos ingredientes.

```text
ID|Nome|Quantidade
```

Exemplo:

```text
1|Farinha|2.5
2|Açúcar|1.8
3|Ovos|12
4|Café|0.5
5|Chocolate|1.0
```

---

## bolos.txt

Armazena os bolos cadastrados no sistema.

Esse arquivo representa as receitas disponíveis, e não o estoque físico de bolos.

```text
ID|Nome|Preço de venda
```

Exemplo:

```text
1|Bolo de Café|25.00
2|Bolo de Chocolate|30.00
3|Bolo de Morango|35.00
```

---

## receitas.txt

Relaciona cada bolo aos ingredientes utilizados em sua receita.

```text
ID_Bolo|ID_Ingrediente|Quantidade
```

Exemplo:

```text
1|1|0.5
1|2|0.3
1|3|3
1|4|0.05
```

Isso representa:

```text
Bolo de Café

Farinha: 0,5 kg
Açúcar: 0,3 kg
Ovos: 3 unidades
Café: 0,05 kg
```

---

## estoque_bolos.txt

Armazena somente os bolos que já foram produzidos.

```text
ID|Nome|Quantidade
```

Exemplo:

```text
1|Bolo de Café|3
2|Bolo de Chocolate|5
3|Bolo de Morango|0
```

---

## vendas.txt

Armazena as vendas realizadas pelo sistema.

Esse arquivo será utilizado posteriormente pelo módulo de histórico para calcular os resultados financeiros.

---

# 13. Interface Inicial do Terminal

A aplicação será iniciada através do arquivo `main.py`.

O menu principal deverá apresentar as principais áreas do sistema.

Exemplo:

```text
================================
       SISTEMA CONFEITARIA
================================

1 - Cozinha de Bolos
2 - Armazém
3 - Caixa
4 - Histórico
0 - Sair

Escolha uma opção:
```

Cada opção deverá direcionar o usuário para o respectivo módulo.

---

# 14. Escopo da Primeira Versão

A primeira versão terá como foco implementar:

- Cadastro de ingredientes;
- Controle de estoque de ingredientes;
- Cadastro de receitas;
- Edição de receitas;
- Separação entre ingredientes base e especiais;
- Cadastro de bolos;
- Cálculo de custo;
- Cálculo de lucro;
- Identificação de prejuízo;
- Produção de bolos;
- Verificação de ingredientes antes da produção;
- Baixa automática dos ingredientes utilizados;
- Estoque de bolos prontos;
- Reabastecimento de ingredientes;
- Registro de vendas;
- Baixa dos bolos vendidos;
- Histórico de vendas e lucros;
- Persistência dos dados através de arquivos `.txt`.

O projeto será inicialmente desenvolvido de forma simples e modular, executando diretamente pelo terminal. Posteriormente, a estrutura poderá ser expandida para uma interface gráfica ou outro sistema de armazenamento, caso seja necessário.
