# Este es un comentari sobre el programa
# Calcula si un nombre és perfecte, es a dir que tots els seus divisors sumen el mateix nombre
def es_perfecto(n):
    sumatorio = 0
    for i in range(1, n):
        if n % i == 0:
            sumatorio += i
    return sumatorio == n

print(es_perfecto(28))

