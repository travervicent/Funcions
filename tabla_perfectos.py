# Este es un comentari sobre el programa
# Escriu un taula amb tos el nombres perfectes entre 1 i n
# Segona versió

def es_perfecto(n):
    sumatorio = 0
    for i in range(1, n):
        if n % i == 0:
            sumatorio += i
    return sumatorio == n

def tabla_perfectos(n):
    perfectos = []
    for i in range(1, n + 1):
        if es_perfecto(i):
            print(i, " és un nombre perfecte")
                  
número = int(input("Introdueix un nombre enter positiu: "))
tabla_perfectos(número)

