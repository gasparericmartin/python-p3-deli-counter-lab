katz_deli = []

def line(katz_deli):
    if len(katz_deli) > 0:
        callout = 'The line is currently:'
        for person in katz_deli:
            callout += f' {katz_deli.index(person) + 1}. {person}'

        print(callout)
    else:
        print('The line is currently empty.')

def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f'Welcome, {name}. You are number {len(katz_deli)} in line.')

def now_serving(katz_deli):
    if len(katz_deli) > 0:
        print(f'Currently serving {katz_deli[0]}.')
        del katz_deli[0]
    else:
        print('There is nobody waiting to be served!')