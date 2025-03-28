from itertools import permutations

def solve_cryptarithmetic():
    for perm in permutations(range(10), 8):
        mapping = dict(zip("SENDMORY", perm))
        if mapping['S'] == 0 or mapping['M'] == 0:
            continue
        send = mapping['S']*1000 + mapping['E']*100 + mapping['N']*10 + mapping['D']
        more = mapping['M']*1000 + mapping['O']*100 + mapping['R']*10 + mapping['E']
        money = mapping['M']*10000 + mapping['O']*1000 + mapping['N']*100 + mapping['E']*10 + mapping['Y']
        if send + more == money:
            print(f"SEND: {send}, MORE: {more}, MONEY: {money}")
            return

solve_cryptarithmetic()
