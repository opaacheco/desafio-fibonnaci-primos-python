# 2 - Números primos -- Criar uma função em sua linguagem preferida. A função deve receber um numero N > 1 (validar o input),
# e retornar todos os números primos até o numero N. EX. p(2) = [2]; p(3) = [2, 3]; p(10) = [2, 3, 5, 7];

# validação do número introduzido pelo utilizador
n = 1
while n <= 1:
    n = int(input(
        "Digite um número limite para dar a sequência dos números primos até ele: "))


# criando a lista com todos os números até chegar no número escolhido pelo utilizador
novaLista = []
for i in range(n+1):
    novaLista.append(i)


# verificação se os números são primos
def isPrimo(lista):
    primos = list(filter(lambda item: item == 2 or item == 3 or (
        item > 3 and item % 3 != 0 and item % 2 != 0), lista))
    return primos


# impressão dos números primos
print(f"Os primos dessa lista são: {isPrimo(novaLista)}")
