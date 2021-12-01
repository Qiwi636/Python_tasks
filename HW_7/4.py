# created by Илья Данилов
# date 06.11.2021
# description Подсчет уровней родства


def find_level_of_kinship(name, names, lvls):
    if name not in names:
        lvls[name] = 0
        return 0
    parent = names[name]
    if parent in lvls:
        lvl = lvls[parent] + 1
    else:
        lvl = find_level_of_kinship(parent, names, lvls) + 1
    lvls[name] = lvl
    return lvl


def create_level_dict(dict_names, lvl_total):
    for name in dict_names:
        if name not in lvl_total:
            find_level_of_kinship(name, dict_names, lvl_total)

    for name in sorted(lvl_total):
        print(name, lvl_total[name])


if __name__ == '__main__':
    kinship_dict = dict()
    kinship_set = set()
    height_dict = dict()
    try:
        value = int(input('max human value: '))
        for _ in range(1, value):
            kinship = list(map(str, input().split()))
            kinship_dict[kinship[0]] = kinship[1]
            kinship_set.add(kinship[0])
            kinship_set.add(kinship[1])
    except (ValueError, TypeError):
        print('ERROR!')
    except EOFError:
        create_level_dict(kinship_dict, height_dict)
    else:
        create_level_dict(kinship_dict, height_dict)
