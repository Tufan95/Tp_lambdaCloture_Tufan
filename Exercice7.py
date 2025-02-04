# Question 1 : Définition de la fonction memoize
def memoize(func):
    cache = {}
    def memoized_func(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return memoized_func

# Question 2 : Fonction de calcul de la factorielle
@memoize
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# Fonction de calcul de Fibonacci
@memoize
def fibonacci(n):
    return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)

print("Factorielle de 7:", factorial(5))
print("Fibonacci de 15:", fibonacci(10))