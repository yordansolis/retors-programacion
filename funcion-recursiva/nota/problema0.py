# def suma_naturales(n):
#     if n == 1:
#         return 1
#     else:
#         return n + suma_naturales(n - 1)



# print(suma_naturales(1))  # Debería devolver 1
# print(suma_naturales(5))  # Debería devolver 15 (1 + 2 + 3 + 4 + 5)
# print(suma_naturales(10)) # Debería devolver 55 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)



def resta_naturales(n):
    if n == 1:
        print('vr',n)
        return 1
    else:
        print(n)
        return n - resta_naturales(n - 1)


print(resta_naturales(5))  # Debería devolver 3 (n5-4= 3,  n3-2=1, n1=1 res(2)+1 del retorno)

# print(resta_naturales(1))  # Debería devolver 1
# print(resta_naturales(10)) # Debería devolver 5 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10)



