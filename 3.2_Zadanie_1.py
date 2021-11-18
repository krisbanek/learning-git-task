lista_zakupow_dict = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

lista_zakupow_dict1 = {k: [v.capitalize() for v in lista_zakupow_dict[k] ] for k in lista_zakupow_dict }
