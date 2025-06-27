
"""
00000101
res = (2 * res + bit) % 5
res = 1
res = (2*1 + 0) % 5
res  = 2
res = (2 * 2 + 1) % 5
res = 0
"""


def fsm_mod3(string: str):
    """estados vienen siendo q0 = 0, q1 = 1 q2 = 2
    pq vamos a calcular solo el modulo de 3
    formula de estado (residuo * 2 + bit) % 3"""
    # q0 estado inicial
    state: int = 0

    transitions = {
        0: {'0': 0, '1': 1},
        1: {'0': 2, '1': 0},
        2: {'0': 1, '1': 2}
    }

    for bit in string:
        state = transitions[state][bit]

    return state


def fsm_mod5(string: str):
    """estados vienen siendo q0 = 0, q1 = 1, q2 = 2,
    q3 = 3,  q4 = 4
    pq vamos a calcular solo el modulo de 5
    formula de estado (residuo * 2 + bit) % 5"""
    # q0 estado inicial
    state: int = 0

    transitions = {
        0: {'0': 0, '1': 1},
        1: {'0': 2, '1': 3},
        2: {'0': 4, '1': 0},
        3: {'0': 1, '1': 2},
        4: {'0': 3, '1': 4}
    }

    for bit in string:
        state = transitions[state][bit]

    return state


def fsm_verify(precompute: set[int], string: str):
    if fsm_mod3(string) == 0 and (5 - fsm_mod5(string)) % 5 in precompute:
        return True
    return False


# (a + b) % 5 == 0

# (a + b) mod m === 0
# a = -b mod m
# -b mod m === (m -(b mod m)) mod m

def fsm_final(transmisions: list[str], checksum: list[str]):
    precompute: set[int] = {int(x, 2) for x in checksum}
    count: int = 0
    for transmision in transmisions:
        count += 1 if fsm_verify(precompute, transmision[9:14]) else 0
    return count/len(transmisions) * 100