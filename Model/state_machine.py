
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

    # 0 o 1
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


def fsm_verify(precompute: list[int], string: str, index: int) -> bool:
    if fsm_mod3(string) == 0 and (5 - fsm_mod5(string)) % 5 == precompute[index]:
        print(index)
        return True
    return False


# (a + b) % 5 == 0
# (a + 18) % 5 == 0
# a = -18 mod 5
# -18 mod 5 === (5 - (18 mod 5)) mod 5

# (a + b) mod m === 0
# a = -b mod m
# -b mod m === (m -(b mod m)) mod m

def fsm_final(transmisions: list[str], checksum: list[str]):
    precompute: list[int] = [int(x, 2) for x in checksum]
    count: int = 0
    for index, transmision in enumerate(transmisions):
        count += 1 if fsm_verify(precompute, transmision[9:14], index) else 0
    return count/len(transmisions) * 100


if __name__ == '__main__':
    transmisiones = [
        "01001001110101101100101101010110",
        "11000101100101011010001001001011",
        "10111001110010111010100100100101",
        "01101100110001001011101010101010",  # valida
        "00111011011011000101011011100100",
        "10011011101110110111011101010101",
        "01110110100010101010101011011001",
        "00100101110011010101010011101001",  # valida
        "11101010010111011101010110101100",  # valida
        "10011110010010101001011101010110"
    ]
# 10010 18
# 0010 2
# 18 + 2 = 20 % 5 == 0
    validacion = [
        "0010",  # 2
        "0101",  # 5
        "1000",  # 8
        "1111",   # 15
        "0010",  # 2
        "0101",  # 5
        "1000",  # 8
        "1111",  # 15
        "0010",  # 2
        "0010",  # 2
    ]

    print(fsm_final(transmisiones, validacion))
    print(fsm_mod5("00000101"))
