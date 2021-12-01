# created by Илья Данилов
# date 09.11.2021
# description Банковские счета

def deposit(name, money):
    if name in bank_dict:
        bank_dict[name] += money
    else:
        bank_dict[name] = money
    # print('deposit', name, bank_dict[name])


def withdraw(name, money):
    if name in bank_dict:
        bank_dict[name] -= money
    else:
        bank_dict[name] = -money
    # print('withdraw', name, bank_dict[name])


def balance(name):
    if name in bank_dict:
        bank_operation.append(bank_dict[name])
    else:
        bank_operation.append('ERROR')


def transfer(name1, name2, money):
    if name1 in bank_dict:
        bank_dict[name1] -= money
    else:
        bank_dict[name1] = -money
    if name2 in bank_dict:
        bank_dict[name2] += money
    else:
        bank_dict[name2] = money
    # print(money)


def income(p):
    try:
        percent = float(p) / 100
    except (ValueError, TypeError):
        print('ERROR INCOME')
    else:
        for name in bank_dict:
            if bank_dict[name] > 0:
                bank_dict[name] = bank_dict[name] + int((bank_dict[name] * percent))
        # print(bank_dict.values())


def action(action_list):
    try:
        upper_action = action_list[0].upper()
        first_name = action_list[1].upper()
        second_name = 'bank_admin'
        money = 0
        if len(action_list) > 2:
            second_name = action_list[2].upper()
            money = int(action_list[-1])
    except (ValueError, TypeError):
        print('Invalid Data!')
    else:
        if upper_action == 'DEPOSIT':
            deposit(first_name, money)
        elif upper_action == 'WITHDRAW':
            withdraw(first_name, money)
        elif upper_action == 'BALANCE':
            balance(first_name)
        elif upper_action == 'TRANSFER':
            transfer(first_name, second_name, money)
        elif upper_action == 'INCOME':
            income(first_name)
        else:
            print('Invalid Data!')


if __name__ == '__main__':
    bank_dict = dict()
    bank_operation = list()
    while True:
        try:
            action_input = list(map(str, input().split()))
        except (ValueError, TypeError):
            print('Invalid Data!')
        except EOFError:
            for x in bank_operation:
                print(x)
            break
        else:
            action(action_input)
