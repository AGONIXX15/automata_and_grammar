
from state_machine import fsm_mod3, fsm_mod5, fsm_verify
"0000001"
string: str = "1000000"
res: int = 0
for c in string:
    res = 2 * res + int(c)
    print(res)

# (a * 2 + b) = res
# res = a
# res = (a * 2 + b) mod m
# res = (a mod m * 2 mod m + b mod m)
# res = (res * 2 + b) mod m


for i in range(0, 10000, 5):
    print(fsm_mod5(bin(i)[2:]))

