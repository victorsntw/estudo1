# 🎄 Validação de Nome e Número — Python

## 📖 Descrição

Programa em Python que realiza a validação do nome do usuário e, condicionalmente, solicita a entrada de um número inteiro dentro de um intervalo específico. Desenvolvido para praticar conceitos de **estrutura condicional**, **laços de repetição** e **tratamento de exceções**.

## 🎯 Funcionalidades

- Captura e formatação do nome do usuário (remoção de espaços e capitalização).
- Verificação condicional do nome ("João").
- Loop infinito controlado (`while True`) para validação de entrada numérica.
- Tratamento de erros com `try/except` para entradas inválidas.
- Encerramento controlado via `break`.

## 🧰 Elementos e Recursos Utilizados

| Recurso | Função |
|---|---|
| `input()` | Captura de dados do usuário |
| `.strip()` | Remove espaços em branco nas extremidades |
| `.capitalize()` | Deixa a primeira letra em maiúscula |
| `if / elif / else` | Estrutura condicional |
| `while True` | Loop infinito controlado |
| `try / except ValueError` | Tratamento de exceções |
| `10 <= n <= 20` | Comparação encadeada (idiomática em Python) |
| `break` | Interrupção do loop |

## 💻 Como Executar

### Pré-requisitos
- Python 3.x instalado ([python.org](https://www.python.org/))

### Passos
```bash
# Clone o repositório (se aplicável)
git clone https://github.com/seu-usuario/seu-repositorio.git

# Acesse a pasta
cd seu-repositorio

# Execute o programa
python nome_do_arquivo.py
```

## 🖥️ Uso

1. O programa solicitará seu nome.
2. Se o nome for **João**, será solicitado um número entre 10 e 20.
3. Digite um número inteiro válido.
4. O programa encerrará automaticamente ao atender uma das condições.

## 📊 Resultado Esperado

### Exemplo 1 — Nome "João"
```
Qual é o seu nome? João
Seu nome é João!
Digite um número que esteja entre 10 e 20: 15
O número está dentro do intervalo!
```

### Exemplo 2 — Caso especial (25)
```
Qual é o seu nome? joão
Seu nome é João!
Digite um número que esteja entre 10 e 20: 25
Feliz natal João
```

### Exemplo 3 — Entrada inválida
```
Qual é o seu nome? João
Seu nome é João!
Digite um número que esteja entre 10 e 20: abc
Erro: Você precisa digitar apenas números inteiros
Digite um número que esteja entre 10 e 20: 5
O número não está dentro do intervalo!
Digite um número que esteja entre 10 e 20: 12
O número está dentro do intervalo!
```

### Exemplo 4 — Nome diferente de "João"
```
Qual é o seu nome? Maria
Seu nome não é João!
```

## 👨‍💻 Autor

**Victor** — Estudante de Programação Python

## 📜 Licença

Este projeto é de uso educacional. Sinta-se livre para estudar e adaptar.
