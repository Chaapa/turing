def get_program():
    d = {}
    while True:
        inp = input().split()
        if inp[0] == 'end':
            return d
        if not inp[0] in d:
            d[inp[0]] = {inp[1]: inp[2:]}
        else:
            d[inp[0]].update({inp[1]: inp[2:]})


def check_line(st):
    state = 'q1'
    ind = 0
    for _ in range(1000):
        if state == 'q0':
            if sum([int(i) for i in st[:ind]]) == 0:
                st = st[ind:]
            return f'{st} результат работы программы'
        elif not st[ind] in program[state]:
            if sum([int(i) for i in st[:ind]]) == 0:
                st = st[ind:]
            return f'{st[:-1]} результат работы программы'
        new_state, new_value, move = program[state][st[ind]]
        st[ind] = new_value
        ind += all_moves[move]
        if ind < 0:
            ind += 1
            st = [empty_symbol] + st
        elif ind >= len(st):
            st = st + [empty_symbol]
        state = new_state
        # print(st)
    return 'Программа не применима'


print('Введите свою программу, которая будет оканчиваться словом end ')
program = get_program()
empty_symbol = input('Введите символ, который вы хотите, чтобы считался пустым ')
all_moves = {'R': 1, 'L': -1, 'S': 0}
# print(program)
while True:
    line = list(input('Введите слово, которое вы хотите обозревать '))
    print(check_line(line))
