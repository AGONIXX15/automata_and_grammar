from comprobar import earley_parser
from gramatic import check

v = {'a', 'b', 'A'}
s = 'S'
t = {'a', 'b'}
p = {
    'S': ['A', 'B'],
    'A': ['aA', 'b'],
    'B': ['bB', 'aA', 'bS', 'AB'],
}

print(earley_parser(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb", p, s, v))  # True

# print(check(v, t, s, p,
#       "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", 100))  # True
