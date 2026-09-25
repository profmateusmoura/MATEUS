# Estruturas de repetição com for

O comando `for` é usado para repetir um bloco de código várias vezes.

## Sequência da aula

### 1) Primeiro passo: percorrer uma string

```python
for letra in "Python":
    print(letra)
```

Explicação:
- `for` significa: "para cada item da sequência"
- `letra` recebe cada elemento da frase ou palavra
- `in` indica de onde os elementos vêm
- a string `"Python"` é uma sequência de caracteres

Resultado esperado:

```python
P
y
t
h
o
n
```

Esse é o primeiro contato com o laço: ele percorre a sequência item por item.

### 2) Segundo passo: usar `range()`

```python
for numero in range(1, 6):
    print(numero)
```

Explicação:
- `range(1, 6)` gera: 1, 2, 3, 4, 5
- o valor final `6` não entra na sequência
- em cada repetição, a variável `numero` recebe um valor da sequência

### 3) Terceiro passo: contagem regressiva com passo negativo

```python
for numero in range(5, 0, -1):
    print(numero)
```

Explicação:
- o terceiro parâmetro `-1` é o passo
- como ele é negativo, a contagem diminui
- a sequência fica: 5, 4, 3, 2, 1

Esse é o primeiro momento em que você vê `range` com passo negativo.

### 4) Quarto passo: usar `if` dentro do `for`

```python
for numero in range(1, 11):
    if numero % 2 == 0:
        print(numero)
```

Explicação:
- o `for` percorre todos os números de 1 a 10
- o `if` verifica qual deles é par
- só os números pares são mostrados

### 5) Quinto passo: tabuada

```python
for numero in range(1, 11):
    print("5 x", numero, "=", 5 * numero)
```

Explicação:
- a variável `numero` recebe 1, 2, 3, ..., 10
- em cada volta, a operação é calculada de novo
- isso repete a mesma regra várias vezes

### 6) Sexto passo: percorrer lista

```python
nomes = ["Ana", "Bruno", "Carla", "Davi"]

for nome in nomes:
    print(nome)
```

Explicação:
- uma lista guarda vários valores em sequência
- `for nome in nomes` percorre cada elemento da lista
- em cada repetição, `nome` recebe um item da lista

## Quando usar

Use `for` quando você quer repetir algo em sequência, como:
- percorrer letras ou palavras
- contar números
- fazer tabuada
- verificar itens com `if`
- percorrer listas
- acumular valores

## Ordem de estudo recomendada

1. exemplo de string
2. exemplo de `range`
3. exemplo de contagem regressiva
4. exemplo com `if` dentro do `for`
5. exemplo de tabuada
6. exemplo com lista
7. exercícios da pasta `exercicios`

A pasta `exemplos` mostra casos simples e a pasta `exercicios` tem atividades para praticar sem respostas prontas.
