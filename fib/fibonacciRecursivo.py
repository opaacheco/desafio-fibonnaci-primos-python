# --- Criar uma função recursiva que resolva fibonacci

# validação do número introduzido pelo utilizador
n = -1
while n < 2:
    n = int(input(
        "Um número index para retornar seu correspondente na lista Fibonacci: "))


# função recursiva
def fib_recursiva(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursiva(n-1) + fib_recursiva(n-2)


# a impressão do número na ordem fibonacci
print(fib_recursiva(n))
