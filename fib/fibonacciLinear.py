# --- Criar uma função linear que resolva fibonnaci

# validação do número introduzido pelo utilizador
n = -1
while n < 2:
    n = int(input(
        "Um número index para retornar seu correspondente na lista Fibonacci: "))


# função linear
def fib_linear(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a+b
        return b


# a impressão do número na ordem fibonacci
print(fib_linear(n))
