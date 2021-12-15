def cookbook_constructor(cookbook='cookbook.txt'):
    def organizer(ingredient_list):
        ingredient_dict = {}
        ingredient_dict['ingredient_name'] = ingredient_list[0]
        ingredient_dict['quantity'] = ingredient_list[1]
        ingredient_dict['measure'] = ingredient_list[2]
        return ingredient_dict
    dishes = {}
    with open(cookbook, 'r', encoding='utf-8') as file:
        for item in file:
            key_dish = item.strip()
            dishes[key_dish] = []
            counter = int(file.readline().strip())
            while counter > 0:
                ingredient_list = file.readline().strip().split('|')
                dishes[key_dish].append(organizer(ingredient_list))
                counter -= 1
            file.readline()
    return dishes


def get_shop_list_by_dishes(dishes, person_count):
    cookbook = cookbook_constructor()
    temporary_dict = {}
    for item in dishes:
        if item in cookbook:
            temporary_dict[item] = cookbook[item]
    for item in temporary_dict:
        for entry in temporary_dict[item]:
            entry['quantity'] = int(entry['quantity']) * person_count
            entry = {entry.pop('ingredient_name'): entry}
    return temporary_dict


def text_fetch(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        trimmed_lines = []
        for line in file:
            trimmed_lines.append(line.strip())
    return trimmed_lines


def sort_and_merge(*args, **kwargs):
    temp_list_args = list(args)
    temp_values_kwargs = list(kwargs.values())
    merged_list = temp_list_args + temp_values_kwargs
    comparison_dict = {}
    for item in merged_list:
        with open(item, 'r', encoding='utf-8') as file:
            line_len = len(file.readlines())
            comparison_dict[line_len] = item
    write_order = list(comparison_dict.keys())
    write_order.sort()
    write_order.reverse()
    # print(comparison_dict)
    with open('result.txt', 'w', encoding='utf-8') as document:
        document.write(''.strip())
    for line_len in write_order:
        with open('result.txt', 'a', encoding='utf-8') as document:
            document.write(f'{comparison_dict[line_len]}\n')
            trimmed_lines = text_fetch(comparison_dict[line_len])
            for line in trimmed_lines:
                document.write(f'{line}\n')


print(cookbook_constructor())
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 12))
sort_and_merge('1.txt', '2.txt', '3.txt')
