from pprint import pprint


def cook_book_from_files(path):
    cook_book = dict()
    with open(path, 'r', encoding='utf-8') as f:
        while True:
            dish = f.readline().strip()
            if not dish:
                break
            cook_book[dish] = []

            ingridients_number = int(f.readline())
            for i in range(ingridients_number):
                ingridient_name, quantity, measure = f.readline().strip().split(' | ')
                cook_book[dish].append({
                    'ingridient_name': ingridient_name,
                    'quantity': int(quantity),
                    'measure': measure,
                })

            f.readline()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingridients = dict()

    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] in ingridients:
                ingridients[ingridient['ingridient_name']]['quantity'] += ingridient['quantity'] * person_count
            else:
                ingridients[ingridient['ingridient_name']] = {
                    'measure': ingridient['measure'],
                    'quantity': ingridient['quantity'] * person_count
                }

    return ingridients


cook_book = cook_book_from_files('recipes.txt')
pprint(cook_book)
pprint(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2))
