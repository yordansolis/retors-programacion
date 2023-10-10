# n se disminuye en 1
# factorial(n - 1) es la llamada recursiva  hace que la funcone se llame automatico
# matematicamente es como si buscara el numero imaginario es decir:



def factorial(n):

    if n == 0:
        return 1

    else:
        print("prin", n)
        return  factorial(n - 1) #  1! = {1}, 2! = {2}, 3! = {6}


print(factorial(4))

# factorial(4) llama a factorial(3).
# factorial(3) llama a factorial(2).
# factorial(2) llama a factorial(1).
# factorial(1) llama a factorial(0).

# En ese momento, factorial(0) retorna 1, y luego las llamadas recursivas se resuelven en orden inverso:

# factorial(1) retorna 1 * 1 = 1.
# factorial(2) retorna 2 * 1 = 2.
# factorial(3) retorna 3 * 2 = 6.
# factorial(4) retorna 4 * 6 = 24.