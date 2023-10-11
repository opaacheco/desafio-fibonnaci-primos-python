# --- Criar uma função linear que resolva p

# validação do número introduzido pelo utilizador
n = 1
while n < 2:
    n = int(input(
        "Digite um número limite para dar a sequência dos números primos até ele: "))

# criando a lista só com numeros primos


def p(n):
    listaPrimos = []
    for i in range(2, n+1):
        if i == 2 or i == 3 or i % 3 != 0 and i % 2 != 0:
            listaPrimos.append(i)
    return f"essa é a lista somente com os números primos: {listaPrimos}"


# impressão da lista
print(p(n))
