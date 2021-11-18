lista_zakupow_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

lista_zakupow_dict1 = {k: [v.capitalize() for v in lista_zakupow_dict[k] ] for k in lista_zakupow_dict }

for shop in lista_zakupow_dict1:
    print(f"Ide do {shop.capitalize()}, kupuję tu następujące rzeczy {lista_zakupow_dict1[shop]}")
print(f"W sumie kupuję {len(lista_zakupow_dict1[shop]) * len(lista_zakupow_dict1)} produktów")

print("Commit_no1")
print("Commit_no2")
