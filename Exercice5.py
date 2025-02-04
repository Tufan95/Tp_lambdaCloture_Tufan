# Question 1 : Définition de la fonction compose
def compose(f, g):
    return lambda x: f(g(x))

# Question 2 : Composition de deux expressions lambda
square = lambda x: x ** 2
increment = lambda x: x + 1

# Test de la fonction composée
composed_function = compose(square, increment)
print(composed_function(3)) 