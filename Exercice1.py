from functools import reduce

# Question 1.1 : Expression lambda pour calculer le carré d'un nombre
square = lambda x: x ** 2  # Déclare une fonction lambda qui calcule le carré d'un nombre

# Question 1.2 : Application de cette fonction avec map() sur une liste de nombres
numbers = [1, 2, 3, 4, 5]  # Crée une liste de nombres
squared_numbers = list(map(square, numbers))  # Applique la fonction square à chaque élément de la liste numbers en utilisant map() et convertit le résultat en liste
print("Carrés des nombres:", squared_numbers)  # Affiche les carrés des nombres

# Question 1.3 : Expression lambda pour calculer la somme de deux nombres
sum_two_numbers = lambda a, b: a + b  # Déclare une fonction lambda qui calcule la somme de deux nombres

# Question 1.4 : Réduction de la liste en une somme totale avec reduce()
total_sum = reduce(sum_two_numbers, numbers)  # Utilise reduce() pour appliquer la fonction sum_two_numbers de manière cumulative à la liste numbers, réduisant la liste à une somme totale
print("Somme totale:", total_sum)  # Affiche la somme totale des nombres
