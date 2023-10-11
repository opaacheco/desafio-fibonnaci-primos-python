# --- Criar uma função recursiva que resolva p

# validação do número introduzido pelo utilizador
n = 1
while n < 2:
    n = int(input(
        "Digite um número limite para dar a sequência dos números primos até ele: "))


# lista que vai guarda os números
listaPrimos = []


# função recursiva que cria a lista com os números e depois verifica se é primo ou não
def p(lista, numero):
    if numero >= 2:
        lista.append(numero)
        p(lista, numero-1)
    primos = list(filter(lambda item: item == 2 or item == 3 or (
        item > 3 and item % 3 != 0 and item % 2 != 0), lista))
    return primos


# ponto a lista somente com números primos
listaPrimos = p(listaPrimos, n)

# ordenando a lista
listaPrimos.sort()

# imprimindo os números primos
print(f"Essa é a lista somente ecom números primos: {listaPrimos}")
