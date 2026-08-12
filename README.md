# Sistema de Gestão para Confeitaria

## 1. Objetivo

Sistema desenvolvido em **Python**, inicialmente executado pelo **terminal**, para controlar receitas, ingredientes, produção, estoque, vendas e lucros de uma confeitaria.

Os dados serão armazenados em arquivos **`.txt`**, sem banco de dados nesta primeira versão.

---

# 2. Funcionalidades

##  2.1. Cozinha

Responsável pelas receitas e produção dos bolos.

- Cadastrar bolo/receita;
- Editar bolo/receita;
- Listar e consultar bolos;
- Adicionar e remover ingredientes;
- Definir quantidades dos ingredientes;
- Separar ingredientes base e especiais;
- Calcular custo e lucro;
- Avisar quando um bolo gerar prejuízo;
- Produzir bolo;
- Verificar se existem ingredientes suficientes antes da produção;
- Retirar os ingredientes utilizados do estoque;
- Adicionar o bolo produzido ao estoque de bolos prontos.

### Receita x estoque

Um bolo cadastrado representa uma **receita**, não uma unidade pronta.

Exemplo:

```text
Bolo de Café
├── Farinha: 500 g
├── Açúcar: 300 g
├── Ovos: 3 un.
└── Café: 50 g
```

O bolo pode estar cadastrado mesmo com estoque de bolos prontos igual a `0`.

---

##  2.2. Estoque

Responsável pelo controle dos ingredientes e dos bolos prontos.

### Ingredientes

- Cadastrar ingredientes;
- Definir unidade de medida;
- Definir preço;
- Consultar quantidade disponível;
- Ver quantos bolos podem ser produzidos;
- Reabastecer ingredientes;
- Definir quantidade fixa para reposição.

### Bolos prontos

- Consultar quantidade de bolos produzidos;
- Receber entrada após uma produção;
- Dar saída após uma venda.

O estoque será dividido em:

```text
Ingredientes
    ↓
Farinha, ovos, açúcar, chocolate...

Bolos prontos
    ↓
Bolo de Café, Bolo de Chocolate...
```

---

##  2.3. Caixa

Responsável pelas vendas.

- Registrar venda;
- Escolher o bolo;
- Informar quantidade;
- Verificar disponibilidade;
- Dar baixa no estoque de bolos prontos;
- Registrar valor da venda.

---

##  2.4. Histórico

Responsável pelo acompanhamento das vendas e resultados.

- Consultar vendas;
- Consultar bolos vendidos;
- Consultar quantidades;
- Consultar faturamento;
- Consultar custos;
- Consultar lucro;
- Consultar resultados por período;
- Visualizar lucro mensal.

---

# 3. Cálculo de Custos

O custo será calculado proporcionalmente à quantidade utilizada de cada ingrediente.

Exemplo:

```text
12 ovos = R$ 12,00
Receita = 3 ovos

Custo dos ovos = R$ 3,00
```

O custo total será:

```text
Custo do bolo =
ingrediente 1
+ ingrediente 2
+ ingrediente 3
+ ...
```

E:

```text
Lucro = Preço de venda - Custo do bolo
```

Caso o resultado seja negativo, o sistema deverá informar **prejuízo**.

---

# 4. Produção

Ao escolher **Produzir Bolo**, o sistema deverá:

```text
1. Escolher a receita
2. Verificar o estoque
3. Conferir todos os ingredientes
4. Se faltar algo → cancelar produção
5. Se houver tudo → retirar ingredientes
6. Adicionar bolo ao estoque de prontos
```

Nenhum ingrediente deverá ser retirado caso a produção não possa ser concluída.

---

# 5. Armazenamento

Os dados serão armazenados em arquivos `.txt`.

```text
dados/
├── ingredientes.txt
├── estoque.txt
├── bolos.txt
├── receitas.txt
├── estoque_bolos.txt
└── vendas.txt
```

### Arquivos

**ingredientes.txt**  
Cadastro e preço dos ingredientes.

**estoque.txt**  
Quantidade atual dos ingredientes.

**bolos.txt**  
Bolos cadastrados e seus preços.

**receitas.txt**  
Ingredientes e quantidades de cada receita.

**estoque_bolos.txt**  
Quantidade de cada bolo pronto.

**vendas.txt**  
Registro das vendas.

---

# 6. Estrutura do Projeto

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
├── estoque/
│   └── estoque.py
│
├── caixa/
│   └── caixa.py
│
└── historico/
    └── historico.py
```

---

# 7. Extras

Funcionalidades e recursos de apoio:

- Sistema de IDs;
- Validação de dados;
- Alertas de prejuízo;
- Cálculo proporcional de ingredientes;
- Ingredientes base e especiais;
- Atualização automática dos arquivos `.txt`;
- Menu principal do terminal.

---

# 8. Fluxo Principal

```text
 COZINHA
    ↓
Receita
    ↓
Produção
    ↓
 ESTOQUE
    ↓
Bolo pronto
    ↓
 CAIXA
    ↓
Venda
    ↓
 HISTÓRICO
    ↓
Lucro / Faturamento
```
