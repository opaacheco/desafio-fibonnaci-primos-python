# 1 - Fibonnaci
# função recursiva

# -- Criar uma função em sua linguagem preferida. A função deve receber um numero N >= 0 (deve validar o input para a função),
# e retornar o valor correspondente desse número na sequencia fibonnaci. EX. fib(0) =0; fib(1) = 1; fib(2) = 1; fib(3) = 2; fib(5) = 5; fib(6) = 8.

# gerar um fibonacci limitado para o código
fibonacci = [0, 1]
while len(fibonacci) < 18:
    fibonacci.append(fibonacci[-1]+fibonacci[-2])

# validação do número introduzido pelo utilizador
n = -1
while n < 0 or n > 18:
    n = int(input(
        "Um número entre 0 e 18, para retornar seu correspondente na lista Fibonacci: "))


# função que vai receber o input do utilizador para retornar o correspondente
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci[n]


# imprimindo o valor subsequente para o utilizador
print(f"O {n}º o correspondente na ordem fibonnaci é: {fib(n)}")
