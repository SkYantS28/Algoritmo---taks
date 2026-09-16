# 🚀 Exercícios de Python — Exploração Espacial e Mitologia

Coleção de exercícios desenvolvidos em **Python**, utilizando diferentes estruturas de programação para resolver problemas baseados em temas de exploração espacial, ficção científica e mitologia.

Os exercícios foram desenvolvidos com foco na prática de **estruturas de repetição, listas, manipulação de strings, condicionais, entrada de dados e funções nativas do Python**.

---

## 📚 Exercícios

### ⭐ 1. Contagem de Estrelas

Simula a contagem de estrelas em uma constelação.

O usuário informa a quantidade de estrelas que deseja contar e o programa exibe cada número da contagem até atingir o valor informado.

**Conceitos utilizados:**

* `input()`
* `int()`
* `for`
* `range()`
* `print()`

---

### 🪐 2. Orbitando Saturno

Simula a quantidade de voltas que uma nave espacial realiza ao redor de Saturno.

O programa recebe a quantidade de voltas e informa cada volta realizada, tratando também a diferença entre singular e plural.

**Conceitos utilizados:**

* `for`
* `range()`
* `if/else`
* F-strings
* Entrada de dados

---

### 🕳️ 3. Viagem ao Passado em "Interestelar"

Simula, de maneira simplificada, a dilatação temporal apresentada no filme *Interestelar*.

O usuário informa a quantidade de horas passadas próximo a um buraco negro e o programa calcula quantos anos teriam passado na Terra.

Neste exercício, foi utilizada a proporção fictícia de:

> **1 hora próximo ao buraco negro = 7 anos na Terra**

**Conceitos utilizados:**

* Operações matemáticas
* `input()`
* `int()`
* `if/else`
* F-strings

---

### 🔴 4. Escala Richter em Marte

Simula o registro de terremotos em Marte (*marsquakes*).

O programa solicita a magnitude dos terremotos registrados e identifica o dia em que ocorreu o terremoto de maior magnitude.

**Conceitos utilizados:**

* Listas
* `for`
* `append()`
* `max()`
* `index()`
* `float()`

O exercício também permite compreender uma particularidade do método `.index()`: quando existem valores máximos repetidos, ele retorna a posição da **primeira ocorrência**.

---

### 🚨 5. Sistema de Evacuação de Prometheus

Simula uma contagem regressiva para a evacuação da tripulação da nave.

O usuário informa o tempo inicial em segundos e o programa exibe a contagem regressiva até chegar a zero.

**Conceitos utilizados:**

* `list()`
* `range()`
* `while`
* `len()`
* Índices de listas
* Condicionais
* F-strings

---

### 👽 6. Decifrando Mensagens do Espaço

Simula a decodificação de uma mensagem alienígena representada por números.

O usuário informa uma sequência de números separados por espaços. Cada número corresponde a uma letra do alfabeto:

```text
1 = a
2 = b
3 = c
...
26 = z
```

O programa converte os números em letras e utiliza `join()` para formar a mensagem final.

**Conceitos utilizados:**

* `input()`
* `split()`
* Listas
* `append()`
* `for`
* `if/elif/else`
* Conversão com `int()`
* `join()`
* Manipulação de strings

**Exemplo:**

```text
Entrada:
8 5 12 12 15

Saída:
Mensagem decodificada: hello
```

---

### 🏛️ 7. A Viagem de Ulisses

Baseado na **Odisseia**, este exercício simula a navegação de Ulisses entre diferentes ilhas.

As ilhas são representadas por números de **1 a 10**, e o usuário informa a ordem em que deseja visitá-las.

A distância entre duas ilhas é calculada a partir da diferença entre seus números:

```text
distância = 2 × |ilha atual - próxima ilha|
```

Ao final, o programa soma todas as distâncias para determinar a distância total percorrida.

**Conceitos utilizados:**

* `input()`
* `split()`
* `map()`
* `int()`
* Listas
* `while`
* `len()`
* `abs()`
* Condicionais
* Operações matemáticas

---

## 🧠 Conceitos praticados

Ao longo dos exercícios foram praticados diversos fundamentos da linguagem Python:

| Conceito       | Utilização                            |
| -------------- | ------------------------------------- |
| `input()`      | Entrada de informações do usuário     |
| `print()`      | Exibição de informações               |
| `int()`        | Conversão para números inteiros       |
| `float()`      | Conversão para números decimais       |
| `for`          | Estruturas de repetição               |
| `while`        | Repetição baseada em condição         |
| `range()`      | Criação de sequências numéricas       |
| `if/elif/else` | Estruturas condicionais               |
| Listas         | Armazenamento de vários valores       |
| `append()`     | Adição de elementos em listas         |
| `max()`        | Identificação do maior valor          |
| `index()`      | Localização de um elemento            |
| `split()`      | Divisão de uma string                 |
| `join()`       | União de strings                      |
| `map()`        | Aplicação de uma função aos elementos |
| `abs()`        | Cálculo do valor absoluto             |
| F-strings      | Formatação de textos                  |

---

## 🛠️ Tecnologias

* **Python 3**
* Programação estruturada
* Estruturas de repetição
* Estruturas condicionais
* Manipulação de listas e strings

---

## 📂 Estrutura

```text
📁 projeto/
│
├── exercicio1.py
├── exercicio2.py
├── exercicio3.py
├── exercicio4.py
├── exercicio5.py
├── exercicio6.py
├── exercicio7.py
└── README.md
```

> Os nomes dos arquivos podem variar de acordo com a organização utilizada no projeto.

---

## ▶️ Como executar

### 1. Instale o Python

Certifique-se de possuir o **Python 3** instalado no computador.

### 2. Clone o repositório

```bash
git clone URL_DO_REPOSITORIO
```

### 3. Acesse a pasta

```bash
cd NOME_DO_PROJETO
```

### 4. Execute um exercício

Por exemplo:

```bash
python exercicio1.py
```

No Windows, também pode ser necessário utilizar:

```bash
py exercicio1.py
```

---

## 🎯 Objetivo

O objetivo da atividade é desenvolver e reforçar conhecimentos fundamentais de **programação em Python**, utilizando problemas contextualizados para praticar lógica de programação e manipulação de dados.

Os exercícios trabalham progressivamente diferentes recursos da linguagem, desde estruturas básicas de repetição até manipulação de listas, strings e cálculos utilizando funções nativas.

---

## 👩‍💻 Autora

**Sky Crizosti**

Estudante de **Engenharia de Software**.

---

## 📖 Contexto acadêmico

Projeto desenvolvido como atividade acadêmica para prática de **lógica de programação e fundamentos de Python**.
