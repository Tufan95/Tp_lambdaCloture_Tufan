# Question 3.1 : Définition d'une liste de mots
words = ["arbre", "maison", "avion", "voiture", "ordinateur", "animal", "école"]

# Question 3.2 : Filtrer les mots qui commencent par "a"
words_starting_with_a = list(filter(lambda word: word.startswith('a'), words))
print("Mots commençant par 'a':", words_starting_with_a)


# Question 3.3: Clôture pour compter les mots de plus de 5 caractères
def count_long_words():
    count = 0
    def counter(word):
        nonlocal count
        if len(word) > 5:
            count += 1
        return count
    return counter

word_counter = count_long_words()
for word in words:
    word_counter(word)
print("Nombre de mots > 5 caractères:", word_counter("") )