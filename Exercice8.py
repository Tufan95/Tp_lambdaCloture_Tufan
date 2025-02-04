# Question 3 : Définition de la fonction calculateDiscount
def calculateDiscount(products, discount_func):
    return sum(discount_func(price) for price in products)

# Question 4 : Liste des prix des produits
product_prices = [100, 200, 50, 75, 150]

# Définition de la réduction de 20%
discount_20 = lambda price: price * 0.8

# Calcul du montant total après réduction
total_after_discount = calculateDiscount(product_prices, discount_20)

print("Montant total après réduction de 20%:", total_after_discount)
