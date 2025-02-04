# Question 2.1 : Définition de la fonction create_multiplier
def create_multiplier(n):
    return lambda x: x * n

# Question 2.2 : Création des fonctions double et triple
double = create_multiplier(2)
triple = create_multiplier(3)

# Question 2.3: Test des fonctions
print("Double de 5:", double(5))
print("Triple de 5:", triple(5))
