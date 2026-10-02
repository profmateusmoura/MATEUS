# Estruturas de repetição com while

O comando `while` repete um bloco de código enquanto uma condição for verdadeira.

## Sequência da aula

### 1) Primeiro passo: contar

```python
numero = 1

while numero <= 5:
    print(numero)
    numero = numero + 1
```

Explicação:
- `while` significa "enquanto"
- a condição `numero <= 5` é verificada antes de cada repetição
- `numero = numero + 1` atualiza o contador
- quando `numero` chega a 6, a condição fica falsa e o laço termina

### 2) Segundo passo: contagem regressiva

```python
numero = 5

while numero >= 1:
    print(numero)
    numero = numero - 1
```

Explicação:
- o contador começa em 5
- em cada repetição, ele diminui 1
- o laço termina quando o contador fica menor que 1

### 3) Terceiro passo: usar `if` dentro do `while`

```python
numero = 1

while numero <= 10:
    if numero % 2 == 0:
        print(numero)
    numero = numero + 1
```

Explicação:
- o `while` percorre os números de 1 a 10
- o `if` mostra apenas os números pares
- o contador avança em todas as repetições

### 4) Quarto passo: acumular valores

```python
numero = 1
soma = 0

while numero <= 5:
    soma = soma + numero
    numero = numero + 1

print("Soma:", soma)
```

Explicação:
- `soma` guarda o total acumulado
- cada número é adicionado uma vez
- ao final, o resultado é 15

### 5) Quinto passo: repetir até uma resposta de saída

```python
resposta = ""

while resposta != "sair":
    resposta = input("Digite sair para encerrar: ")
```

Explicação:
- nesse caso, não sabemos antecipadamente quantas repetições serão necessárias
- o laço continua até a pessoa digitar `sair`

## Atenção ao contador

Em um `while`, é importante que algo dentro do laço possa tornar a condição falsa. Se a condição nunca mudar, o programa pode ficar repetindo para sempre. Confira se o contador ou a resposta de saída são atualizados.

## Quando usar

Use `while` quando a repetição depende de uma condição ou quando você não sabe antecipadamente quantas vezes o bloco precisará repetir.

## Ordem de estudo recomendada

1. exemplos de contador e contagem regressiva
2. exemplos com condição e `if`
3. exemplos de soma e entrada do usuário
4. exercícios da pasta `exercicios`

A pasta `exemplos` mostra casos simples e a pasta `exercicios` tem atividades para praticar sem respostas prontas.
