moves = [
    ("apple", +10),
    ("banana", +5),
    ("apple", -3),
    ("orange", +7),
    ("banana", -2),
]

def compute_inventory(moves):
    dico = {}
    for product, quantity in moves:
        if product not in dico:
            dico[product] = quantity
        else:
            dico[product] += quantity
    print(dico)

compute_inventory(moves)