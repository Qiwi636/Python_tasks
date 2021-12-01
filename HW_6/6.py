# created by Илья Данилов
# date 27.10.2021
# description Телефонные номера

def formatter(list_contact):
    for f in range(len(list_contact)):
        list_contact[f] = list_contact[f].replace('+', ''). \
            replace('(', '').replace(')', '').replace('-', '')
        if list_contact[f][0] == '7':
            list_contact[f] = '8' + list_contact[f][1:]
        if len(list_contact[f]) < 11:
            list_contact[f] = '8495' + list_contact[f][0:]
    return list_contact


def contacts_check(list_contact):
    compared = list_contact[0]
    for f in range(1, len(list_contact)):
        if list_contact[f] == compared:
            print('YES')
        else:
            print('NO')


if __name__ == '__main__':
    try:
        contact_input = input()
        existing_contacts = list()
        existing_contacts.append(contact_input)
        for x in range(3):
            existing_contacts.append(input())
    except (ValueError, TypeError):
        print('ERROR!')
    else:
        list_formatter = formatter(existing_contacts)
        contacts_check(list_formatter)
